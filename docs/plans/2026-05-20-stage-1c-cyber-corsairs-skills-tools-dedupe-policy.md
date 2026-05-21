# Stage 1C: Cyber-Corsairs skills/tools dedupe and import policy

Scope: public, Git-tracked Cyber-Corsairs skill/tool files only. Private and ignored data remains out of scope: `.env*`, `.memory*`, databases, logs, token files, bot runtime data, caches, and ignored generated files.

Decision basis: user default for item 12 is B — import all non-duplicates. Therefore the default action is `import` for public, non-duplicate, reusable skill/tool assets after validation. Duplicate Hermes assets are skipped or merged, never blindly copied.

## Safe inventory snapshot

Collected from Git-tracked paths only using `git ls-files` and Git blob hashing.

Cyber-Corsairs tracked skill/tool inventory:

- Total tracked `skills/**` + `tools/**` files: 2,323
- `skills/hermes/**`: 773 files — skip as Hermes mirror/import duplicate
- `skills/superpowers/**`: 49 files — hold/manual review; do not blindly import
- Root/original Cyber-Corsairs skill directories excluding `hermes` and `superpowers`: 123 directories
- Root/original Cyber-Corsairs skill files excluding `hermes` and `superpowers`: 1,258 files
- `tools/**`: 243 files across 16 top-level tool categories

Hermes comparison inventory:

- Hermes tracked `skills/**`, `optional-skills/**`, and `tools/**`: 950 files
- Root Cyber-Corsairs skill-name overlaps with Hermes skill basenames: 2
- Known overlapping duplicate skill names: `design-md`, `humanizer`
- Exact content duplicate files among non-`skills/hermes`, non-`skills/superpowers` Cyber-Corsairs candidates: 170

Exact duplicate file categories found among otherwise importable candidates:

- Skill categories: document/PDF/slide/spreadsheet-style categories, one skill-creator file, one trading file, and one market-pulse group
- Tool categories: root package init, Gmail helper/reference, Hermes-reference material, memory helper/reference

These exact duplicates should be marked `skip-duplicate` at the file level unless a manual reviewer decides to merge a Cyber-Corsairs delta.

## Import policy

### 1. Hard skips

Always skip:

- `skills/hermes/**`
  - Rationale: tracked Cyber-Corsairs copy of Hermes material; importing it back creates loops and stale duplicates.
- Any file with exact blob hash already present in Hermes tracked skills/tools/optional-skills.
  - Rationale: no new content.
- Known duplicate skills `design-md` and `humanizer` as direct imports.
  - Rationale: name overlap with Hermes; route to merge review only if Cyber-Corsairs has useful deltas.
- Private/ignored/runtime files, even if referenced by public tools.
  - Rationale: privacy and Git hygiene.

### 2. Hold/manual review before import

Hold by default:

- `skills/superpowers/**`
  - Rationale: likely workflow overlap with Hermes software-development skills; import only selected unique workflows under a clear namespace or merge into existing Hermes skills.
- Any skill/tool category that depends on private Cyber-Corsairs operations, personal business accounts, private memory paths, Telegram chat IDs, local Google Drive paths, or credentials.
  - Public reusable logic may be extracted; operation-specific wrappers go to the private `cyber-corsairs` Hermes profile.
- Any file that references `.memory`, `.env`, token/config JSONs, databases, or logs.
  - Public docs/scripts may be sanitized; private access remains profile-only.

### 3. Default imports

Import all remaining Git-tracked, non-duplicate Cyber-Corsairs skills/tools when they pass gates:

- Public/generic marketing, content, ads, newsletter, design, GTM, CRO, product, SEO, video, research, and document-production skills.
- Generic templates, references, examples, and support assets required by imported skills.
- Generic CLI/tool wrappers and integration guides that do not require private state and can read credentials from normal Hermes profile configuration.

Preferred destination:

