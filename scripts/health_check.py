#!/usr/bin/env python3
"""
health_check.py — Autonomous Health Check Engine

Runs automatically via Windows Task Scheduler (daily, on logon).
Validates Second Brain integrity and writes report.
Zero user interaction required.
"""

import json
import yaml
from pathlib import Path
from datetime import datetime

BRAIN_ROOT = Path.home() / ".second_brain"
LEARNING_LOG = BRAIN_ROOT / "learning_log.md"
MASTER_INDEX = BRAIN_ROOT / "MASTER_INDEX.yaml"
REPORT_FILE = BRAIN_ROOT / "scripts" / "health_report.json"

REQUIRED_FILES = [
    "MASTER_INDEX.yaml",
    "global_rules.md",
    "behavioral_patterns.yaml",
    "active_behavior_rules.yaml",
    "learning_log.md",
]

REQUIRED_SCRIPTS = [
    "scripts/project_watcher.py",
    "scripts/learn_detector.py",
    "scripts/auto_consolidate.py",
    "scripts/health_check.py",
]


def check_file_integrity() -> list[dict]:
    results = []
    for fname in REQUIRED_FILES:
        path = BRAIN_ROOT / fname
        results.append({
            "file": fname,
            "exists": path.exists(),
            "size_bytes": path.stat().st_size if path.exists() else 0,
        })
    return results


def check_master_index_size() -> dict:
    if not MASTER_INDEX.exists():
        return {"ok": False, "lines": 0, "limit": 300}
    lines = len(MASTER_INDEX.read_text(encoding="utf-8").splitlines())
    return {"ok": lines <= 300, "lines": lines, "limit": 300}


def check_learning_log() -> dict:
    if not LEARNING_LOG.exists():
        return {"ok": False, "lines": 0, "size_kb": 0}
    content = LEARNING_LOG.read_text(encoding="utf-8")
    lines = len(content.splitlines())
    size_kb = round(LEARNING_LOG.stat().st_size / 1024, 1)
    pending = content.count("| USER |") + content.count("| ANTIGRAVITY |") + content.count("| CLAUDE |")
    return {
        "ok": True,
        "lines": lines,
        "size_kb": size_kb,
        "pending_entries": pending,
        "needs_consolidation": lines > 200,
    }


def check_project_contexts() -> list[dict]:
    projects_dir = BRAIN_ROOT / "projects"
    if not projects_dir.exists():
        return []
    results = []
    for ctx in projects_dir.glob("*_context.md"):
        age_days = (datetime.now() - datetime.fromtimestamp(ctx.stat().st_mtime)).days
        results.append({
            "project": ctx.stem.replace("_context", ""),
            "age_days": age_days,
            "stale": age_days > 30,
            "size_bytes": ctx.stat().st_size,
        })
    return results


def check_cursorrules() -> list[dict]:
    projects_root = Path("C:/Projetos")
    results = []
    if not projects_root.exists():
        return results
    for proj in projects_root.iterdir():
        if proj.is_dir() and not proj.name.startswith("_"):
            has_cursor = (proj / ".cursorrules").exists()
            results.append({"project": proj.name, "has_cursorrules": has_cursor})
    return results


def check_scripts() -> list[dict]:
    results = []
    for script in REQUIRED_SCRIPTS:
        path = BRAIN_ROOT / script
        results.append({"script": script, "exists": path.exists()})
    return results


def append_health_log(issues: list[str]) -> None:
    if not LEARNING_LOG.exists():
        return
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    if issues:
        entries = "\n".join(f"- HEALTH_ISSUE: {i}" for i in issues)
    else:
        entries = "- Health check passed: all systems nominal"
    block = f"\n### {timestamp} | HEALTH_CHECK | AUTO\n{entries}\n"
    with open(LEARNING_LOG, "a", encoding="utf-8") as f:
        f.write(block)


def main() -> None:
    print("=== SECOND BRAIN: Autonomous Health Check ===")
    print(f"Time: {datetime.now().isoformat()}")
    print()

    report = {
        "timestamp": datetime.now().isoformat(),
        "files": check_file_integrity(),
        "master_index": check_master_index_size(),
        "learning_log": check_learning_log(),
        "project_contexts": check_project_contexts(),
        "cursorrules": check_cursorrules(),
        "scripts": check_scripts(),
        "issues": [],
        "status": "OK",
    }

    issues = []

    # Evaluate results
    for f in report["files"]:
        if not f["exists"]:
            issues.append(f"MISSING core file: {f['file']}")
        elif f["size_bytes"] == 0:
            issues.append(f"EMPTY core file: {f['file']}")

    if not report["master_index"]["ok"]:
        issues.append(f"MASTER_INDEX exceeds 100 lines ({report['master_index']['lines']} lines)")

    ll = report["learning_log"]
    if ll.get("needs_consolidation"):
        issues.append(f"learning_log.md has {ll['lines']} lines — needs consolidation (run auto_consolidate.py)")

    for ctx in report["project_contexts"]:
        if ctx["stale"]:
            issues.append(f"Stale context: {ctx['project']} ({ctx['age_days']} days)")

    for cursor in report["cursorrules"]:
        if not cursor["has_cursorrules"]:
            issues.append(f"Missing .cursorrules: {cursor['project']}")

    for script in report["scripts"]:
        if not script["exists"]:
            issues.append(f"MISSING script: {script['script']}")

    report["issues"] = issues
    report["status"] = "ISSUES" if issues else "OK"

    # Print summary
    print(f"Files OK: {sum(1 for f in report['files'] if f['exists'])}/{len(report['files'])}")
    print(f"MASTER_INDEX: {report['master_index']['lines']} lines")
    print(f"Learning log: {ll.get('lines', 0)} lines, {ll.get('pending_entries', 0)} pending")
    print(f"Projects indexed: {len(report['project_contexts'])}")
    print(f"Issues: {len(issues)}")
    print()

    if issues:
        print("ISSUES DETECTED:")
        for i in issues:
            print(f"  - {i}")
    else:
        print("STATUS: All systems nominal")

    # Save report
    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    REPORT_FILE.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    # Log to learning_log
    append_health_log(issues)

    print(f"\nReport written: {REPORT_FILE}")
    print("=== DONE ===")


if __name__ == "__main__":
    main()
