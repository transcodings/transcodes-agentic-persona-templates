// html2pptx — turn a 1920×1080 HTML deck (<section class="slide">) into an editable PPTX
//
// Walks each slide in paint (DOM) order and emits:
//   shape    every box with a background or border → native PowerPoint shape (editable)
//   text     every piece of text → native text box with the browser's line breaks (editable)
//   picture  what PowerPoint can't draw natively (::before/::after marks, SVG, images, gradients)
//            → transparent PNG cut from the page, placed at the same depth
//
// usage: node html2pptx.mjs <deck.html> <out.pptx>

import path from 'node:path'
import { pathToFileURL } from 'node:url'
import puppeteer from 'puppeteer-core'
import PptxGenJS from 'pptxgenjs'

const [input, output] = process.argv.slice(2)
if (!input || !output) {
  console.error('usage: node html2pptx.mjs <deck.html> <out.pptx>')
  process.exit(1)
}
const chromePath = process.env.CHROME || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

const PX_PER_IN = 96
const inch = (px) => px / PX_PER_IN
const pt = (px) => px * 0.75
const SCALE = 2 // picture resolution

// CSS family → PowerPoint font. Runs with Hangul use the Korean font
const FONT_MAP = { 'Pretendard Variable': 'Pretendard', 'General Sans': 'General Sans', 'JetBrains Mono': 'JetBrains Mono' }
const KOREAN_FONT = process.env.PPTX_KOREAN_FONT || 'Pretendard'
const LATIN_FONT = process.env.PPTX_LATIN_FONT // optional: replace every non-mono Latin font

