#!/usr/bin/env python3
"""
project_watcher.py — Autonomous Project Scanner & Registrar

Runs automatically on:
  - Windows Logon (Task Scheduler trigger)
  - Every 30 minutes (periodic trigger)

Actions per new project detected:
  1. Deploy .cursorrules from Second Brain template
  2. Create project context file in ~/.second_brain/projects/
  3. Inject entry into MASTER_INDEX.yaml
  4. Append discovery event to learning_log.md
  5. Install git hooks if .git exists

Zero user interaction required. Fully autonomous.
"""

import os
import re
import sys
import json
import yaml
import shutil
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Optional

BRAIN_ROOT = Path.home() / ".second_brain"
PROJECTS_ROOT = Path("C:/Projetos")
MASTER_INDEX = BRAIN_ROOT / "MASTER_INDEX.yaml"
LEARNING_LOG = BRAIN_ROOT / "learning_log.md"
CURSOR_TEMPLATE = BRAIN_ROOT / "integrations" / "cursorrules_template.md"
PROJECTS_DIR = BRAIN_ROOT / "projects"
STATE_FILE = BRAIN_ROOT / "scripts" / "watcher_state.json"

GIT_HOOK_CONTENT = """#!/bin/sh
# Second Brain auto-hook — injected by project_watcher.py
# Runs after checkout/merge to ensure Second Brain context is current.
python "C:/Users/USER/.second_brain/scripts/project_watcher.py" --single "$(pwd)" 2>/dev/null &
"""

CONTEXT_TEMPLATE = """\
# Contexto do Projeto: {name}

> Carregamento sob demanda. Detectado automaticamente em {date}.

---

## Visao Geral

Projeto detectado pelo Second Brain Watcher automaticamente.
Preencha esta secao com uma descricao do projeto apos a criacao.

## Caminho

`{path}`

## Stack Tecnica

_Detectar automaticamente via analise de arquivos._

{tech_block}

---

## Historico

| Data       | Descricao                                              |
|------------|--------------------------------------------------------|
| {date}     | Projeto detectado e registrado automaticamente pelo watcher |
"""


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {"indexed": [], "last_scan": None}


def save_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")


