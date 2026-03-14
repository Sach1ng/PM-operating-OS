# PM Operating System — Self-Serve Onboarding

Welcome! This guide helps you customize the PM-OS for your role, team, and tools. Your answers **restructure which files get created** and **how they're configured**.

---

## How it works

1. **Tell it about you** — Your role, product, goals, and domain context. This is where PM-OS gets its power.
2. **Customize the knowledge layer** — Edit files in `knowledge/` to match your product, personas, and strategy.
3. **Connect tools (optional)** — Hook up Slack and Google Drive MCPs for agents that pull live data.
4. **Run the setup script** — `./scripts/setup.sh --copy` generates your personalized rules, agents, skills, and deploys them.
5. **Restart Cursor** — Changes load from `~/.cursor/`.

Run the onboarding agent in Cursor (say **"onboard"** or **"PM-OS setup"**) for interactive Q&A, or edit `config/pm-os-config.yaml` manually using the questions below.

---

## What you get

PM-OS is structured as an operating system with four layers:

| Layer | What it is | Folder |
|-------|------------|--------|
| **Knowledge (kernel)** | Strategy and domain context that every skill and agent draws from | `knowledge/` |
| **Rules (system services)** | Always-on guidance — strategic framing, domain awareness | `templates/rules/` → `output/rules/` |
| **Skills (applications)** | On-demand PM capabilities — PRDs, launch posts, experiments | `skills/` |
| **Agents (daemons)** | Specialized assistants — VOC analysis, exec updates, strategy review | `templates/agents/` → `output/agents/` |

---

## Part 1: Identity & Role

> **Start here.** Your identity and domain context are what make PM-OS useful. Everything else is optional.

### Q1. What's your role and product focus?

| Question | Your answer | What it affects |
|----------|-------------|-----------------|
| **Role title** (e.g., Principal PM, Senior PM, Group PM) | | Chief-of-staff rule, domain context rule |
| **Product/initiative name** (e.g., Payments, Marketplace, Analytics) | | Rules, skills, agent context, knowledge layer |
| **Product type** (0-1 / growth / platform / other) | | Prioritization framing in rules |
| **Company/org** (e.g., Acme Corp, your startup name) | | PRD template choice, org references |

**Example:** `Principal PM | Payments Platform | 0-1 product | Acme Corp`

---

### Q2. Who do you report to, and who are your key stakeholders?

| Question | Your answer | What it affects |
|----------|-------------|-----------------|
| **Direct manager(s)** — names or Slack handles | | VIP auto-escalation in agents, prioritization |
| **Other VIP senders** (always prioritize their messages) | | Action-item prioritizer, weekly planner |
| **Org structure** (one line: e.g., "I report to Sarah, VP of Product") | | Chief-of-staff rule, exec-update-generator |

**Example:** `Sarah (sparker), Mike | Sarah, Mike | I report to Sarah, VP of Product`

---

## Part 2: Goals & Prioritization

### Q3. What are your top 2–3 strategic goals this quarter?

For each goal, provide: **name**, **metric**, **focus area**.

| Goal | Name | Metric | Focus |
|------|------|--------|-------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

**Example:**
- Goal 1: Self-serve onboarding — 45K signups — acquisition, pipeline, conversion
- Goal 2: Enterprise launch — 500 paying customers — experiments, retention, activation

These goals are used by: action-item-prioritizer, strategy-connector, exec-update-generator, domain-context rule.

---

### Q4. What should be deprioritized or skipped?

| Question | Your answer | What it affects |
|----------|-------------|-----------------|
| **Low-priority areas** (push to backlog) | | Action prioritizer, weekly planner |
| **Things to never prioritize** (delegate or ignore) | | Chief-of-staff rule, domain context rule |

**Example:** `Internal process docs, meetings without goal link`

---

## Part 3: Domain Context

> **This is the most impactful part of onboarding.** The more context you provide here, the better every skill and agent performs.

### Q5. What's your product domain?

You can either **fill in the fields below** or **provide a strategy doc URL** and the onboarding agent will extract the context for you.