// ================================================================ browser side
function extract() {
  const parseColor = (c) => {
    const m = c && c.match(/rgba?\(([^)]+)\)/)
    if (!m) return null
    const [r, g, b, a = 1] = m[1].split(/[ ,/]+/).filter(Boolean).map(Number)
    if (a === 0) return null
    const hex = [r, g, b].map((v) => Math.round(v).toString(16).padStart(2, '0')).join('').toUpperCase()
    return { hex, alpha: a }
  }

  const rotationOf = (el, slide) => {
    let deg = 0
    for (let n = el; n && n !== slide; n = n.parentElement) {
      const t = getComputedStyle(n).transform
      if (t && t !== 'none') {
        const [a, b] = (t.match(/matrix\(([^)]+)\)/)?.[1] || '1,0').split(',').map(Number)
        deg += (Math.atan2(b, a) * 180) / Math.PI
      }
    }
    return Math.round(deg * 100) / 100
  }

  // untransformed box relative to the slide, even when rotated
  const boxOf = (el, slide, origin) => {
    const r = el.getBoundingClientRect()
    const rot = rotationOf(el, slide)
    if (!rot) return { x: r.left - origin.left, y: r.top - origin.top, w: r.width, h: r.height, rot: 0 }
    const w = el.offsetWidth || r.width
    const h = el.offsetHeight || r.height
    return { x: r.left + r.width / 2 - origin.left - w / 2, y: r.top + r.height / 2 - origin.top - h / 2, w, h, rot }
  }

  const radiusPx = (v, w, h) => (v.endsWith('%') ? (parseFloat(v) / 100) * Math.min(w, h) : parseFloat(v) || 0)
  const isInline = (el) => getComputedStyle(el).display === 'inline'
  const hasPseudo = (el) =>
    ['::before', '::after'].some((p) => {
      const c = getComputedStyle(el, p).content
      return c && c !== 'none' && c !== 'normal'
    })

  let pictureId = 0

  return [...document.querySelectorAll('.slide')].map((slide) => {
    const origin = slide.getBoundingClientRect()
    const pageTop = origin.top + window.scrollY
    const out = { bg: parseColor(getComputedStyle(slide).backgroundColor), items: [], pictures: [] }

    // text owners: nearest non-inline ancestor of each text node
    const owners = new Map()
    const tw = document.createTreeWalker(slide, NodeFilter.SHOW_TEXT)
    for (let node = tw.nextNode(); node; node = tw.nextNode()) {
      if (!node.textContent.trim()) continue
      const parent = node.parentElement
      if (parent.closest('svg, script, style')) continue
      let owner = parent
      while (owner !== slide && isInline(owner)) owner = owner.parentElement
      if (!owners.has(owner)) owners.set(owner, [])
      owners.get(owner).push(node)
    }

    // picture runs: consecutive pictures (no shape in between) share one PNG
    let run = null
    const addPicture = (el, mode) => {
      if (!run) {
        run = { id: pictureId++, targets: [] }
        out.pictures.push(run)
        out.items.push({ type: 'picture', id: run.id })
      }
      el.dataset.ovRun = run.id
      el.dataset.ovMode = mode
      const r = el.getBoundingClientRect()
      run.targets.push({ l: r.left - origin.left, t: r.top - origin.top, r: r.right - origin.left, b: r.bottom - origin.top })
    }

    const addShapes = (el, cs) => {
      const box = boxOf(el, slide, origin)
      if (box.w < 1 || box.h < 1) return
      const fill = parseColor(cs.backgroundColor)
      const sides = ['Top', 'Right', 'Bottom', 'Left'].map((s) => ({
        w: cs[`border${s}Style`] === 'none' ? 0 : parseFloat(cs[`border${s}Width`]),
        c: parseColor(cs[`border${s}Color`]),
        dash: cs[`border${s}Style`]
      }))
      const visible = sides.map((s) => s.w > 0 && !!s.c)
      const uniform = visible.every(Boolean) && sides.every((s) => s.w === sides[0].w && s.c.hex === sides[0].c.hex)
      if (!fill && !visible.some(Boolean)) return

      const radius = radiusPx(cs.borderTopLeftRadius, box.w, box.h)
      const kind =
        radius >= Math.min(box.w, box.h) / 2 - 0.5 ? (Math.abs(box.w - box.h) < 1 ? 'ellipse' : 'round') : radius > 0 ? 'round' : 'rect'
      if (fill || uniform) {
        out.items.push({ type: 'shape', kind, ...box, radius, fill, line: uniform ? { w: sides[0].w, c: sides[0].c, dash: sides[0].dash } : null })
        run = null
      }
      if (!uniform) {
        const { x, y, w, h } = box
        sides.forEach((s, i) => {
          if (!visible[i]) return
          const d = s.w / 2
          const pos = [
            [x, y + d, x + w, y + d],
            [x + w - d, y, x + w - d, y + h],
            [x, y + h - d, x + w, y + h - d],
            [x + d, y, x + d, y + h]
          ][i]
          out.items.push({ type: 'line', x1: pos[0], y1: pos[1], x2: pos[2], y2: pos[3], line: { w: s.w, c: s.c, dash: s.dash } })
          run = null
        })
      }
    }

    const addText = (owner, nodes) => {
      const ocs = getComputedStyle(owner)
      const lineH = parseFloat(ocs.lineHeight) || parseFloat(ocs.fontSize) * 1.3
      const lines = [[]]
      let lastTop = null
      let rect = null
      const chars = []
      const walker = document.createTreeWalker(owner, NodeFilter.SHOW_TEXT | NodeFilter.SHOW_ELEMENT, {
        acceptNode(n) {
          if (n.nodeType === 1) {
            if (n.tagName === 'BR') return NodeFilter.FILTER_ACCEPT
            if (n !== owner && !isInline(n)) return NodeFilter.FILTER_REJECT
            return NodeFilter.FILTER_SKIP
          }
          return nodes.includes(n) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP
        }
      })
      const range = document.createRange()
      for (let n = walker.nextNode(); n; n = walker.nextNode()) {
        if (n.nodeType === 1) {
          lines.push([])
          lastTop = null
          continue
        }
        const pel = n.parentElement
        const cs = getComputedStyle(pel)
        const style = {
          font: cs.fontFamily.split(',')[0].replace(/["']/g, '').trim(),
          size: parseFloat(cs.fontSize),
          bold: parseInt(cs.fontWeight, 10) >= 600,
          italic: cs.fontStyle === 'italic',
          color: parseColor(cs.webkitTextFillColor) || parseColor(cs.color),
          spacing: parseFloat(cs.letterSpacing) || 0,
          underline: cs.textDecorationLine.includes('underline'),
          upper: cs.textTransform === 'uppercase',
          href: pel.closest('a')?.href
        }
        const text = n.textContent
        for (let i = 0; i < text.length; i++) {
          range.setStart(n, i)
          range.setEnd(n, i + 1)
          const r = [...range.getClientRects()].find((q) => q.width > 0)
          if (!r) continue
          const ch = /\s/.test(text[i]) ? ' ' : text[i]
          if (lastTop !== null && r.top > lastTop + lineH * 0.5) lines.push([])
          if (lastTop === null || r.top > lastTop + lineH * 0.5) lastTop = r.top
          const line = lines[lines.length - 1]
          if (ch === ' ' && (!line.length || line[line.length - 1].text.endsWith(' '))) continue
          const prev = line[line.length - 1]
          if (prev && prev.style === style) prev.text += ch
          else line.push({ text: ch, style })
          rect = rect
            ? { l: Math.min(rect.l, r.left), t: Math.min(rect.t, r.top), r: Math.max(rect.r, r.right), b: Math.max(rect.b, r.bottom) }
            : { l: r.left, t: r.top, r: r.right, b: r.bottom }
          chars.push({ cx: r.left + r.width / 2, cy: r.top + r.height / 2, size: parseFloat(cs.fontSize) })
        }
      }
      const clean = lines
        .map((l) => {
          if (l.length) l[l.length - 1].text = l[l.length - 1].text.replace(/\s+$/, '')
          return l.filter((x) => x.text)
        })
        .filter((l) => l.length)
      if (!clean.length || !rect) return

      const rot = rotationOf(owner, slide)
      let box = { x: rect.l - origin.left, y: rect.t - origin.top, w: rect.r - rect.l, h: rect.b - rect.t, rot: 0 }
      if (rot) {
        // un-rotate each character around the owner's center to get the text's own box
        const or = owner.getBoundingClientRect()
        const ox = or.left + or.width / 2
        const oy = or.top + or.height / 2
        const a = (-rot * Math.PI) / 180
        let lb = null
        for (const c of chars) {
          const dx = c.cx - ox
          const dy = c.cy - oy
          const lx = dx * Math.cos(a) - dy * Math.sin(a)
          const ly = dx * Math.sin(a) + dy * Math.cos(a)
          const hw = c.size * 0.5
          const hh = lineH / 2
          lb = lb
            ? { l: Math.min(lb.l, lx - hw), t: Math.min(lb.t, ly - hh), r: Math.max(lb.r, lx + hw), b: Math.max(lb.b, ly + hh) }
            : { l: lx - hw, t: ly - hh, r: lx + hw, b: ly + hh }
        }
        const lcx = (lb.l + lb.r) / 2
        const lcy = (lb.t + lb.b) / 2
        const b = (rot * Math.PI) / 180
        const cx = ox + lcx * Math.cos(b) - lcy * Math.sin(b) - origin.left
        const cy = oy + lcx * Math.sin(b) + lcy * Math.cos(b) - origin.top
        const w = lb.r - lb.l
        const h = lb.b - lb.t
        box = { x: cx - w / 2, y: cy - h / 2, w, h, rot }
      }
      const ta = ocs.textAlign
      const align = ta === 'center' ? 'center' : ta === 'right' || ta === 'end' ? 'right' : 'left'
      out.items.push({ type: 'text', box, align, lineH: parseFloat(ocs.lineHeight) || null, lines: clean })
    }

    const visit = (el) => {
      const cs = getComputedStyle(el)
      if (cs.display === 'none' || cs.visibility === 'hidden' || parseFloat(cs.opacity) === 0) return
      if (el.tagName === 'svg' || el.tagName === 'IMG' || el.tagName === 'CANVAS') {
        addPicture(el, 'element')
        return
      }
      if (el !== slide) {
        if (cs.backgroundImage !== 'none') addPicture(el, 'element-bg')
        else addShapes(el, cs)
      }
      if (hasPseudo(el)) addPicture(el, 'pseudo')
      if (owners.has(el)) addText(el, owners.get(el))
      for (const child of el.children) visit(child)
    }
    visit(slide)

    // clip box for each picture run (pseudo-elements can sit a little outside their element)
    for (const p of out.pictures) {
      const pad = 80
      const l = Math.max(0, Math.min(...p.targets.map((t) => t.l)) - pad)
      const t = Math.max(0, Math.min(...p.targets.map((q) => q.t)) - pad)
      const r = Math.min(1920, Math.max(...p.targets.map((q) => q.r)) + pad)
      const b = Math.min(1080, Math.max(...p.targets.map((q) => q.b)) + pad)
      p.clip = { x: l, y: t, w: r - l, h: b - t, pageY: pageTop + t }
      delete p.targets
    }
    return out
  })
}

// ================================================================ node side
const browser = await puppeteer.launch({ executablePath: chromePath, headless: true, args: ['--hide-scrollbars'] })
try {
  const page = await browser.newPage()
  await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: SCALE })
  await page.goto(pathToFileURL(path.resolve(input)).href, { waitUntil: 'networkidle0', timeout: 60000 })
  await page.evaluate(async () => {
    await document.fonts.ready
    await Promise.all([...document.images].map((img) => (img.complete ? null : new Promise((r) => (img.onload = img.onerror = r)))))
  })

  const data = await page.evaluate(extract)

  // cut each picture run: hide everything except that run's pseudo-elements / SVG / images
  await page.addStyleTag({
    content: `
      html, body, .slide { background-color: transparent !important; }
      .slide, .slide *, .slide::before, .slide::after, .slide *::before, .slide *::after { visibility: hidden !important; }
    `
  })
  const runStyle = await page.evaluateHandle(() => {
    const s = document.createElement('style')
    document.head.append(s)
    return s
  })
  const pictures = new Map()
  for (const s of data) {
    for (const p of s.pictures) {
      await runStyle.evaluate((node, id) => {
        const sel = `[data-ov-run="${id}"]`
        node.textContent = `
          ${sel}[data-ov-mode="pseudo"]::before, ${sel}[data-ov-mode="pseudo"]::after { visibility: visible !important; }
          ${sel}[data-ov-mode="element"], ${sel}[data-ov-mode="element"] * { visibility: visible !important; }
          ${sel}[data-ov-mode="element-bg"] { visibility: visible !important; -webkit-text-fill-color: transparent !important; border-color: transparent !important; }
        `
      }, p.id)
      const buf = await page.screenshot({
        type: 'png',
        omitBackground: true,
        captureBeyondViewport: true,
        clip: { x: p.clip.x, y: p.clip.pageY, width: p.clip.w, height: p.clip.h }
      })
      pictures.set(p.id, { data: `data:image/png;base64,${Buffer.from(buf).toString('base64')}`, clip: p.clip })
    }
  }

  // ---- build the pptx
  const pptx = new PptxGenJS()
  pptx.defineLayout({ name: 'DECK', width: inch(1920), height: inch(1080) })
  pptx.layout = 'DECK'
  pptx.title = path.basename(input, path.extname(input))

  const color = (c) => (c ? { color: c.hex, transparency: Math.round((1 - c.alpha) * 100) } : {})
  const dash = (d) => (d === 'dashed' ? 'dash' : d === 'dotted' ? 'sysDot' : 'solid')
  const lineOf = (l) => ({ ...color(l.c), width: pt(l.w), dashType: dash(l.dash) })
  const hangul = (s) => /[ㄱ-힝]/.test(s)
  const fontFor = (run) => {
    if (hangul(run.text)) return KOREAN_FONT
    const f = FONT_MAP[run.style.font] || run.style.font
    return LATIN_FONT && !/mono/i.test(f) ? LATIN_FONT : f
  }

  let counts = { shapes: 0, texts: 0, pictures: 0 }
  for (const s of data) {
    const slide = pptx.addSlide()
    if (s.bg) slide.background = { color: s.bg.hex }

    for (const it of s.items) {
      if (it.type === 'line') {
        slide.addShape(pptx.ShapeType.line, {
          x: inch(Math.min(it.x1, it.x2)),
          y: inch(Math.min(it.y1, it.y2)),
          w: inch(Math.abs(it.x2 - it.x1)),
          h: inch(Math.abs(it.y2 - it.y1)),
          line: lineOf(it.line)
        })
        counts.shapes++
      } else if (it.type === 'shape') {
        const type = it.kind === 'ellipse' ? pptx.ShapeType.ellipse : it.kind === 'rect' ? pptx.ShapeType.rect : pptx.ShapeType.roundRect
        const opts = {
          x: inch(it.x),
          y: inch(it.y),
          w: inch(it.w),
          h: inch(it.h),
          rotate: it.rot || 0,
          fill: it.fill ? color(it.fill) : { type: 'none' },
          line: it.line ? lineOf(it.line) : { type: 'none' }
        }
        if (type === pptx.ShapeType.roundRect) opts.rectRadius = inch(Math.min(it.radius, Math.min(it.w, it.h) / 2))
        slide.addShape(type, opts)
        counts.shapes++
      } else if (it.type === 'picture') {
        const pic = pictures.get(it.id)
        slide.addImage({ data: pic.data, x: inch(pic.clip.x), y: inch(pic.clip.y), w: inch(pic.clip.w), h: inch(pic.clip.h) })
        counts.pictures++
      } else if (it.type === 'text') {
        const runs = []
        it.lines.forEach((line, li) => {
          line.forEach((run, ri) => {
            const st = run.style
            const o = {
              fontFace: fontFor(run),
              fontSize: Math.round(pt(st.size) * 10) / 10,
              bold: st.bold,
              italic: st.italic,
              ...color(st.color),
              align: it.align,
              lang: hangul(run.text) ? 'ko-KR' : 'en-US'
            }
            if (st.underline) o.underline = { style: 'sng' }
            if (st.spacing) o.charSpacing = Math.round(pt(st.spacing) * 10) / 10
            if (it.lineH) o.lineSpacing = Math.round(pt(it.lineH) * 10) / 10
            if (st.href) o.hyperlink = { url: st.href }
            if (ri === line.length - 1 && li < it.lines.length - 1) o.breakLine = true
            runs.push({ text: st.upper ? run.text.toUpperCase() : run.text, options: o })
          })
        })
        // one-line labels never wrap; paragraphs get room for a slightly wider fallback font
        const single = it.lines.length === 1
        const slack = single ? Math.max(12, it.box.w * 0.1) : Math.max(10, it.box.w * 0.08)
        const x = it.align === 'center' ? it.box.x - slack / 2 : it.align === 'right' ? it.box.x - slack : it.box.x
        slide.addText(runs, {
          x: inch(x),
          y: inch(it.box.y),
          w: inch(it.box.w + slack),
          h: inch(it.box.h),
          rotate: it.box.rot || 0,
          margin: 0,
          valign: 'top',
          align: it.align,
          wrap: !single,
          fit: 'none',
          paraSpaceBefore: 0,
          paraSpaceAfter: 0
        })
        counts.texts++
      }
    }
  }

  await pptx.writeFile({ fileName: path.resolve(output) })
  console.log(`${data.length} slides · ${counts.shapes} shapes · ${counts.texts} text boxes · ${counts.pictures} pictures → ${output}`)
} finally {
  await browser.close()
}
