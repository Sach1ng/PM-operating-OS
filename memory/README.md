# Memory — PM OS Context Graph

This directory is the **event clock** and **trajectory store** for your PM context graph. It captures the reasoning, decisions, and agent outputs that accumulate over time — turning PM OS from a static configuration system into infrastructure where context compounds.

## Structure

```
memory/
├── decisions/          # Decision traces — the "why" behind key calls
├── feedback/           # Feedback analyzer outputs over time
├── weekly-plans/       # Weekly planner outputs
├── strategy-reviews/   # Strategy reviewer scorecards
├── exec-updates/       # Executive status updates
└── knowledge-snapshots/# Versioned snapshots of knowledge/ for drift detection
```

## How It Works

**Agents write here after every run.** Each agent saves a structured summary so future runs can reference past context. This creates temporal awareness — the feedback analyzer in March knows what February found, and the weekly planner knows what last week's plan was.

**Agents read here before every run.** Each agent checks its own history and relevant cross-agent memory to spot trends, track progress, and avoid starting from scratch.

**Cross-agent references create the graph.** The weekly planner reads from feedback and decisions. The exec update generator reads from everything. The retrospective agent walks across all memory to surface patterns and drift.

## Conventions

- **Filenames**: `YYYY-MM-DD_short-description.md` for decisions, `YYYY-MM-DD.md` for periodic outputs, `YYYY-Wxx.md` for weekly plans
- **Append-only**: Never delete or overwrite entries. Memory is a log, not a cache.
- **Structured format**: Each entry follows a consistent markdown template so agents can parse reliably.
- **Git-tracked**: Memory entries are committed to the repo. This *is* the context graph — it should travel with the project.

## What This Enables

Once enough memory accumulates, PM OS can:
- **Trend** — Feedback themes shifting quarter over quarter
- **Recall** — "What did we decide about pricing in Q1?"
- **Detect drift** — Strategy says X, but last 5 decisions moved toward Y
- **Simulate** — "If we deprioritize mobile, what breaks?" (grounded in actual context)
