# PRD Template

Standard template for Product Requirements Documents.

## Document Header

```
🚧 Draft | ✅ Approved | 🔄 In Review
LAST UPDATED: [Date]

[PRD Title]
[One-line description of initiative for reader's quick context]
```

## Governance Table (RACI)

PRDs use a RACI governance framework. Review status lets others know when you're done reviewing.

### Guidance on RACI for PRD Approval

**For new products or offerings:**
- Senior PMs or Principal PMs typically own/drive
- With sign-off from all contributors and reviewers, the driver/owner PM will be the approver
- Depending on scope, PM leadership may request the driver's PM leader/manager to act as Approver

**For new features/enhancements for existing products:**
- Staff or Senior PMs typically own/drive
- PM leadership (Group PM/Director/VP) will be the Approver

### RACI Table Format

| ROLE | NAMES | REVIEW STATUS |
|------|-------|---------------|
| **RESPONSIBLE** (Drive decision process with key stakeholders) | PM (Primary Owner): [Name], Design: [Name], Eng: [Name] | Not started |
| **ACCOUNTABLE** (Ultimate decision authority, accountable for outcome) | [Name] - Ideally 1, no more than 2 | Not started |
| **CONSULTED** (Contribute input and perspective) | [Names] | Not started |
| **INFORMED** (Kept updated on progress) | [Names] | Not started |

---

## Section: Background & Current State

Add relevant background context and current state experience. Link to references to help paint the picture:
- Recording of current state
- Figma file
- Competitive analysis
- Industry research

---

## Section: Problem Statements

Customer (or business) problem statements help describe in detail "What is the customer problem?", so teams can align and agree on which problems to solve, and communicate with partners and stakeholders.

### Customer Problem Format

```
I am… [Narrow description of the customer - not you]
I am trying to… [Desired outcome the customer is trying to achieve]
But… [Problem or barrier]
Because… [Root cause of the problem or barrier]
Which makes me feel… [Emotion]
```

### Business Problem Format

```
I am… [Business unit or team description]
I am trying to… [Business goal or objective]
But… [Challenge or blocker]
Because… [Root cause]
Which makes me feel… [Business impact or urgency]
```

---

## Section: Ideal State

The Ideal State describes a future state where an important customer problem or opportunity has been solved to such an amazing degree that the outcome seems almost impossible.

Format:
```
In a perfect world: [Vision statement]
The biggest benefit to me is: [Primary value proposition]
Which makes me feel: [Emotional outcome]
```

---

## Section: Business Goals and Success Metrics

Identify the primary business goals for the project. These will be used to balance the customer problem statements and to develop appropriate metrics and data to measure the success of the project.

Connect to your team's OKRs and quarterly goals.

| GOAL/METRIC | DESCRIPTION | TARGET |
|-------------|-------------|--------|
| [Goal/metric name] | [Brief description of the goal/metric] | [Goal/outcome target for success] |

---

## Section: Key Features

High level explanation of the key features / feature areas that will be addressed.

**Example:** Create parental controls: Allows parents to set usage limits, restrict access to apps and content, and monitor online activity.

---

## Section: Use Cases & Functional Requirements

| ID | PRIORITY | PERSONA | USE CASE | ACCEPTANCE CRITERIA & SCOPE |
|----|----------|---------|----------|----------------------------|
| 1.1 | P0/P1/P2 | [Persona name] | [User story or scenario] | [Specific acceptance criteria] |

**Priority Definitions:**
- **P0**: Must have for launch (blocking)
- **P1**: Should have, important for success
- **P2**: Nice to have, can defer

**Example Row:**
| 1.1 | P0 | Guest Shopper | Guest Shoppers should be able to complete a purchase without creating an account to save time and effort, minimizing friction. | Shoppers must be offered a clear Guest Checkout option. Guests must provide Shipping, Billing, and Payment details. Upon successful payment, redirect to Order Confirmation with unique Order ID. |

---

## Section: Non-Functional Requirements

Non-functional requirements can include latency, volume, etc.

### Security Requirements
[Add any security requirements here.]

### Legal Requirements
[Add any legal requirements here.]

### Internationalization Requirements
[Add any internationalization requirements here.]

### Performance Requirements
[Add latency, throughput, scalability requirements here.]

### Reliability Requirements
[Add uptime SLA, failover, disaster recovery requirements here.]

---

## Section: Insights and Problem Validation

### Market Research (Optional)
Provide clear SWOT analysis of any competitors or players in the market. Include any competitive UI analysis.

### Customer Insights
What do customers say about the problem(s)? Include any customer insights gathered from:
- User research / interviews
- Survey studies
- Customer feedback and surveys
- App reviews
- Support tickets

---

## Section: Milestones and Releases

| MILESTONE | TARGET DATE | DESCRIPTION |
|-----------|-------------|-------------|
| Milestone 1 | [Date] | [Scope and deliverables] |
| Milestone 2 | [Date] | [Scope and deliverables] |
| Milestone 3 | [Date] | [Scope and deliverables] |

---

## Section: Open Questions and Decisions

Use this area to track open questions and decisions made to advance the project. Record the date and decision made.

| TYPE | DESCRIPTION | PERSON RESPONSIBLE | STATUS | DATE TO CLOSE |
|------|-------------|-------------------|--------|---------------|
| Question | [Question description] | [Name] | Not started | [Date] |
| Decision | [Decision description] | [Name] | Decided | [Date] |

---

## Section: Appendix

| RELATED ARTIFACTS | DESCRIPTION | LINKS |
|-------------------|-------------|-------|
| Related PRD | Any PRD connected to the same workstream or goals | [Link] |
| Related docs | 1-pagers, white papers, presentations | [Link] |
| Figma | E2E customer journeys, audits, wireframes, concepts, final design | [Link] |
| Program deck | Design review presentation of E2E application and core edge cases | [Link] |
| Research plan | High-level research plan of core questions, outcomes, and methods | [Link] |
| Research insights | Document for hosting all key insights and feedback | [Link] |
