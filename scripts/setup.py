#!/usr/bin/env python3
"""
PM Operating System — Setup script
Reads config/pm-os-config.yaml and generates personalized rules, agents, and skills.
Also generates .cursor/mcp.json for selected MCPs — users just add their API keys.
"""

import argparse
import json
import os
import shutil
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(PROJECT_ROOT))

try:
    import yaml
    from jinja2 import Environment, FileSystemLoader
except ImportError as e:
    print("Error: Missing dependencies. Run: pip install -r requirements.txt")
    print(f"  {e}")
    sys.exit(1)


def load_config() -> dict:
    config_path = PROJECT_ROOT / "config" / "pm-os-config.yaml"
    if not config_path.exists():
        print(f"Error: Config not found at {config_path}")
        print("  1. Copy config/pm-os-config.yaml if needed")
        print("  2. Fill in your answers from ONBOARDING.md")
        sys.exit(1)
    with open(config_path) as f:
        return yaml.safe_load(f)


def build_template_context(cfg: dict) -> dict:
    """Build a flat context for Jinja2 templates."""
    identity = cfg.get("identity", {})
    stakeholders = cfg.get("stakeholders", {})
    goals = cfg.get("goals", [])
    deprioritize = cfg.get("deprioritize", {})
    slack = cfg.get("slack", {})
    gdrive = cfg.get("google_drive", {})
    domain = cfg.get("domain", {})

    ctx = {
        "product": identity.get("product", "My Product"),
        "role": identity.get("role", "PM"),
        "company": identity.get("company", "My Company"),
        "product_type": identity.get("product_type", "product"),
        "managers": ", ".join(stakeholders.get("managers", [])),
        "org_structure": stakeholders.get("org_structure", ""),
        "deprioritize": deprioritize,
        "deprioritize_flat": deprioritize.get("low_priority", []) + deprioritize.get("never_prioritize", []),
        "goals": goals,
        "vip_senders": stakeholders.get("vip_senders", []),
        "identity": identity,
        "domain": domain,
        "voc_channel": slack.get("voc_channel", "#feedback"),
        "voc_channel_id": slack.get("voc_channel_id", ""),
        "dm_recipient_id": slack.get("dm_recipient_id", ""),
        "monday_planning_doc_id": gdrive.get("monday_planning_doc_id", ""),
        "daily_standup_doc_id": gdrive.get("daily_standup_doc_id", ""),
        "pmo_sheet_url": gdrive.get("pmo_sheet_url", ""),
    }
    return ctx


def render_template(env: Environment, name: str, ctx: dict) -> str:
    template = env.get_template(name)
    return template.render(ctx)


# MCP configs we can auto-generate (official npm packages or URL-based).
# Other MCPs: user adds via Cursor Marketplace one-click.
MCP_CONFIGS = {
    "slack": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-slack"],
        "env": {
            "SLACK_BOT_TOKEN": "YOUR_SLACK_BOT_TOKEN",
            "SLACK_TEAM_ID": "YOUR_SLACK_TEAM_ID",
        },
    },
    "google_drive": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-gdrive"],
        "env": {},
    },
    "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": {"GITHUB_PERSONAL_ACCESS_TOKEN": "YOUR_GITHUB_TOKEN"},
    },
    "figma": {
        "url": "https://mcp.figma.com/mcp",
        "headers": {},
    },
}


def generate_mcp_config(cfg: dict) -> None:
    """Generate .cursor/mcp.json from tools config. Users replace placeholders with real keys."""
    tools = cfg.get("tools", {})
    if not any(tools.get(k) for k in MCP_CONFIGS if k in tools):
        return

    mcp_servers = {}
    for tool_key, enabled in tools.items():
        if not enabled or tool_key not in MCP_CONFIGS:
            continue
        mcp_servers[tool_key] = MCP_CONFIGS[tool_key].copy()
        # Deep copy env to avoid mutating template
        if "env" in mcp_servers[tool_key]:
            mcp_servers[tool_key]["env"] = dict(mcp_servers[tool_key]["env"])

    if not mcp_servers:
        return

    cursor_dir = PROJECT_ROOT / ".cursor"
    cursor_dir.mkdir(exist_ok=True)
    mcp_path = cursor_dir / "mcp.json"
    mcp_path.write_text(json.dumps({"mcpServers": mcp_servers}, indent=2), encoding="utf-8")
    print(f"  Generated .cursor/mcp.json ({len(mcp_servers)} MCPs)")
    print("  → Replace placeholders in .cursor/mcp.json with your API keys. See MCP_SETUP.md")


