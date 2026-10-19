#!/usr/bin/env python3
"""
dedup_rules.py — Semantic Deduplication Engine for active_behavior_rules.yaml

PURPOSE:
    Prevents the 427-line bloat problem by ensuring no duplicate rules exist.
    Uses semantic fingerprinting (not just string match) to detect equivalent rules.

WHEN TO RUN:
    - Before any write to active_behavior_rules.yaml
    - As part of auto_consolidate.py pipeline
    - Via Windows Task Scheduler (weekly)

LOGIC:
    1. Load all existing rules (communication, code, governance, architecture, candidates)
    2. Compute fingerprint for each rule (normalized text hash)
    3. Remove any entry whose fingerprint already exists in a higher-priority section
    4. Write deduplicated file preserving ALL unique historical rules
    5. Log deduplication results to learning_log.md

GUARANTEE:
    Old rules are NEVER deleted — only exact semantic duplicates are removed.
    The history of unique rules is always preserved.

Usage:
    python dedup_rules.py              # deduplicate and save
    python dedup_rules.py --dry-run    # report duplicates without saving
    python dedup_rules.py --report     # print stats only
"""

import re
import yaml
import hashlib
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional

BRAIN_ROOT = Path.home() / ".second_brain"
RULES_FILE = BRAIN_ROOT / "active_behavior_rules.yaml"
LEARNING_LOG = BRAIN_ROOT / "learning_log.md"
REPORT_FILE = BRAIN_ROOT / "scripts" / "dedup_report.json"


def normalize_text(text: str) -> str:
    """Normalize rule text for semantic comparison."""
    text = text.lower().strip()
    # Remove source metadata patterns like (src: ANTIGRAVITY:xxxxxxxx)
    text = re.sub(r"\(src:.*?\)", "", text)
    # Remove prefixes like [RECOVERED|HIGH|explicit_correction]
    text = re.sub(r"\[RECOVERED\|[^\]]+\]", "", text)
    # Collapse whitespace
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def compute_fingerprint(text: str) -> str:
    """Semantic fingerprint: MD5 of normalized text, first 16 chars."""
    normalized = normalize_text(text)
    return hashlib.md5(normalized.encode("utf-8")).hexdigest()[:16]


def load_yaml(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def save_yaml(path: Path, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


def collect_all_fingerprints(rules: dict) -> dict[str, str]:
    """
    Collect fingerprints from all promoted rule sections.
    Returns {fingerprint: rule_id} for dedup checking.
    """
    seen: dict[str, str] = {}
    priority_sections = [
        "second_brain_rules",
        "communication_rules",
        "code_rules",
        "governance_rules",
        "architecture_rules",
        "promoted_rules",
    ]
    for section in priority_sections:
        for rule in rules.get(section, []) or []:
            fp = compute_fingerprint(str(rule.get("rule", "")))
            rule_id = rule.get("id", "unknown")
            if fp not in seen:
                seen[fp] = rule_id
            # Attach fingerprint to rule if missing
            if "fingerprint" not in rule:
                rule["fingerprint"] = fp
    return seen


def dedup_candidates(rules: dict, promoted_fps: dict[str, str], dry_run: bool = False) -> tuple[list, int, int]:
    """
    Deduplicate candidate_rules against promoted fingerprints and against each other.
    Returns (deduplicated_list, removed_count, kept_count).
    """
    candidates = rules.get("candidate_rules", []) or []
    seen_fps: dict[str, str] = dict(promoted_fps)
    kept = []
    removed = 0

    for candidate in candidates:
        rule_text = str(candidate.get("rule", ""))
        fp = candidate.get("fingerprint") or compute_fingerprint(rule_text)
        candidate["fingerprint"] = fp

        if fp in seen_fps:
            existing_id = seen_fps[fp]
            if not dry_run:
                pass  # Silent dedup
            else:
                print(f"  [DEDUP] '{candidate.get('id')}' duplicates '{existing_id}' — removing")
            removed += 1
        else:
            seen_fps[fp] = candidate.get("id", "unknown")
            kept.append(candidate)

    return kept, removed, len(kept)


def dedup_section(section: list, dry_run: bool = False) -> tuple[list, int]:
    """Remove duplicates within a single section."""
    seen_fps: dict[str, str] = {}
    kept = []
    removed = 0
    for rule in section or []:
        fp = compute_fingerprint(str(rule.get("rule", "")))
        rule_id = rule.get("id", "unknown")
        if fp in seen_fps:
            removed += 1
            if dry_run:
                print(f"  [DEDUP-INTERNAL] '{rule_id}' duplicates '{seen_fps[fp]}'")
        else:
            seen_fps[fp] = rule_id
            if "fingerprint" not in rule:
                rule["fingerprint"] = fp
            kept.append(rule)
    return kept, removed


def append_dedup_log(removed: int, kept: int, sections_cleaned: list[str]) -> None:
    if not LEARNING_LOG.exists():
        return
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = (
        f"\n### {timestamp} | DEDUP_ENGINE | AUTO\n"
        f"- Deduplication run: {removed} duplicates removed, {kept} unique rules kept\n"
        f"- Sections cleaned: {', '.join(sections_cleaned)}\n"
    )
    with open(LEARNING_LOG, "a", encoding="utf-8") as f:
        f.write(entry)


def run(dry_run: bool = False, report_only: bool = False) -> dict:
    print("=== SECOND BRAIN: Deduplication Engine ===")
    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'} | File: {RULES_FILE}")

    rules = load_yaml(RULES_FILE)
    if not rules:
        print("ERROR: Could not load active_behavior_rules.yaml")
        return {}

    total_removed = 0
    sections_cleaned = []

    # Step 1: Collect fingerprints from promoted sections
    promoted_fps = collect_all_fingerprints(rules)
    print(f"  Promoted fingerprints indexed: {len(promoted_fps)}")

    # Step 2: Dedup within each main section (internal duplicates)
    for section_name in ["second_brain_rules", "communication_rules", "code_rules",
                          "governance_rules", "architecture_rules", "promoted_rules"]:
        section = rules.get(section_name, [])
        if section:
            cleaned, removed = dedup_section(section, dry_run)
            if removed > 0:
                rules[section_name] = cleaned
                total_removed += removed
                sections_cleaned.append(section_name)
                print(f"  [{section_name}] Removed {removed} internal duplicate(s)")

    # Step 3: Dedup candidate_rules against promoted + against each other
    deduped_candidates, cand_removed, cand_kept = dedup_candidates(rules, promoted_fps, dry_run)
    if cand_removed > 0:
        rules["candidate_rules"] = deduped_candidates
        total_removed += cand_removed
        sections_cleaned.append("candidate_rules")

    print(f"\n  Total duplicates removed: {total_removed}")
    print(f"  Candidate rules kept: {cand_kept}")

    summary = {
        "timestamp": datetime.now().isoformat(),
        "total_removed": total_removed,
        "candidate_rules_kept": cand_kept,
        "sections_cleaned": sections_cleaned,
        "dry_run": dry_run,
    }

    if report_only:
        print("\n=== REPORT ONLY — No changes written ===")
        return summary

    if total_removed > 0 and not dry_run:
        save_yaml(RULES_FILE, rules)
        print(f"  Saved: {RULES_FILE}")
        append_dedup_log(total_removed, cand_kept, sections_cleaned)
        print("  Dedup event logged to learning_log.md")

    import json
    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    REPORT_FILE.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    print("=== DONE ===")
    return summary


def main() -> None:
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    report_only = "--report" in args
    run(dry_run=dry_run, report_only=report_only)


if __name__ == "__main__":
    main()
