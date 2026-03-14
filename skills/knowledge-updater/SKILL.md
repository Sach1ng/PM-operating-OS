---
name: knowledge-updater
description: "Update knowledge layer docs with automatic versioning. Use when updating strategy, segments, metrics, or competitive landscape. Snapshots the current state before overwriting so the retrospective agent can detect strategy drift."
---

# Knowledge Updater

Update knowledge layer documents (`knowledge/`) with automatic snapshotting. Before any update, the current version is saved to `memory/knowledge-snapshots/` so the retrospective agent can track how strategy evolved over time.

## When to Use

- Updating `knowledge/` files (strategy, segments, metrics, competitive landscape)
- After quarterly planning when strategy shifts
- After significant market or competitive changes
- When asked "update my strategy", "refresh knowledge docs", or "knowledge update"

## Process

### 1. Identify What's Changing

Ask if not clear:
- Which knowledge doc(s) are being updated?
- What changed? (new strategy, updated segments, revised metrics, competitive shift)
- Why? (quarterly planning, market shift, exec direction, experiment results)

### 2. Snapshot Current State

Before making any changes, save the current version:

1. Create a timestamped snapshot directory: `memory/knowledge-snapshots/YYYY-MM-DD/`
2. Copy the file(s) being updated into that directory with their original names
3. Add a `_changelog.md` file to the snapshot:

```markdown
# Knowledge Snapshot — YYYY-MM-DD

**Reason for update:** [what triggered this change]
**Files updated:** [list]

## Changes Summary
- [File 1]: [what changed and why]
- [File 2]: [what changed and why]
```

### 3. Make the Update

Edit the knowledge file(s) in `knowledge/{product}/` with the new content. Ensure:
- Format matches the existing template structure
- Changes are clearly reflected in the content
- No orphaned references (e.g., removing a segment that's referenced elsewhere)

### 4. Log as a Decision (optional)

If the knowledge update reflects a significant strategic shift, suggest logging it as a decision trace using the decision-logger skill.

## Output

- Updated knowledge file(s) in `knowledge/{product}/`
- Snapshot of previous version in `memory/knowledge-snapshots/YYYY-MM-DD/`
- Changelog documenting what changed and why

Over time, snapshots enable:
- **Drift detection**: How has stated strategy evolved quarter over quarter?
- **Decision coherence**: Do knowledge updates align with decision traces?
- **Retrospective analysis**: The retrospective agent compares current knowledge to snapshots to surface gradual shifts
