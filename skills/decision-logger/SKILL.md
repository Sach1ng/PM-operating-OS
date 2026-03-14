---
name: decision-logger
description: "Capture decision traces — the reasoning behind key PM decisions. Use after PRD approvals, scope changes, launch/kill calls, prioritization shifts, or any significant product decision."
---

# Decision Logger

Capture the reasoning behind key product decisions as structured, append-only traces. This builds the "event clock" — the record of *why* things became true, not just *what* is true now.

## When to Use

- After a PRD is approved or rejected
- After a scope change or pivot
- After a launch/kill/iterate decision on an experiment
- After a prioritization shift (quarterly planning, reprioritization)
- After a significant stakeholder alignment (exec review, cross-functional agreement)
- When asked "log this decision", "record why we decided this", or "decision trace"

## Process

### 1. Identify the Decision

Ask if not obvious from context:
- What was decided? (1 sentence)
- What triggered this decision? (signal, meeting, data, escalation)

### 2. Capture the Trace

Gather the following — from conversation context, user input, or by asking:

- **Decision**: What was decided (1 sentence)
- **Date**: When the decision was made
- **Context**: What prompted this — the signal, conversation, or data point
- **Alternatives considered**: What other options were on the table (at least 2)
- **Evidence**: What data, insight, or customer signal drove the call
- **Stakeholders**: Who was involved, who approved, who dissented
- **Expected outcome**: What we expect to happen as a result
- **Risk / reversal cost**: How hard is this to undo if wrong
- **Tags**: strategic-pillar, metric, segment, experiment (for retrieval)

### 3. Write the Entry

Save to `memory/decisions/YYYY-MM-DD_short-slug.md` using this format:

```markdown
# [Decision title]

**Date:** YYYY-MM-DD
**Type:** [PRD approval | Scope change | Launch/Kill | Prioritization | Alignment | Other]
**Tags:** [pillar, metric, segment]

## Decision
[1-2 sentences: what was decided]

## Context
[What prompted this — the trigger]

## Alternatives Considered
1. **[Option A]** — [brief description, why not chosen]
2. **[Option B]** — [brief description, why not chosen]

## Evidence
- [Data point, customer insight, or signal that drove the call]

## Stakeholders
- **Decision maker:** [who]
- **Consulted:** [who]
- **Informed:** [who]

## Expected Outcome
[What we expect to happen, and how we'll know]

## Risk / Reversal Cost
[How hard is this to undo — low/medium/high, and why]
```

### 4. Confirm with User

Show the drafted entry. Ask the user to confirm or adjust before saving.

## Output

A timestamped decision trace saved to `memory/decisions/`. Append-only — never overwrite existing entries.

Over time, these traces enable:
- **Recall**: "Why did we decide X?"
- **Pattern detection**: "We've killed 3 pricing experiments in a row"
- **Drift detection**: "Strategy says X but decisions are moving toward Y"
- **Counterfactual reasoning**: "What if we'd chosen the alternative?"
