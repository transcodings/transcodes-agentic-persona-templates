---
name: sync-with-team
description: Version Personas, share Knowledge Bases, and use Organization — use when asked about sync, versions, upload, pull, tags, backups, invites, 조직, 동기화, or 최신 버전.
---

# Prerequisites
- Signed in. Cloud sync and invites need Standard.
- Persona vs Knowledge Base.
- Exact name, and whether they are uploading this device or getting the team copy.

# Steps
1. Open Transcodes Desktop → Organization. Four tabs: Members, Personas, Knowledge Bases, Organization (plan and org name).
2. Personas tab and Knowledge Bases tab each have two tables:
   - Needs attention — local only, organization only, local changes, update available, conflict.
   - Up to date / 최신 상태 — already In Sync.
3. Read the status before clicking:
   - Local Only / 로컬만 — this device only. **Sync to Cloud / 클라우드 동기화**. Type a tag the team will recognize (not a version number).
   - Organization Only — on the team, not here. **Get Latest / 최신 버전 받기**.
   - Local Changes — edited here. Upload to share, or Undo My Changes to throw away the local edit (a backup is saved first).
   - Update Available — team is newer. Get Latest.
   - Conflict — both sides changed. Get Latest saves a local backup first.
   - In Sync / 동기화됨 — nothing required.
4. Persona upload creates a new revision (v1, v2, …) plus the tag. The current table shows remote revision, current revision, tag, and who updated it.
5. Knowledge Base upload does not create a revision list. It replaces the one shared latest copy and updates the tag. Do not promise an old Knowledge version they can restore from the team.
6. Local backups are on this device, made right before an overwrite. Restore replaces this device only. The team copy does not change.
7. Members tab: Invite. An accepted member is a billed seat on Standard. Owners can transfer ownership, suspend, or remove.
8. After Get Latest, Apply the Persona to each project folder that should see the new copy. Sync is not Apply. Uploading does not update Claude or Cursor until someone Applies (or auto-apply runs on a remembered folder on this device).
9. If a Persona push fails because a linked Knowledge Base is unpublished, upload that Knowledge Base first, or unlink it.

# Gotchas
- Signed-out Organization tabs cannot list remotes.
- Knowledge Bases have no “go back to v3” on the team. Personas do.
- Deleting the organization Knowledge Base copy is not available in the plugin. Use Desktop.
- Restoring a backup does not Apply by itself if they also need other machines updated — those machines Get Latest, then Apply.

# Output
**Deliverable** — Which item, which table, upload or download, tag or revision, backup if any, and whether a project Apply is still required.
**Done when** — The Organization table shows the intended state and they know which folders still need Apply.
