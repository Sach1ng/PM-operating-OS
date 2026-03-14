---
name: prd-writer
description: "Use this skill when user asks to create, write, or draft a PRD (Product Requirements Document). Generates structured PRDs with governance framework, problem statements, business goals, use cases, and functional requirements."
---

# PRD Writer

Create comprehensive Product Requirements Documents following a structured PRD template format. This skill ensures consistent, well-structured PRDs that align with product development standards.

## When to Use

- User explicitly asks for a PRD
- User wants to document product requirements
- User needs to formalize a product idea into a structured document
- User mentions "product requirements", "PRD", or "spec"

## PRD Structure

### 1. Header Section

```
🚧 Draft | ✅ Approved | 🔄 In Review
LAST UPDATED: [Date]

[PRD Title]
[One-line description of initiative for quick context]
```

### 2. Governance Table (RACI)

| ROLE | NAMES | REVIEW STATUS |
|------|-------|---------------|
| RESPONSIBLE (Drive decision process) | PM (Primary Owner): [Name], Design: [Name], Eng: [Name] | Not started |
| ACCOUNTABLE (Ultimate decision authority) | [Name] | Not started |
| CONSULTED (Contribute input) | [Names] | Not started |
| INFORMED | [Names] | Not started |

### 3. Background & Current State

- Current state experience with pain points
- Industry data and competitive landscape
- Link to recordings, Figma files, or other references

### 4. Problem Statements (Customer Problem Framework)

Use the problem statement framework:

**Customer Problem:**
```
I am… [narrow description of customer]
I am trying to… [desired outcome]
But… [problem or barrier]
Because… [root cause]
Which makes me feel… [emotion]
```

**Business Problem:**
```
I am… [business unit/team]
I am trying to… [business goal]
But… [challenge]
Because… [root cause]
Which makes me feel… [impact]
```

### 5. Ideal State

```
In a perfect world: [Vision of solved problem]
The biggest benefit to me is: [Primary value proposition]
Which makes me feel: [Emotional outcome]
```

### 6. Business Goals and Success Metrics

| GOAL/METRIC | DESCRIPTION | TARGET |
|-------------|-------------|--------|
| [Metric name] | [Brief description] | [Target value] |

### 7. Key Features

High-level explanation of feature areas (3-6 features):
- Feature 1: [Description]
- Feature 2: [Description]
- Feature 3: [Description]

### 8. Use Cases & Functional Requirements

| ID | PRIORITY | PERSONA | USE CASE | ACCEPTANCE CRITERIA |
|----|----------|---------|----------|---------------------|
| 1.1 | P0/P1/P2 | [Persona] | [As a user, I want...] | [Criteria for completion] |

Priority levels:
- **P0**: Must have for launch
- **P1**: Important, should have
- **P2**: Nice to have

### 9. Non-Functional Requirements

- **Performance Requirements**: Latency, throughput, scalability
- **Security Requirements**: Auth, encryption, compliance
- **Legal Requirements**: Disclaimers, regulatory compliance
- **Internationalization**: Language, locale support
- **Reliability**: Uptime SLA, failover

### 10. Insights and Problem Validation

- **Market Research**: SWOT analysis, competitive UI analysis
- **Customer Insights**: Research findings, survey data, customer feedback, app reviews
- Include supporting quotes when available

### 11. Milestones and Releases

| MILESTONE | TARGET DATE | DESCRIPTION |
|-----------|-------------|-------------|
| Alpha | [Date] | [Scope] |
| Beta | [Date] | [Scope] |
| GA | [Date] | [Scope] |

### 12. Open Questions and Decisions

| TYPE | DESCRIPTION | PERSON RESPONSIBLE | STATUS | DATE TO CLOSE |
|------|-------------|---------------------|--------|---------------|
| Question/Decision | [Description] | [Name] | Not started/Decided | [Date] |

### 13. Appendix

| RELATED ARTIFACTS | DESCRIPTION | LINKS |
|-------------------|-------------|-------|
| Related PRD | Connected workstream PRDs | [Link] |
| Figma | E2E journeys, wireframes, designs | [Link] |
| Research | Research plans and insights | [Link] |

## Workflow

### Step 1: Gather Information

Ask clarifying questions (one at a time):
1. What is the product/feature being defined?
2. Who is the target user/persona?
3. What problem does it solve?
4. What are the key success metrics?
5. What are the main features?
6. Any constraints or dependencies?

### Step 2: Draft PRD

Create PRD in sections, validating each:
1. Header and governance
2. Problem statements
3. Goals and features
4. Use cases and requirements
5. Milestones and appendix

### Step 3: Output Options

- **Google Doc**: Use `create_document` and `write_document` tools
- **Local Markdown**: Write to project directory
- **Both**: Create local source of truth + shareable Google Doc

## Best Practices

- **Be specific**: Avoid vague requirements; include measurable criteria
- **Use personas**: Reference specific user personas consistently
- **Prioritize ruthlessly**: Not everything is P0
- **Include rationale**: Explain "why" not just "what"
- **Link evidence**: Reference research, data, and prior art
- **Keep it current**: Update last modified date with each change

## Agentic PRD Extensions

For AI-powered products, include additional sections:

- **Agent Classification**: Type, autonomy level, interaction mode
- **AI Trust Profile**: Data sensitivity, decision risk, reversibility
- **AI Leverage Points**: Where AI adds unique value
- **Guardrails & Safety**: Ethical bounds, fallbacks, human escalation
- **Eval Framework**: How to measure AI performance

See `references/agentic-prd-template.md` for the full agentic PRD template.

## Reference Templates

| Template | Use Case |
|----------|----------|
| `references/prd-template.md` | Standard PRD with governance, problem statements, requirements |
| `references/agentic-prd-template.md` | Extended template for AI/agent products with evals, guardrails, trust |

## Quick Reference

| Section | Purpose | Key Content |
|---------|---------|-------------|
| Governance | Who decides | Who decides, approves, reviews |
| Problem Statement | Why | Customer and business pain points |
| Ideal State | Vision | Perfect world outcome |
| Goals/Metrics | Success | Measurable targets |
| Use Cases | What | Functional requirements |
| NFRs | How | Performance, security, reliability |
| Milestones | When | Timeline and phases |