def main():
    parser = argparse.ArgumentParser(description="PM-OS setup: generate personalized Cursor config")
    parser.add_argument("--copy", action="store_true", help="Copy output to Cursor dir (default)")
    parser.add_argument("--symlink", action="store_true", help="Symlink output to Cursor dir")
    parser.add_argument("--output-only", action="store_true", help="Only generate to output/, don't copy")
    parser.add_argument("--cursor-path", default=None, help="Override Cursor path (e.g. ~/.cursor)")
    args = parser.parse_args()

    cfg = load_config()
    tools = cfg.get("tools", {})
    skills_cfg = cfg.get("skills", {})
    agents_cfg = cfg.get("agents", {})

    if args.output_only:
        mode = "output_only"
    elif args.symlink:
        mode = "symlink"
    else:
        mode = args.copy or (cfg.get("output", {}).get("mode", "copy"))

    cursor_path = Path(args.cursor_path or cfg.get("output", {}).get("cursor_path", "~/.cursor")).expanduser()
    output_dir = PROJECT_ROOT / "output"
    output_dir.mkdir(exist_ok=True)

    for d in ["rules", "agents", "skills"]:
        (output_dir / d).mkdir(exist_ok=True)
        for f in (output_dir / d).iterdir():
            if f.is_file():
                f.unlink()

    env = Environment(
        loader=FileSystemLoader(PROJECT_ROOT / "templates"),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    ctx = build_template_context(cfg)

    # 1. Chief-of-staff rule (always)
    rule_content = render_template(env, "rules/chief-of-staff.mdc.template", ctx)
    rule_name = f"{cfg.get('identity', {}).get('product', 'chief-of-staff').lower().replace(' ', '-')}-chief-of-staff.mdc"
    (output_dir / "rules" / rule_name).write_text(rule_content, encoding="utf-8")
    print(f"  Generated rules/{rule_name}")

    # 1b. Domain context rule (always)
    domain_tpl = "rules/domain-context.mdc.template"
    domain_name = cfg.get("domain", {}).get("name", "") or cfg.get("identity", {}).get("product", "domain")
    domain_rule_filename = f"{domain_name.lower().replace(' ', '-')}-domain-context.mdc"
    domain_rule_content = render_template(env, domain_tpl, ctx)
    (output_dir / "rules" / domain_rule_filename).write_text(domain_rule_content, encoding="utf-8")
    print(f"  Generated rules/{domain_rule_filename}")

    # 2. Onboarding agent (always — for re-runs)
    onboarding_src = PROJECT_ROOT / ".cursor" / "agents" / "onboarding.md"
    if onboarding_src.exists():
        shutil.copy2(onboarding_src, output_dir / "agents" / "onboarding.md")
        print(f"  Copied agents/onboarding.md")

    # 3. VOC analyzer (if Slack + enabled)
    if tools.get("slack") and agents_cfg.get("voc_analyzer"):
        voc_content = render_template(env, "agents/voc-analyzer.md.template", ctx)
        (output_dir / "agents" / "voc-analyzer.md").write_text(voc_content, encoding="utf-8")
        print(f"  Generated agents/voc-analyzer.md")
    else:
        print(f"  Skipped agents/voc-analyzer.md (slack={tools.get('slack')}, voc_analyzer={agents_cfg.get('voc_analyzer')})")

    # 4. Weekly planner (if Google Drive + Slack + enabled)
    if tools.get("slack") and tools.get("google_drive") and agents_cfg.get("weekly_planner"):
        wp_content = render_template(env, "agents/weekly-planner.md.template", ctx)
        (output_dir / "agents" / "weekly-planner.md").write_text(wp_content, encoding="utf-8")
        print(f"  Generated agents/weekly-planner.md")
    else:
        print(f"  Skipped agents/weekly-planner.md")

    # 4b. Strategy reviewer (if enabled)
    if agents_cfg.get("strategy_reviewer"):
        sr_content = render_template(env, "agents/strategy-reviewer.md.template", ctx)
        (output_dir / "agents" / "strategy-reviewer.md").write_text(sr_content, encoding="utf-8")
        print(f"  Generated agents/strategy-reviewer.md")

    # 4c. Exec update generator (if enabled)
    if agents_cfg.get("exec_update_generator"):
        eu_content = render_template(env, "agents/exec-update-generator.md.template", ctx)
        (output_dir / "agents" / "exec-update-generator.md").write_text(eu_content, encoding="utf-8")
        print(f"  Generated agents/exec-update-generator.md")

    # 5. Skills — copy from skills/ or generate from templates
    skills_src = PROJECT_ROOT / "skills"
    templates_dir = PROJECT_ROOT / "templates"

    if skills_cfg.get("prd_writer", True):
        skill = "prd-writer"
        if (skills_src / skill).exists():
            shutil.copytree(skills_src / skill, output_dir / "skills" / skill, dirs_exist_ok=True)
            print(f"  Copied skills/{skill}/")

    if skills_cfg.get("working_backwards", True):
        skill = "working-backwards"
        if (skills_src / skill).exists():
            shutil.copytree(skills_src / skill, output_dir / "skills" / skill, dirs_exist_ok=True)
            print(f"  Copied skills/{skill}/")

    if skills_cfg.get("pptx_creator", True):
        skill = "pptx-creator"
        if (skills_src / skill).exists():
            shutil.copytree(skills_src / skill, output_dir / "skills" / skill, dirs_exist_ok=True)
            print(f"  Copied skills/{skill}/")

    SKILL_MAP = {
        "strategy_connector": "strategy-connector",
        "exec_communicator": "exec-communicator",
        "experiment_designer": "experiment-designer",
        "launch_readiness": "launch-readiness",
        "launch_post": "launch-post",
        "one_pager": "one-pager",
        "stakeholder_update": "stakeholder-update",
        "meeting_to_actions": "meeting-to-actions",
        "experiment_writeup": "experiment-writeup",
        "brainstorming": "brainstorming",
        "writing_clearly": "writing-clearly",
    }
    for cfg_key, folder_name in SKILL_MAP.items():
        if skills_cfg.get(cfg_key, False) and (skills_src / folder_name).exists():
            shutil.copytree(skills_src / folder_name, output_dir / "skills" / folder_name, dirs_exist_ok=True)
            print(f"  Copied skills/{folder_name}/")

    # Action-item-prioritizer: generate from template (has goals/VIPs)
    if skills_cfg.get("action_item_prioritizer", True):
        ap_dir = output_dir / "skills" / "action-item-prioritizer"
        ap_dir.mkdir(parents=True, exist_ok=True)
        ap_tpl = templates_dir / "skills" / "action-item-prioritizer" / "SKILL.md.template"
        if ap_tpl.exists():
            env_ap = Environment(
                loader=FileSystemLoader(templates_dir / "skills" / "action-item-prioritizer"),
                trim_blocks=True,
                lstrip_blocks=True,
            )
            content = env_ap.get_template("SKILL.md.template").render(ctx)
            (ap_dir / "SKILL.md").write_text(content, encoding="utf-8")
            print(f"  Generated skills/action-item-prioritizer/SKILL.md")

    print(f"\nOutput written to: {output_dir}")

    # Always generate MCP config when tools are selected (project-level .cursor/mcp.json)
    generate_mcp_config(cfg)

    if mode == "output_only":
        print("\nNext: Copy or symlink from output/ to your Cursor directory.")
        return

    # Copy or symlink to Cursor
    cursor_rules = cursor_path / "rules"
    cursor_agents = cursor_path / "agents"
    cursor_skills = cursor_path / "skills"
    for d in [cursor_rules, cursor_agents, cursor_skills]:
        d.mkdir(parents=True, exist_ok=True)

    def deploy(src: Path, dst_dir: Path, mode: str):
        for f in src.iterdir():
            if f.is_file():
                target = dst_dir / f.name
                if target.exists():
                    target.unlink()
                if mode == "symlink":
                    target.symlink_to(f.resolve())
                else:
                    shutil.copy2(f, target)

    deploy(output_dir / "rules", cursor_rules, mode)
    deploy(output_dir / "agents", cursor_agents, mode)
    # Skills are directories
    for skill_dir in (output_dir / "skills").iterdir():
        if skill_dir.is_dir():
            dst = cursor_skills / skill_dir.name
            if dst.exists():
                shutil.rmtree(dst)
            if mode == "symlink":
                dst.symlink_to(skill_dir.resolve())
            else:
                shutil.copytree(skill_dir, dst)
            print(f"  Deployed skills/{skill_dir.name}/")

    print(f"\nDeployed to {cursor_path} (mode={mode})")
    print("Done. Restart Cursor or reload the window to pick up changes.")


if __name__ == "__main__":
    main()
