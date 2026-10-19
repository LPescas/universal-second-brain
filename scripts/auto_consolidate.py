#!/usr/bin/env python3
"""
auto_consolidate.py — Autonomous Weekly Consolidation Engine

PIPELINE:
  1. Run learn_detector.py (scan for patterns)
  2. Load candidate_rules from active_behavior_rules.yaml
  3. Auto-promote rules with status == "promotion_candidate" (>=3 occurrences)
     to behavioral_patterns.yaml WITHOUT human intervention
  4. Prune consolidated entries from learning_log.md
  5. Write consolidation history

SCHEDULE: Weekly via Windows Task Scheduler (configured by setup)
RULE: Auto-promotion ONLY for patterns with occurrences >= 3.
      Corrections with occurrences < 3 still require manual validation.

Run: python auto_consolidate.py
"""

import re
import yaml
import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime, date
from typing import Optional

BRAIN_ROOT = Path.home() / ".second_brain"
LOG_FILE = BRAIN_ROOT / "learning_log.md"
RULES_FILE = BRAIN_ROOT / "active_behavior_rules.yaml"
PATTERNS_FILE = BRAIN_ROOT / "behavioral_patterns.yaml"
HISTORY_FILE = BRAIN_ROOT / "scripts" / "consolidation_history.json"
DETECTOR_SCRIPT = BRAIN_ROOT / "scripts" / "learn_detector.py"
DEDUP_SCRIPT = BRAIN_ROOT / "scripts" / "dedup_rules.py"

AUTO_PROMOTE_THRESHOLD = 3


def run_detector() -> None:
    """Execute learn_detector.py first to refresh candidate_rules."""
    print("[1/5] Running learn_detector.py...")
    result = subprocess.run(
        [sys.executable, str(DETECTOR_SCRIPT)],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    print(result.stdout)
    if result.returncode != 0:
        print(f"WARN: Detector had errors: {result.stderr}")


def load_yaml(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def save_yaml(path: Path, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


def load_history() -> list:
    if not HISTORY_FILE.exists():
        return []
    return json.loads(HISTORY_FILE.read_text(encoding="utf-8"))


def save_history(history: list) -> None:
    HISTORY_FILE.write_text(json.dumps(history, indent=2, ensure_ascii=False), encoding="utf-8")


def promote_candidates(rules: dict, patterns: dict) -> tuple[dict, dict, int]:
    """
    Auto-promote candidate_rules with occurrences >= threshold.
    Returns updated rules, updated patterns, and count promoted.
    """
    candidates = rules.get("candidate_rules", []) or []
    promoted_count = 0
    today = str(date.today())

    # Ensure auto_promoted section exists in patterns
    if "auto_promoted" not in patterns:
        patterns["auto_promoted"] = []

    for candidate in candidates:
        if (
            candidate.get("status") == "promotion_candidate"
            and candidate.get("occurrences", 0) >= AUTO_PROMOTE_THRESHOLD
        ):
            promoted_entry = {
                "id": candidate["id"],
                "rule": candidate["rule"],
                "promoted_on": today,
                "occurrences": candidate["occurrences"],
                "source": candidate.get("source", "auto_consolidate"),
            }
            patterns["auto_promoted"].append(promoted_entry)
            candidate["status"] = "promoted"
            candidate["promoted_on"] = today
            promoted_count += 1

    return rules, patterns, promoted_count


def prune_learning_log(promoted_count: int) -> int:
    """
    Mark consolidated entries in learning_log.md.
    Does NOT delete — only adds [CONSOLIDATED] markers.
    Returns lines processed.
    """
    if promoted_count == 0:
        return 0

    content = LOG_FILE.read_text(encoding="utf-8")
    today = str(date.today())

    # Add consolidation marker at top of Consolidated section
    marker = f"\n### {today} | AUTO_CONSOLIDATE | PROMOTED\n- {promoted_count} pattern(s) auto-promoted from candidate_rules.\n"
    content = content.replace(
        "_Empty — awaiting first consolidation cycle._",
        marker.strip()
    )

    # Update history table in log
    history_line = f"| {today} | auto_detect | {promoted_count} | 0 |"
    content = content.replace(
        "| _none_ | _none_ | _none_ | _none_ |",
        history_line
    )

    LOG_FILE.write_text(content, encoding="utf-8")
    return promoted_count


def write_history(promoted_count: int, candidates_total: int) -> None:
    history = load_history()
    history.append({
        "date": datetime.now().isoformat(),
        "candidates_scanned": candidates_total,
        "promoted": promoted_count,
        "auto": True,
    })
    save_history(history)


def main() -> None:
    print("=== SECOND BRAIN: Auto-Consolidation Engine ===")
    print(f"Date: {datetime.now().isoformat()}")
    print("")

    # Step 1: Run detector to refresh candidates
    run_detector()

    # Step 2: Load current state
    print("[2/5] Loading current rules and patterns...")
    rules = load_yaml(RULES_FILE)
    patterns = load_yaml(PATTERNS_FILE)

    candidates = rules.get("candidate_rules", []) or []
    eligible = [c for c in candidates if c.get("status") == "promotion_candidate"]
    print(f"  Candidates total: {len(candidates)}")
    print(f"  Eligible for auto-promotion: {len(eligible)}")

    if not eligible:
        print("[3/5] No candidates eligible for auto-promotion. Nothing to do.")
        write_history(0, len(candidates))
        print("=== DONE (no changes) ===")
        return

    # Step 3: Promote
    print(f"[3/5] Auto-promoting {len(eligible)} rule(s)...")
    rules, patterns, promoted_count = promote_candidates(rules, patterns)
    print(f"  Promoted: {promoted_count}")

    # Step 4: Save updated files
    print("[4/5] Saving updated files...")
    save_yaml(RULES_FILE, rules)
    save_yaml(PATTERNS_FILE, patterns)
    pruned = prune_learning_log(promoted_count)
    print(f"  active_behavior_rules.yaml: updated")
    print(f"  behavioral_patterns.yaml: updated")
    print(f"  learning_log.md: {pruned} entries marked")

    # Step 4b: Run deduplication after save
    print("[4b/5] Running deduplication engine...")
    if DEDUP_SCRIPT.exists():
        dedup_result = subprocess.run(
            [sys.executable, str(DEDUP_SCRIPT)],
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        print(dedup_result.stdout)
        if dedup_result.returncode != 0:
            print(f"WARN: Dedup had errors: {dedup_result.stderr}")
    else:
        print("  WARN: dedup_rules.py not found — skipping")

    # Step 5: Write history
    print("[5/5] Writing consolidation history...")
    write_history(promoted_count, len(candidates))

    print("")
    print(f"=== DONE: {promoted_count} rule(s) promoted to behavioral layer ===")


if __name__ == "__main__":
    main()
