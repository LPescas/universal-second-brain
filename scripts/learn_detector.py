#!/usr/bin/env python3
"""
learn_detector.py — Pattern Detection Engine (Layer 1 & 2)

Scans learning_log.md for:
  - Explicit corrections (keyword-triggered)
  - Repeated patterns (>= 3 occurrences)
  - Promotion candidates

Outputs to:
  - active_behavior_rules.yaml (candidate_rules section)
  - learning_log.md (flags entries)

Run: python learn_detector.py
Schedule: Daily via Task Scheduler or cron
"""

import re
import yaml
import json
from pathlib import Path
from datetime import datetime, date
from collections import Counter
from typing import Optional

BRAIN_ROOT = Path.home() / ".second_brain"
LOG_FILE = BRAIN_ROOT / "learning_log.md"
RULES_FILE = BRAIN_ROOT / "active_behavior_rules.yaml"
PATTERNS_FILE = BRAIN_ROOT / "behavioral_patterns.yaml"
REPORT_FILE = BRAIN_ROOT / "scripts" / "detect_report.json"

CORRECTION_KEYWORDS = [
    "nao e assim", "nao quero assim", "prefiro", "faz diferente",
    "errado", "nao gostei", "muda isso", "that's wrong",
    "not like that", "prefer", "nao use", "sempre use",
    "nunca faca", "evita", "avoid", "always", "never",
]


def load_log() -> list[str]:
    if not LOG_FILE.exists():
        return []
    return LOG_FILE.read_text(encoding="utf-8").splitlines()


def extract_entries(lines: list[str]) -> list[dict]:
    """Parse learning_log.md entries into structured dicts."""
    entries = []
    current: Optional[dict] = None

    for line in lines:
        # Match section header: ### DATE | SOURCE | TYPE
        header_match = re.match(r"^### (\d{4}-\d{2}-\d{2}[^\|]*)\| ([^\|]+) \| ([^\n]+)", line)
        if header_match:
            if current:
                entries.append(current)
            current = {
                "date": header_match.group(1).strip(),
                "source": header_match.group(2).strip(),
                "type": header_match.group(3).strip(),
                "content": [],
                "raw": line,
            }
        elif current and line.startswith("- "):
            current["content"].append(line[2:].strip())

    if current:
        entries.append(current)

    return entries


def detect_corrections(entries: list[dict]) -> list[dict]:
    """Find entries containing correction keywords."""
    corrections = []
    for entry in entries:
        for item in entry["content"]:
            item_lower = item.lower()
            for kw in CORRECTION_KEYWORDS:
                if kw in item_lower:
                    corrections.append({
                        "date": entry["date"],
                        "source": entry["source"],
                        "content": item,
                        "trigger_keyword": kw,
                    })
                    break
    return corrections


def detect_repeated_patterns(entries: list[dict], threshold: int = 3) -> list[dict]:
    """
    Find content items that appear >= threshold times across entries.
    Normalize and cluster similar items.
    """
    all_content = []
    for entry in entries:
        for item in entry["content"]:
            # Normalize: lowercase, strip punctuation edges
            normalized = re.sub(r"[^\w\s]", "", item.lower()).strip()
            if len(normalized) > 15:  # skip trivially short entries
                all_content.append((normalized, item, entry["date"]))

    # Count occurrences
    counter = Counter(item[0] for item in all_content)
    repeated = []
    seen = set()

    for normalized, original, first_date in all_content:
        if counter[normalized] >= threshold and normalized not in seen:
            seen.add(normalized)
            repeated.append({
                "pattern": original,
                "occurrences": counter[normalized],
                "first_seen": first_date,
            })

    return repeated


def load_rules() -> dict:
    if not RULES_FILE.exists():
        return {}
    with open(RULES_FILE, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def update_candidate_rules(
    rules: dict,
    corrections: list[dict],
    repeated: list[dict],
) -> dict:
    """Merge detected patterns into candidate_rules section."""
    candidates = rules.get("candidate_rules", []) or []
    existing_ids = {c.get("id") for c in candidates}
    today = str(date.today())

    # Add corrections as candidates
    for i, correction in enumerate(corrections):
        cand_id = f"CAND-CORR-{today}-{i:03d}"
        if cand_id not in existing_ids:
            candidates.append({
                "id": cand_id,
                "rule": correction["content"],
                "trigger": correction["trigger_keyword"],
                "occurrences": 1,
                "first_seen": correction["date"],
                "last_seen": today,
                "status": "pending",
                "source": f"CORRECTION | {correction['source']}",
            })

    # Add repeated patterns as candidates
    for i, pattern in enumerate(repeated):
        cand_id = f"CAND-REPEAT-{today}-{i:03d}"
        if cand_id not in existing_ids:
            candidates.append({
                "id": cand_id,
                "rule": pattern["pattern"],
                "occurrences": pattern["occurrences"],
                "first_seen": pattern["first_seen"],
                "last_seen": today,
                "status": "promotion_candidate" if pattern["occurrences"] >= 3 else "pending",
                "source": f"REPEATED_PATTERN | {pattern['occurrences']}x",
            })

    rules["candidate_rules"] = candidates
    return rules


def write_rules(rules: dict) -> None:
    with open(RULES_FILE, "w", encoding="utf-8") as f:
        # Preserve header comments by writing manually
        f.write("# active_behavior_rules.yaml — auto-updated by learn_detector.py\n")
        f.write(f"# Last scan: {datetime.now().isoformat()}\n")
        yaml.dump(rules, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


def write_report(corrections: list[dict], repeated: list[dict]) -> None:
    report = {
        "scan_date": datetime.now().isoformat(),
        "corrections_found": len(corrections),
        "repeated_patterns_found": len(repeated),
        "promotion_candidates": len([r for r in repeated if r.get("occurrences", 0) >= 3]),
        "corrections": corrections[:10],  # top 10
        "repeated": repeated[:10],
    }
    REPORT_FILE.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")


def main() -> None:
    print("=== SECOND BRAIN: Learning Detector ===")
    print(f"Scanning: {LOG_FILE}")

    lines = load_log()
    if not lines:
        print("ERROR: learning_log.md not found or empty.")
        return

    entries = extract_entries(lines)
    print(f"Entries parsed: {len(entries)}")

    corrections = detect_corrections(entries)
    print(f"Corrections detected: {len(corrections)}")

    repeated = detect_repeated_patterns(entries, threshold=3)
    print(f"Repeated patterns (>=3x): {len(repeated)}")

    rules = load_rules()
    rules = update_candidate_rules(rules, corrections, repeated)
    write_rules(rules)
    write_report(corrections, repeated)

    promoted = [c for c in rules.get("candidate_rules", []) if c.get("status") == "promotion_candidate"]
    print(f"Promotion candidates flagged: {len(promoted)}")
    print(f"Rules file updated: {RULES_FILE}")
    print(f"Report written: {REPORT_FILE}")
    print("=== DONE ===")


if __name__ == "__main__":
    main()
