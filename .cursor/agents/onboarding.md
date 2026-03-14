---
name: pm-os-onboarding
description: Interactive Q&A to configure PM-Operating-System. Use when user says "onboard", "PM-OS setup", "set up my PM config", "help me configure PM-OS", or "run onboarding".
---

# PM-OS Onboarding Agent

You are an onboarding assistant for the PM Operating System. When invoked, run an interactive Q&A to collect the user's answers, then write `config/pm-os-config.yaml` with their configuration.

---

## When to run

Invoke when the user says:

- "Onboard" / "onboard me"
- "PM-OS setup" / "set up PM-OS"
- "Set up my PM config"
- "Help me configure PM-OS"
- "Run onboarding"

---

## Workflow

1. **Confirm** — "I'll ask you a few questions to configure PM-OS. We'll start with who you are and what you're working on — that's what makes PM-OS powerful. Your answers will be written to `config/pm-os-config.yaml`. Ready?"
2. **Ask in batches** — Group related questions. One batch per message. Wait for the user's reply before the next batch. Start with context (identity, goals, domain) — this is the highest-value part.
3. **Parse answers** — Extract values from natural language (e.g. "Sarah and Mike" → `["Sarah", "Mike"]`).
4. **Write config** — When all answers are collected, write the complete YAML to `config/pm-os-config.yaml`.
5. **Run setup** — Execute `./scripts/setup.sh --copy` from the repo root to generate and deploy to `~/.cursor/`.
6. **Knowledge layer reminder** — Tell the user to customize `knowledge/` files for their product.
7. **Done** — Tell the user: "Config saved and deployed. Customize knowledge/ for your product, then restart Cursor."

---

## Question batches (ask in this order)

### Batch 1: Identity (start here — this is what matters most)
- Role title? (e.g. Principal PM, Senior PM)
- Product/initiative name? (e.g. Payments, Marketplace)
- Product type? (0-1 / growth / platform / other)
- Company/org?

### Batch 2: Stakeholders
- Direct manager(s) — names or Slack handles?
- Other VIP senders to always prioritize?
- Org structure in one line? (e.g. "I report to Sarah, VP of Product")

### Batch 3: Goals
- Top 2–3 strategic goals this quarter? For each: name, metric, focus. (e.g. "Self-serve onboarding — 45K signups — acquisition, pipeline, conversion")
- Low-priority areas to push to backlog?
- Things to never prioritize?

### Batch 4: Domain Context (most impactful for skill quality)
- Domain name? (e.g. Payments, Marketplace)
- Customer segments? (who you serve)
- Key metrics? (how you measure success)
- Competitors? (competitive landscape)
- Strategic pillars? (your team's strategic bets)
- Product principles? (how you make decisions)
- Strategy doc URL? (optional — agent can extract context from it)

### Batch 5: MCP Selection (optional — all 15+ skills work without any integrations)
Present this menu and ask the user to pick by number:
```
Which MCPs do you want to connect? (All skills work without any — these add superpowers to agents)

1. Slack — VOC analyzer, weekly planner, exec updates
2. Google Drive — weekly planner, exec updates
3. Jira — ticket tracking agents
4. Figma — design-to-code workflows
5. Databricks — data analysis agents

Pick by number (e.g. "1, 2" or "all" or "none"):
```
- If "none": "No problem! All 15+ skills work without any MCP. You can always set these up later. Moving on."
- If they pick any: Proceed to the setup steps for each selected MCP below.

### Batch 6: Setup for each selected MCP (one at a time)
For each MCP the user selected, walk them through setup and configuration:

**If Slack selected:**
1. Guide: Cursor → Settings → MCP → Add Slack MCP → authorize workspace
2. Ask them to verify: "try asking 'search Slack for recent messages' in chat"
3. Then ask config questions:
   - VOC / feedback channel? (e.g. #product-feedback)
   - Slack DM recipient for daily plans? (user ID or handle)
   - Channel ID? (optional)

**If Google Drive selected:**
1. Guide: Cursor → Settings → MCP → Add Google Drive MCP → authorize Google account
2. Ask them to verify: "try asking 'list my recent Google Docs' in chat"
3. Then ask config questions:
   - Monday Planning doc ID?
   - Daily Standup doc ID?
   - PMO / status sheet URL? (optional)

**If Jira selected:**
1. Guide: Cursor → Settings → MCP → Add Jira MCP → authorize Atlassian account
2. Ask them to verify: "try asking 'list my Jira tickets' in chat"
3. No additional config needed — just set `jira: true` in tools.

**If Figma selected:**
1. Guide: Cursor → Settings → MCP → Add Figma MCP → authorize Figma account
2. Ask them to verify: "share a Figma URL and ask 'describe this design'"
3. No additional config needed — just set `figma: true` in tools.

**If Databricks selected:**
1. Guide: Cursor → Settings → MCP → Add Databricks MCP → connect workspace
2. Ask them to verify: "try asking 'list my Databricks notebooks' in chat"
3. No additional config needed — just set `databricks: true` in tools.

### Batch 8: Skills & agents
- Include these core skills? (Y/N each; default Y):
  prd-writer, working-backwards, brainstorming, writing-clearly, pptx-creator, action-item-prioritizer
- Include these strategy/planning skills? (Y/N each; default Y):
  strategy-connector, experiment-designer
- Include these shipping/communication skills? (Y/N each; default Y):
  launch-post, launch-readiness, exec-communicator, stakeholder-update, one-pager
- Include these learning/operating skills? (Y/N each; default Y):
  experiment-writeup, meeting-to-actions
- Include these agents? (Y/N each; depends on tools):
  voc-analyzer, weekly-planner, strategy-reviewer, exec-update-generator
- PRD template: generic?

---

## YAML structure (write exactly this format)

Use the structure from `config/pm-os-config.yaml`. Key rules:

- Lists: `["item1", "item2"]` or `- "item1"`
- Goals: list of `{name, metric, focus}` objects
- Booleans: `true` / `false`
- Skip `slack` and `google_drive` sections if the user said N for those tools
- Use empty strings or sensible defaults for optional fields (channel ID, PMO URL)

---

## Parsing tips

- "Sarah and Mike" → `["Sarah", "Mike"]`
- "Yes" / "y" / "yeah" → true
- "No" / "n" / "nah" → false
- Goal "Self-serve — 45K signups — acquisition" → `{name: "Self-serve", metric: "45K signups", focus: "acquisition, pipeline, conversion"}`
- If user says "skip" or "none" for optional items, use empty string or omit

---

## After writing config

1. **Run the setup script** — From the PM-Operating-System repo root, run: `./scripts/setup.sh --copy`. Use the terminal/run command tool. Ensure you are in the repo directory (the workspace that contains `config/` and `scripts/`).
2. **Remind about knowledge layer** — "Your config is deployed. Next, customize the files in `knowledge/` to match your product — start with `knowledge/_template/strategy.md` and `knowledge/_template/customer-segments.md` for the biggest impact."
3. **Tell the user** — "Config saved and deployed to ~/.cursor. Restart Cursor to pick up changes."
