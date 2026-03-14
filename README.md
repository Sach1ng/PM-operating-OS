# PM Operating System

A context graph for product teams — rules, skills, agents, and memory that adapt to your role, goals, and tools. Built on Cursor IDE.

**Created by [@Sach1ng](https://github.com/Sach1ng) and [@hardiktiwari](https://github.com/hardiktiwari)**

---

## Quick start (self-serve onboarding)

1. **Clone this repo**
   ```bash
   git clone https://github.com/Sach1ng/PM-operating-OS.git
   cd PM-operating-OS
   ```

2. **Run onboarding** — Open the repo in Cursor, then in chat say: **"onboard"** or **"PM-OS setup"**. Answer the questions; the agent writes config and runs setup automatically.
   - *Or* manually edit `config/pm-os-config.yaml` and run `./scripts/setup.sh --copy`

3. **Restart Cursor** — Rules, skills, and agents will load from `~/.cursor/`.

---

## What's included

| Type | What it is | How it's customized |
|------|------------|---------------------|
| **Rules** | Persistent guidance Cursor applies | Your product, role, org, deprioritization signals |
| **Skills** | On-demand PM capabilities | Goals, VIPs, PRD template, expanded PM workflows |
| **Agents** | Specialized assistants (VOC, planning, strategy review, exec updates, retrospective) | Slack channel, Google docs, goals |
| **Knowledge layer** | Strategy and domain context (personas, metrics, competitive landscape) | Customize in `knowledge/` |
| **Memory** | Trajectory store — accumulated agent outputs, decision traces, knowledge snapshots | Builds automatically as you use agents |

---

## Structure (after onboarding)

| Folder | Purpose |
|--------|---------|
| **.cursor/agents/** | Project-local onboarding agent (loaded when repo is open) |
| **config/** | Your answers → `pm-os-config.yaml` |
| **templates/** | Jinja2 templates for rules, agents, skills |
| **scripts/** | `setup.sh` / `setup.py` — generates personalized files |
| **output/** | Generated rules, agents, skills (gitignored) |
| **skills/** | Source for prd-writer, working-backwards, and expanded PM skills |
| **knowledge/** | Strategy docs (personas, metrics, competitive landscape) — used by agents and rules |
| **memory/** | Context graph trajectory store — decision traces, agent outputs, knowledge snapshots |
| **agents/** | Agent docs (see agents/README.md) |

---

## Rules, skills, and agents — what's the difference?

| | What it is | In plain terms |
|---|------------|----------------|
| **Rules** | Persistent guidance Cursor applies | How *you* work: standards, org context, prioritization |
| **Skills** | On-demand "how-to" Cursor uses when the task fits | PM capabilities: PRDs, working backwards, prioritization |
| **Agents** | Specialized assistants Cursor delegates to | Concrete tasks: VOC analysis, daily planning, strategy review |

---

## PM Workflows

| Workflow | Skills |
|----------|--------|
| **Planning** | strategy-connector, working-backwards |
| **Building** | prd-writer, one-pager, experiment-designer |
| **Shipping** | launch-readiness, launch-post |
| **Communicating** | exec-communicator, stakeholder-update |
| **Learning** | experiment-writeup, voc-analyzer |
| **Operating** | weekly-planner, meeting-to-actions, action-item-prioritizer |
| **Context graph** | decision-logger, what-if, knowledge-updater, retrospective |

---

## Knowledge Layer

The `knowledge/` directory holds strategy and domain context that agents and rules reference:

- **_template/** — Copy this folder and rename it for your domain (e.g., `my-product/`)
- **examples/** — Fully worked-out examples using public investor data from **Spotify, Netflix, Shopify, and Uber** (SEC 10-Ks, earnings calls, investor presentations)

**How to customize:** Edit the markdown files in `knowledge/` to reflect your product, team, and current strategy. Browse `knowledge/examples/` to see how real companies' strategy, segments, and metrics map to the template. The strategy-reviewer agent and domain context rule use this context automatically.

---

## Context Graph — Memory Layer

PM OS includes a **memory layer** that turns it from a static configuration system into a context graph where reasoning accumulates over time. Inspired by [context graph infrastructure](https://www.linkedin.com/pulse/how-do-you-build-context-graph-jaya-gupta-xicwe/) — the idea that the next wave of AI won't just store data, it will capture the *reasoning* that connects data to decisions.

### How it works

Every agent **reads from memory before starting** (what happened last time, what trends are emerging) and **writes to memory after completing** (structured summary of findings). This creates three capabilities:

| Capability | What it does | How |
|------------|-------------|-----|
| **Temporal awareness** | Agents know what happened before | VOC in March knows what February found; weekly planner knows what got done vs. dropped |
| **Cross-agent context** | Agents read each other's outputs | Exec update pulls from VOC, plans, decisions, and reviews — no manual stitching |
| **Compounding intelligence** | Context gets richer over time | More runs → better trend detection, drift analysis, and simulation grounding |

### Memory structure

```
memory/
├── decisions/            # Decision traces — the "why" behind key calls
├── voc/                  # VOC analyzer outputs over time
├── weekly-plans/         # Weekly planner outputs
├── strategy-reviews/     # Strategy reviewer scorecards
├── exec-updates/         # Executive status updates
└── knowledge-snapshots/  # Versioned snapshots for drift detection
```

### Context graph skills and agents

| Name | Type | What it does |
|------|------|-------------|
| **decision-logger** | Skill | Captures structured decision traces after key PM moments (PRD approvals, scope changes, launch/kill calls) |
| **what-if** | Skill | Simulates impact of proposed decisions using accumulated context — strategy, past decisions, VOC, execution history |
| **knowledge-updater** | Skill | Updates knowledge docs with automatic snapshotting for drift detection |
| **retrospective** | Agent | Reads across all memory to surface patterns, strategy drift, execution velocity, and blind spots |

### Getting started with memory

Memory builds automatically as you use PM OS agents. To accelerate:

1. **Log a few key decisions** — Say *"log this decision"* after your next prioritization call or PRD approval
2. **Run VOC analysis** — Each run saves to memory, building a trend baseline
3. **Plan your week** — Weekly plans accumulate, creating an execution history
4. **Run a retrospective** — Say *"retrospective"* once you have 5+ memory entries to see patterns emerge

---

## Manual setup (without the script)

If you prefer not to run the setup script:

- Edit `config/pm-os-config.yaml` with your answers
- Copy `skills/` subfolders to `~/.cursor/skills/`
- Edit templates in `templates/` and copy outputs to `~/.cursor/` (rules, agents)

---

## Requirements

**Required:**
- **Cursor IDE** with MCP support
- **Python 3** (for setup script; `pip install -r requirements.txt`)

**Optional (for agents that connect to external tools):**
- **Slack, Google Drive, GitHub, Figma** — Setup auto-generates `.cursor/mcp.json` for these. You just add your API keys. See [MCP_SETUP.md](MCP_SETUP.md).
- **Jira, Linear, Notion, etc.** — Add via Cursor Settings → Tools & MCP (one-click from Marketplace).

> **15+ skills work immediately without any MCP.** Setup generates MCP config for you — you only need to add your keys. See [MCP_SETUP.md](MCP_SETUP.md).

---

## VOC Analyzer (Slack feedback)

If you enabled the VOC analyzer:

1. Configure **Slack MCP** in Cursor (Settings → MCP) with access to your VOC channel.
2. In Cursor chat, say: *"Analyze VOC"*, *"Slack VOC analysis"*, or *"Customer feedback"*.
3. The agent searches your configured channel, classifies feedback by theme, and returns a PM report.

See [agents/README.md](agents/README.md) for details.

---

## Authors

| | GitHub | Role |
|---|---|---|
| **Sachin** | [@Sach1ng](https://github.com/Sach1ng) | Co-creator |
| **Hardik** | [@hardiktiwari](https://github.com/hardiktiwari) | Co-creator |

## Contributing

To add a new skill, create a folder in `skills/` with a `SKILL.md` following the existing format.

---

## Disclaimer

*This is a personal project and is not affiliated with, endorsed by, or representative of any employer.*

## License

MIT — see [LICENSE](LICENSE) for details.
