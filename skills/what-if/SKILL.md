---
name: what-if
description: "Simulate the impact of a proposed decision using accumulated context. Use when asked 'what if', 'what would happen if', 'impact analysis', 'simulate this decision', or 'trade-off analysis'."
---

# What-If Simulation

Simulate the impact of a proposed product decision by reasoning over accumulated organizational context — strategy, past decisions, customer feedback, and execution history. This is the "world model" layer: if the system can answer "what if" grounded in real context, it's more than a search index.

## When to Use

- Evaluating a proposed prioritization change ("What if we deprioritize mobile?")
- Assessing a strategic pivot ("What if we shift ICP from SMB to enterprise?")
- Analyzing experiment patterns ("We've killed 3 pricing experiments — what does that mean?")
- Trade-off decisions ("Should we invest in feature A or feature B?")
- Risk assessment ("What's the blast radius of cutting this team's scope?")
- When asked "what if", "what would happen", "simulate", "impact analysis", or "trade-off analysis"

## Process

### 1. Clarify the Hypothetical

Ask if not clear from context:
- **Proposed action**: What change is being considered? (1 sentence)
- **Scope**: What does it affect? (product, team, segment, timeline)
- **Constraint**: Is this reversible? What's the time horizon?

### 2. Load Context

Read the following to ground the simulation in actual organizational context:

- **`knowledge/` (strategy, segments, metrics, competitive landscape)** — the baseline "world model"
- **`memory/decisions/`** — past decision traces for precedent and pattern
- **`memory/feedback/`** — customer signals that would be affected
- **`memory/weekly-plans/`** — current execution state and momentum
- **`memory/strategy-reviews/`** — alignment patterns and recurring gaps

### 3. Run the Simulation

For the proposed action, analyze:

**A. Strategic Impact**
- Which strategic pillars does this strengthen? Which does it weaken?
- Does this move toward or away from stated goals?
- Precedent: have similar decisions been made before? What happened?

**B. Customer Impact**
- Which customer segments are affected? (reference `knowledge/customer-segments.md`)
- Does customer feedback data support or contradict this direction?
- What customer pain points get addressed vs. neglected?

**C. Metric Impact**
- Which key metrics move? In which direction?
- Are there second-order effects? (e.g., deprioritizing mobile affects engagement, which affects retention)
- What guardrail metrics might regress?

**D. Execution Impact**
- What current work gets affected? (reference recent plans)
- What dependencies break or change?
- What new work does this create?

**E. Competitive Impact**
- Does this open or close gaps with competitors? (reference `knowledge/competitive-landscape.md`)
- Does this create differentiation or reduce it?

**F. Risk Assessment**
- What's the worst-case outcome?
- How reversible is this decision?
- What early signals would indicate this was the wrong call?

### 4. Surface the Trade-offs

Frame the analysis as explicit trade-offs:
- **You gain:** [what improves]
- **You lose:** [what degrades]
- **You risk:** [what could go wrong]
- **You assume:** [what must be true for this to work]

### 5. Recommend

Based on the accumulated context, provide:
- A clear recommendation (proceed / modify / reconsider)
- Conditions under which the recommendation changes
- Suggested experiment or validation step if uncertainty is high

## Output

```markdown
## What-If Analysis: [Proposed Action]

**Date:** YYYY-MM-DD
**Proposed action:** [1 sentence]

### Strategic Impact
- [Pillars strengthened/weakened]
- [Goal alignment assessment]
- [Precedent from decision history]

### Customer Impact
- [Segments affected]
- [Feedback alignment]

### Metric Impact
| Metric | Expected Direction | Confidence | Rationale |
|--------|--------------------|------------|-----------|
| [metric] | ↑/↓/→ | High/Med/Low | [why] |

### Execution Impact
- [Current work affected]
- [Dependencies]

### Competitive Impact
- [Gap analysis]

### Trade-offs
| You Gain | You Lose | You Risk | You Assume |
|----------|----------|----------|------------|
| [gain] | [loss] | [risk] | [assumption] |

### Recommendation
**[Proceed / Modify / Reconsider]**
- [Rationale grounded in context]
- [Conditions that would change this recommendation]
- [Suggested validation step]
```

The strength of this analysis depends on the depth of accumulated context in `memory/`. With sparse memory, flag low confidence and recommend building more context before committing.