def load_yaml(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def save_yaml(path: Path, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


def detect_tech(project_path: Path) -> list[str]:
    """Auto-detect tech stack from file extensions and config files."""
    tech = []
    indicators = {
        "python": ["*.py", "requirements.txt", "setup.py", "pyproject.toml"],
        "node/js": ["package.json", "*.js", "*.ts"],
        "react/next": ["next.config.*", "*.jsx", "*.tsx"],
        "flask": ["app*.py", "wsgi.py"],
        "selenium": ["requirements.txt"],  # check content
        "sqlite": ["*.db", "*.sqlite"],
        "html": ["*.html"],
        "docker": ["Dockerfile", "docker-compose.*"],
    }

    for tech_name, patterns in indicators.items():
        for pattern in patterns:
            matches = list(project_path.glob(f"**/{pattern}"))
            if matches:
                # Special case: selenium inside requirements
                if tech_name == "selenium":
                    req_files = list(project_path.glob("**/requirements.txt"))
                    for req in req_files:
                        try:
                            content = req.read_text(errors="ignore")
                            if "selenium" in content.lower():
                                tech.append("selenium")
                                break
                        except Exception:
                            pass
                else:
                    tech.append(tech_name)
                break

    return list(set(tech))


def deploy_cursorrules(project_path: Path) -> bool:
    """Deploy .cursorrules to project if not already present."""
    target = project_path / ".cursorrules"
    if target.exists():
        return False  # Already deployed
    if CURSOR_TEMPLATE.exists():
        shutil.copy2(CURSOR_TEMPLATE, target)
        return True
    return False


def create_context(project_name: str, project_path: Path, tech: list[str]) -> bool:
    """Create project context file in Second Brain projects dir."""
    safe_name = re.sub(r"\s+", "_", project_name.lower())
    ctx_file = PROJECTS_DIR / f"{safe_name}_context.md"
    if ctx_file.exists():
        return False  # Already exists

    tech_block = ""
    if tech:
        tech_block = "## Stack Detectada\n\n" + "\n".join(f"- `{t}`" for t in tech)

    content = CONTEXT_TEMPLATE.format(
        name=project_name,
        date=datetime.now().strftime("%Y-%m-%d"),
        path=str(project_path),
        tech_block=tech_block,
    )
    ctx_file.write_text(content, encoding="utf-8")
    return True


def update_master_index(project_name: str, project_path: Path, tech: list[str]) -> bool:
    """
    Inject new project entry into MASTER_INDEX.yaml projects section.
    Only if not already present.
    """
    index = load_yaml(MASTER_INDEX)
    projects = index.get("projects", {})

    safe_name = re.sub(r"\s+", "_", project_name.lower())

    if safe_name in projects:
        return False  # Already indexed

    # Build domain keywords from name and tech
    domain_keywords = [project_name.lower()] + tech
    domain_keywords = list(set(kw.replace("/", "_") for kw in domain_keywords))

    projects[safe_name] = {
        "path": str(project_path),
        "context": f"projects/{safe_name}_context.md",
        "domain": domain_keywords,
        "tech": tech,
        "auto_detected": datetime.now().strftime("%Y-%m-%d"),
    }

    index["projects"] = projects
    save_yaml(MASTER_INDEX, index)
    return True


def install_git_hooks(project_path: Path) -> bool:
    """Install post-checkout and post-merge hooks if .git exists."""
    git_dir = project_path / ".git"
    if not git_dir.exists():
        return False

    hooks_dir = git_dir / "hooks"
    hooks_dir.mkdir(exist_ok=True)
    installed = False

    for hook_name in ("post-checkout", "post-merge", "post-commit"):
        hook_file = hooks_dir / hook_name
        if not hook_file.exists():
            hook_file.write_text(GIT_HOOK_CONTENT, encoding="utf-8")
            # Make executable (no-op on Windows but correct for WSL/cross-platform)
            try:
                hook_file.chmod(0o755)
            except Exception:
                pass
            installed = True

    return installed


def append_learning_log(events: list[str]) -> None:
    """Append discovery events to learning_log.md."""
    if not events or not LEARNING_LOG.exists():
        return
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entries = "\n".join(f"- {e}" for e in events)
    block = f"\n### {timestamp} | WATCHER | AUTO_DETECT\n{entries}\n"
    with open(LEARNING_LOG, "a", encoding="utf-8") as f:
        f.write(block)


def scan_project(project_path: Path, state: dict) -> list[str]:
    """
    Process a single project directory.
    Returns list of actions taken (for logging).
    """
    project_name = project_path.name
    safe_name = re.sub(r"\s+", "_", project_name.lower())
    actions = []

    # Skip hidden dirs, venvs, node_modules
    skip_patterns = {".venv", "venv", "node_modules", ".git", "__pycache__", ".pytest_cache"}
    if project_name.startswith("_audit_") or project_name in skip_patterns:
        return []

    tech = detect_tech(project_path)

    cursor_deployed = deploy_cursorrules(project_path)
    if cursor_deployed:
        actions.append(f"Deployed .cursorrules to {project_name}")

    ctx_created = create_context(project_name, project_path, tech)
    if ctx_created:
        actions.append(f"Created Second Brain context for {project_name} (tech: {', '.join(tech) or 'unknown'})")

    index_updated = update_master_index(project_name, project_path, tech)
    if index_updated:
        actions.append(f"Registered {project_name} in MASTER_INDEX.yaml")

    hooks_installed = install_git_hooks(project_path)
    if hooks_installed:
        actions.append(f"Installed git hooks in {project_name}")

    if actions and safe_name not in state["indexed"]:
        state["indexed"].append(safe_name)

    return actions


def run_full_scan(args: list[str]) -> None:
    """Scan all projects or a single specified one."""
    state = load_state()
    state["last_scan"] = datetime.now().isoformat()
    all_actions = []

    # Single project mode (called from git hook)
    if "--single" in args:
        idx = args.index("--single")
        if idx + 1 < len(args):
            single_path = Path(args[idx + 1])
            if single_path.exists():
                actions = scan_project(single_path, state)
                all_actions.extend(actions)
    else:
        # Full scan of PROJECTS_ROOT
        if PROJECTS_ROOT.exists():
            for proj_dir in PROJECTS_ROOT.iterdir():
                if proj_dir.is_dir():
                    actions = scan_project(proj_dir, state)
                    all_actions.extend(actions)

        # Also scan current working directory if it's a project not in PROJECTS_ROOT
        cwd = Path.cwd()
        if cwd.is_dir() and cwd.parent != PROJECTS_ROOT and cwd != PROJECTS_ROOT:
            if (cwd / ".git").exists() or list(cwd.glob("*.py")) or list(cwd.glob("package.json")):
                actions = scan_project(cwd, state)
                all_actions.extend(actions)

    # Log all actions
    if all_actions:
        append_learning_log(all_actions)
        print(f"[WATCHER] {len(all_actions)} action(s) taken:")
        for a in all_actions:
            print(f"  - {a}")
    else:
        print("[WATCHER] No new projects detected. All indexed.")

    save_state(state)


if __name__ == "__main__":
    run_full_scan(sys.argv[1:])