- Public generic skills: `skills/<domain>/<skill-name>/` in Hermes, using existing Hermes category conventions.
- Optional/heavy/niche skills: `optional-skills/<domain>/<skill-name>/` when they bring large dependencies, external service assumptions, or niche workflows.
- Generic reusable tools: plugin-first when possible under `plugins/<name>/`, or Hermes core `tools/` only if they are broadly useful, tested, and fit the existing registry model.
- Private operational tools/skills: profile-local only, outside Hermes Git.

### 4. Merge instead of copy

Use `merge-review` rather than direct import when:

- The Cyber-Corsairs item has the same skill name as a Hermes skill.
- Exact duplicate files are mixed with Cyber-Corsairs-only files in the same skill/tool category.
- The item is a fork or specialization of a Hermes tool/skill.
- The item improves existing Hermes behavior but should not create a second competing command/skill.

Merge output should be a small patch to the existing Hermes item plus attribution/provenance, not a copied duplicate tree.

## Manifest strategy

Create a sanitized manifest before copying. The manifest may be committed only if it contains public paths, hashes, statuses, and reviewer notes without private content.

Recommended manifest fields:

```yaml
source_repo: cyber-corsairs
source_path: skills/<public-path-or-category>
source_kind: skill | tool | reference | template | support-file
tracked_in_source_git: true
source_sha256: <git-blob-sha256-or-directory-merkle>
hermes_match:
  match_type: none | exact-file | exact-directory | name-overlap | semantic-overlap | private-reference
  hermes_category: <category-only-when-needed>
policy_status: import | skip-duplicate | merge-review | profile-only | hold-review | quarantine
recommended_target: hermes-repo | optional-skill | plugin | profile-local | skip
privacy_status: public-ok | needs-redaction | private-reference | blocked
license_attribution_status: ok | needs-attribution | needs-review
validation_status: pending | passed | failed
reviewer_notes: <short sanitized note>
```

Directory-level dedupe should use a Merkle-style hash over Git blob hashes plus relative paths. File-level exact duplicates should be dropped even when the surrounding directory is imported.

## Validation gates

Gate 1C-A: Safe source gate

- Source files are from `git ls-files` only.
- No ignored/private files are read or copied.
- No raw private content appears in manifests, logs, docs, or diffs.

Gate 1C-B: Dedupe gate

- `skills/hermes/**` is excluded.
- `skills/superpowers/**` is excluded from bulk import pending manual review.
- Exact hash duplicates are marked `skip-duplicate`.
- `design-md` and `humanizer` are marked `merge-review` or `skip-duplicate`, not direct import.

Gate 1C-C: Privacy/license gate

- Secret scan passes on staged import.
- References to `.env`, `.memory`, tokens, DBs, logs, private paths, chat IDs, and personal operations are removed, templated, or routed profile-local.
- Attribution/license material is preserved where applicable, including Cyber-Corsairs attribution files.

Gate 1C-D: Hermes compatibility gate

- Imported skills have valid frontmatter/metadata and resolve local references.
- Imported tools have dependency declarations, tests or smoke checks, and do not bypass Hermes credential handling.
- Slash-command/skill names do not conflict with existing Hermes names.

Gate 1C-E: Batch gate

- First import batch is small and reviewable.
- Public Git diff contains only sanitized, public assets.
- User approves before bulk import continues.

## Recommended next steps

1. Generate a sanitized manifest for all 2,323 tracked Cyber-Corsairs skill/tool files with the statuses above.
2. Pre-mark hard-skip categories:
   - `skills/hermes/**` as `skip-duplicate`
   - `skills/superpowers/**` as `hold-review`
   - exact hash duplicates as `skip-duplicate`
   - `design-md` and `humanizer` as `merge-review` or `skip-duplicate`
3. Classify the 123 original skill directories into public Hermes repo, optional-skill, profile-only, merge-review, or quarantine.
4. Classify the 16 top-level tool categories into public plugin/tool, profile-only operational tool, merge-review, or skip.
5. Run a first small import batch from low-risk public/generic skills only, then validate frontmatter, references, secret scan, and tests before expanding.
