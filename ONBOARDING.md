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

### What are MCPs?

MCPs (Model Context Protocol servers) are plugins that connect Cursor to external tools. **PM-OS does not include any MCPs** — you install and authorize each one yourself in Cursor settings. Think of them like browser extensions: you pick the ones you need, connect your own accounts, and Cursor's agents can then read/write data from those tools.

**How to install any MCP:**
1. Open Cursor → **Settings → MCP** (or **Features → MCP**)
2. Browse or search for the MCP server you want
3. Add it and authorize with your account
4. Verify it works by asking Cursor a test question

### Q6. Which MCPs do you want to connect?

Pick the ones relevant to your workflow. You can always add more later.

#### Communication & Collaboration

| # | MCP | What it does | PM use case |
|---|-----|-------------|-------------|
| 1 | **Slack** | Search channels, send messages, read threads | VOC analysis, weekly planning, exec updates |
| 2 | **Gmail / Email** | Read and draft emails | Stakeholder communication, follow-ups |
| 3 | **Microsoft Teams** | Search chats and channels | VOC analysis, team communication (Teams-based orgs) |

#### Documents & Knowledge

| # | MCP | What it does | PM use case |
|---|-----|-------------|-------------|
| 4 | **Google Drive** | Read/write Docs, Sheets, Slides | Weekly planning, exec updates, PRD collaboration |
| 5 | **Notion** | Read/write pages and databases | PRDs, wikis, meeting notes, roadmaps |
| 6 | **Confluence** | Read/write wiki pages | Enterprise documentation, specs, decision logs |

#### Project Management

| # | MCP | What it does | PM use case |
|---|-----|-------------|-------------|
| 7 | **Jira** | Read/write tickets, track sprints | Backlog management, sprint planning, status tracking |
| 8 | **Linear** | Read/write issues, projects, cycles | Issue tracking, roadmap management |
| 9 | **Asana** | Read/write tasks and projects | Task management, cross-functional coordination |
| 10 | **GitHub** | Read/write issues, PRs, repos | Engineering coordination, release tracking |

#### Design

| # | MCP | What it does | PM use case |
|---|-----|-------------|-------------|
| 11 | **Figma** | Read designs, inspect components | Design reviews, spec writing, design-to-requirements |

#### Data & Analytics

| # | MCP | What it does | PM use case |
|---|-----|-------------|-------------|
| 12 | **Databricks** | Query data, run notebooks | Metric deep-dives, experiment analysis |
| 13 | **Snowflake** | Query data warehouse | Metric reporting, ad-hoc analysis |
| 14 | **PostgreSQL / SQL** | Direct database queries | Quick data pulls, validation |
| 15 | **Amplitude** | Read product analytics | Feature adoption, funnel analysis, retention |
| 16 | **Mixpanel** | Read product analytics | Event tracking, user behavior analysis |

#### CRM & Customer

| # | MCP | What it does | PM use case |
|---|-----|-------------|-------------|
| 17 | **Salesforce** | Read CRM data, accounts, opportunities | Customer insights, enterprise deal context |
| 18 | **HubSpot** | Read CRM and marketing data | Lead data, customer lifecycle |
| 19 | **Zendesk** | Read support tickets | Customer pain points, bug reports, VOC |
| 20 | **Intercom** | Read conversations and tickets | Customer feedback, support trends |

**Choose by number** (e.g., "1, 4, 7" or "none"). You can always add more later.

---

### Setup for each selected MCP

For each MCP you selected, follow the same pattern:

1. **Install:** Cursor → Settings → MCP → find and add the MCP server
2. **Authorize:** Connect your account (OAuth, API key, or token — depends on the MCP)
3. **Verify:** Ask Cursor a test question to confirm it works (see examples below)

#### Slack (1) — requires configuration

**Verify:** Ask "search Slack for recent messages"

**Configuration (needed for PM-OS agents):**

| Question | Your answer | What it affects |
|----------|-------------|-----------------|
| **VOC / feedback channel** (e.g., #product-feedback) | | VOC analyzer agent — which channel to search |
| **Slack DM recipient** for daily plans (user ID or handle) | | Weekly planner — where to send plans |
| **Channel ID** (optional; if known) | | VOC agent query |

#### Google Drive (4) — requires configuration

**Verify:** Ask "list my recent Google Docs"

**Configuration (needed for PM-OS agents):**

| Question | Your answer | What it affects |
|----------|-------------|-----------------|
| **Monday Planning doc ID** (weekly goals) | | Weekly planner — reads goals |
| **Daily Standup doc ID** (append plans) | | Weekly planner — reads/writes |
| **PMO / status sheet URL** (optional) | | Weekly planner — project status |

#### All other MCPs — no PM-OS configuration needed

For MCPs 2-3, 5-20: just install and authorize. No additional PM-OS config required — Cursor's agents will automatically use them when relevant. Set the corresponding flag to `true` in `config/pm-os-config.yaml` under `tools:`.

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