| Question | Your answer | What it affects |
|----------|-------------|-----------------|
| **Domain name** (e.g., Payments, Marketplace) | | Rule title, knowledge folder |
| **Customer segments** (who you serve) | | Domain context rule, PRDs, experiments |
| **Key metrics** (how you measure success) | | Domain context rule, exec updates, prioritization |
| **Competitors** (competitive landscape) | | Domain context rule, strategy reviews |
| **Strategic pillars** (your team's strategic bets) | | Domain context rule, strategy connector |
| **Product principles** (how you make decisions) | | Domain context rule, PRDs |

**Example (SaaS Payments):**
- Domain: Payments Platform
- Segments: SMBs, Mid-market, Enterprise
- Metrics: GMV, Take Rate, NPS, Churn, Activation Rate
- Competitors: Stripe, Square, Adyen, PayPal
- Pillars: Self-serve onboarding, Enterprise expansion, Developer experience
- Principles: API-first, Reliability > Features, Customer-obsessed

**Option B: Provide a strategy doc**

If you have a strategy doc (Google Doc, wiki, markdown), provide the URL in `domain.strategy_doc_url` in the config. The onboarding agent will read it and populate the domain fields automatically.

### Q5b. Customize the knowledge layer (optional)

The `knowledge/` directory holds strategy and domain docs that agents and rules reference. Create a folder for your domain (e.g., `knowledge/my-product/`) with any of these:

| File | What to include |
|------|-----------------|
| `strategy.md` | Strategic pillars, multi-phase approach, quarterly priorities |
| `customer-segments.md` | Who you serve, personas, pain points |
| `competitive-landscape.md` | Competitors, positioning, differentiation |
| `value-proposition.md` | Target value prop, product design principles |
| `metrics-and-targets.md` | Key metrics, definitions, financial targets |
| `key-learnings.md` | Recent experiment results, learnings, focus shifts |

**Tip:** Start with `strategy.md` and `customer-segments.md` — these have the biggest impact on skill quality. Update quarterly.

---

## Part 4: Tools & Integrations (optional)

> **All 15+ skills work without any integrations.** This section is only needed if you want agents that pull live data from your tools.

### Q6. Which MCPs do you want to connect?

MCPs (Model Context Protocol servers) connect Cursor to external tools. Each user connects **their own** accounts — no shared credentials, no API keys to manage. Pick the ones you want:

| # | MCP | What it unlocks | Agents enabled |
|---|-----|-----------------|----------------|
| 1 | **Slack** | Search channels, send messages | VOC analyzer, weekly planner, exec-update-generator |
| 2 | **Google Drive** | Read/write Google Docs and Sheets | Weekly planner, exec-update-generator |
| 3 | **Jira** | Read/write tickets, track sprints | Jira-aware agents |
| 4 | **Figma** | Read designs, design-to-code | Design workflows |
| 5 | **Databricks** | Query data, run notebooks | Data analysis agents |

**Choose by number** (e.g., "1, 2" or "all" or "none").

---

### Setup for each selected MCP

Once you've picked your MCPs, follow the setup steps below for each one you selected.

#### If you selected Slack (1):

**Setup:**
1. Open Cursor → **Settings → MCP** (or **Features → MCP**)
2. Add the Slack MCP server and authorize with your Slack workspace
3. Verify: in Cursor chat, ask "search Slack for recent messages" — if it works, you're set

**Configuration:**

| Question | Your answer | What it affects |
|----------|-------------|-----------------|
| **VOC / feedback channel** (e.g., #product-feedback) | | VOC analyzer agent — which channel to search |
| **Slack DM recipient** for daily plans (user ID or handle) | | Weekly planner — where to send plans |
| **Channel ID** (optional; if known) | | VOC agent query |

**Example:** `#product-feedback | W012WHKRA4C | C02A5A7D9U5`

#### If you selected Google Drive (2):

**Setup:**
1. Open Cursor → **Settings → MCP**
2. Add the Google Drive MCP server and authorize with your Google account
3. Verify: in Cursor chat, ask "list my recent Google Docs" — if it works, you're set

**Configuration:**

| Question | Your answer | What it affects |
|----------|-------------|-----------------|
| **Monday Planning doc ID** (weekly goals) | | Weekly planner — reads goals |
| **Daily Standup doc ID** (append plans) | | Weekly planner — reads/writes |
| **PMO / status sheet URL** (optional) | | Weekly planner — project status |

#### If you selected Jira (3):

**Setup:**
1. Open Cursor → **Settings → MCP**
2. Add the Jira MCP server and authorize with your Jira/Atlassian account
3. Verify: in Cursor chat, ask "list my Jira tickets" — if it works, you're set

No additional configuration needed.

#### If you selected Figma (4):

**Setup:**
1. Open Cursor → **Settings → MCP**
2. Add the Figma MCP server and authorize with your Figma account
3. Verify: in Cursor chat, share a Figma URL and ask "describe this design" — if it works, you're set

No additional configuration needed.

#### If you selected Databricks (5):

**Setup:**
1. Open Cursor → **Settings → MCP**
2. Add the Databricks MCP server and connect to your workspace
3. Verify: in Cursor chat, ask "list my Databricks notebooks" — if it works, you're set

No additional configuration needed.

---

## Part 5: Skills & Agents

### Q9. Which skills do you want?

#### Core PM skills

| Skill | Include? (Y/N) | What it does |
|-------|-----------------|--------------|
| **prd-writer** | | PRD creation with governance framework |
| **working-backwards** | | PR/FAQ, press release, customer-first planning |
| **brainstorming** | | Structured ideation — turn vague ideas into concrete plans |
| **writing-clearly** | | Clear, concise writing for all PM artifacts |
| **pptx-creator** | | Professional PowerPoint creation |
| **action-item-prioritizer** | | Prioritize tasks against strategic goals |

#### Strategy & planning skills

| Skill | Include? (Y/N) | What it does |
|-------|-----------------|--------------|
| **strategy-connector** | | Map any work to OKRs and strategy pillars |
| **experiment-designer** | | Hypothesis → experiment design → recipes → decision criteria |

#### Shipping & communication skills

| Skill | Include? (Y/N) | What it does |
|-------|-----------------|--------------|
| **launch-post** | | Slack-native launch announcements |
| **launch-readiness** | | Launch checklists and go/no-go recommendations |
| **exec-communicator** | | Executive updates, escalations, decision requests (BLUF format) |
| **stakeholder-update** | | Concise status updates for leadership |
| **one-pager** | | Feature one-pagers — lighter than a PRD, quick alignment |

#### Learning & operating skills

| Skill | Include? (Y/N) | What it does |
|-------|-----------------|--------------|
| **experiment-writeup** | | Structured experiment results — hypothesis, results, decision |
| **meeting-to-actions** | | Turn meeting notes into prioritized action items |

---

### Q10. Which agents do you want?

| Agent | Include? (Y/N) | Requirements |
|-------|-----------------|--------------|
| **voc-analyzer** | | Slack MCP, VOC channel access |
| **weekly-planner** | | Google Drive MCP, Slack MCP, planning docs |
| **strategy-reviewer** | | Reviews any artifact for strategic alignment (scorecard) |
| **exec-update-generator** | | Slack + Drive MCP (optional) |

---

### Q11. PRD template preference

| Option | When to use |
|--------|-------------|
| **Generic** | Standard PRD structure for any company |

---

## Summary: What gets created

Based on your answers, the setup script generates and deploys:

### Rules (always-on guidance)

| Output | What it does |
|--------|--------------|
| `rules/chief-of-staff.mdc` | Personalized strategic framing — role, org, prioritization |
| `rules/domain-context.mdc` | Always-on domain awareness — personas, metrics, goals, competitive context |

### Agents (specialized assistants)

| Output | What it does | Requires |
|--------|--------------|----------|
| `agents/voc-analyzer.md` | VOC analysis from Slack feedback channels | Slack MCP |
| `agents/weekly-planner.md` | Daily/weekly planning from Google Docs + Slack | Slack + Drive MCP |
| `agents/strategy-reviewer.md` | Reviews PRDs, one-pagers, specs for strategic fit | — |
| `agents/exec-update-generator.md` | Auto-generates leadership status updates | Slack + Drive MCP (optional) |

### Skills (on-demand PM capabilities)

| Workflow | Skills deployed |
|----------|----------------|
| **Planning** | strategy-connector, working-backwards |
| **Building** | prd-writer, one-pager, experiment-designer |
| **Shipping** | launch-readiness, launch-post |
| **Communicating** | exec-communicator, stakeholder-update |
| **Learning** | experiment-writeup |
| **Operating** | meeting-to-actions, action-item-prioritizer |
| **Foundation** | brainstorming, writing-clearly, pptx-creator |

---

## Next steps

1. **Fill config** — Run the onboarding agent in Cursor ("onboard" or "PM-OS setup") for Q&A; it writes config and runs setup automatically. Or edit `config/pm-os-config.yaml` and run `./scripts/setup.sh --copy`.
2. **Customize knowledge** — Edit the files in `knowledge/` to match your product and strategy.
3. **Restart Cursor** to pick up changes.

Need help? See [README.md](README.md) for manual setup and structure details.
