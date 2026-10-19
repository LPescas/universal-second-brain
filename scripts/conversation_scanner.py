#!/usr/bin/env python3
"""
conversation_scanner.py — Fault-Tolerant Learning Recovery Engine

ARCHITECTURE: Stage 2 + 3 of the 3-stage redundant learning pipeline.

This script operates INDEPENDENTLY of agent compliance.
It scans conversation transcripts at the OS level and recovers
any learning events that the agent failed to write.

Sources scanned:
  - Antigravity IDE: ~/.gemini/antigravity-ide/brain/*/transcript.jsonl
  - Claude Code:     ~/.claude/sessions/*/
  - OpenClaude:      ~/.openclaude/sessions/*/

Recovery guarantee:
  - HIGH priority corrections: NEVER lost (scanned every 6h + on logon)
  - MEDIUM priority: scanned every 6h
  - LOW priority: scanned weekly during consolidation

Zero agent dependency. Runs as scheduled task.

Usage:
    python conversation_scanner.py              # full scan
    python conversation_scanner.py --days 3    # last 3 days only
    python conversation_scanner.py --conv <id> # single conversation
"""

import re
import json
import hashlib
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional
import sys

BRAIN_ROOT = Path.home() / ".second_brain"
LEARNING_LOG = BRAIN_ROOT / "learning_log.md"
SCAN_STATE = BRAIN_ROOT / "scripts" / "scanner_state.json"
RECOVERY_LOG = BRAIN_ROOT / "scripts" / "recovery_log.json"

ANTIGRAVITY_BRAIN = Path.home() / ".gemini" / "antigravity-ide" / "brain"
CLAUDE_SESSIONS = Path.home() / ".claude" / "sessions"
OPENCLAUDE_SESSIONS = Path.home() / ".openclaude" / "sessions"

# ============================================================
# LEARNING PRIORITY CLASSIFICATION
# ============================================================
PATTERNS = {
    "HIGH": [
        # Explicit corrections — architectural impact
        (r"nao (e|eh) assim", "explicit_correction"),
        (r"nao quero assim", "explicit_correction"),
        (r"\berrado\b", "explicit_correction"),
        (r"nao gostei", "explicit_correction"),
        (r"muda (isso|esse|essa)", "explicit_correction"),
        (r"that'?s wrong", "explicit_correction"),
        (r"not like that", "explicit_correction"),
        (r"nunca (faca|faz|use|uses)", "architectural"),
        (r"sempre (use|faz|faça)", "architectural"),
        (r"never (do|use)", "architectural"),
        (r"always (use|do)", "architectural"),
        (r"nao (use|usa) (isso|esse|essa)", "architectural"),
    ],
    "MEDIUM": [
        # Style / preference
        (r"\bprefiro\b", "style_preference"),
        (r"\bprefer\b", "style_preference"),
        (r"faz diferente", "style_preference"),
        (r"de outra forma", "style_preference"),
        (r"gostaria que", "style_preference"),
        (r"would (prefer|rather)", "style_preference"),
        (r"nao preciso de", "style_preference"),
        (r"pode (simplificar|simplifica|resumir|resumo)", "style_preference"),
    ],
    "LOW": [
        # Minor phrasing adjustments
        (r"pode mudar", "phrasing"),
        (r"nao precisa (de |ser )?tao", "phrasing"),
        (r"menos (detalhes|verboso|longo)", "phrasing"),
    ],
}

# Keywords to skip (meta-instructions, not user corrections)
SKIP_PATTERNS = [
    r"act like",
    r"your objective",
    r"you must",
    r"simulate",
    r"verify if",
    r"check if",
    r"MANDATORY",
]


def load_state() -> dict:
    if SCAN_STATE.exists():
        return json.loads(SCAN_STATE.read_text(encoding="utf-8"))
    return {"scanned_hashes": [], "last_scan": None, "recovered_count": 0}


def save_state(state: dict) -> None:
    SCAN_STATE.parent.mkdir(parents=True, exist_ok=True)
    SCAN_STATE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


def load_recovery_log() -> list:
    if RECOVERY_LOG.exists():
        return json.loads(RECOVERY_LOG.read_text(encoding="utf-8"))
    return []


def save_recovery_log(log: list) -> None:
    RECOVERY_LOG.write_text(json.dumps(log, indent=2, ensure_ascii=False), encoding="utf-8")


def content_hash(text: str) -> str:
    """Stable hash for deduplication."""
    return hashlib.md5(text.strip().lower().encode()).hexdigest()[:12]


def is_skip_content(text: str) -> bool:
    """Returns True if content is meta-instruction, not a real user correction."""
    text_lower = text.lower()
    for pattern in SKIP_PATTERNS:
        if re.search(pattern, text_lower):
            return True
    return False


def classify_learning_event(text: str) -> Optional[tuple[str, str, str]]:
    """
    Scan text for learning signals.
    Returns (priority, category, matched_pattern) or None.
    Priority: HIGH > MEDIUM > LOW
    """
    text_lower = text.lower()

    if is_skip_content(text_lower):
        return None

    for priority in ("HIGH", "MEDIUM", "LOW"):
        for pattern, category in PATTERNS[priority]:
            if re.search(pattern, text_lower):
                return (priority, category, pattern)

    return None


def extract_learning_from_text(text: str, source_label: str, timestamp: str) -> list[dict]:
    """
    Extract one or more learning events from a block of text.
    Returns list of event dicts.
    """
    events = []
    result = classify_learning_event(text)
    if not result:
        return events

    priority, category, pattern = result

    # Extract the relevant sentence(s)
    sentences = re.split(r"[.!?\n]", text)
    relevant = []
    for sentence in sentences:
        if re.search(pattern, sentence.lower()):
            cleaned = sentence.strip()
            if 5 < len(cleaned) < 300:
                relevant.append(cleaned)

    if not relevant:
        return events

    for sentence in relevant[:2]:  # max 2 per message
        h = content_hash(sentence)
        events.append({
            "hash": h,
            "priority": priority,
            "category": category,
            "content": sentence,
            "source": source_label,
            "timestamp": timestamp,
            "pattern": pattern,
            "recovered": False,
        })

    return events


def load_existing_log_hashes() -> set:
    """
    Load all content hashes already in learning_log.md to avoid duplicates.
    We hash each bullet point line in the log.
    """
    if not LEARNING_LOG.exists():
        return set()

    hashes = set()
    for line in LEARNING_LOG.read_text(encoding="utf-8").splitlines():
        if line.startswith("- ") and len(line) > 5:
            hashes.add(content_hash(line[2:]))

    return hashes


def append_recovered_events(events: list[dict], existing_hashes: set) -> int:
    """
    Append recovered learning events to learning_log.md.
    Only appends events NOT already in the log (checks both existing_hashes and
    a fresh re-read to prevent duplicates from concurrent scans).
    Returns count of new entries written.
    """
    # Re-read hashes fresh to catch concurrent writes
    fresh_hashes = load_existing_log_hashes()
    combined_hashes = existing_hashes | fresh_hashes

    new_events = [e for e in events if e["hash"] not in combined_hashes]
    if not new_events:
        return 0

    # Group by priority for ordered writing
    high = [e for e in new_events if e["priority"] == "HIGH"]
    medium = [e for e in new_events if e["priority"] == "MEDIUM"]
    low = [e for e in new_events if e["priority"] == "LOW"]

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    blocks = []

    for priority_group, label in [(high, "HIGH"), (medium, "MEDIUM"), (low, "LOW")]:
        if priority_group:
            entries = "\n".join(
                f"- [RECOVERED|{e['priority']}|{e['category']}] {e['content']} (src: {e['source']})"
                for e in priority_group
            )
            blocks.append(
                f"\n### {timestamp} | SCANNER | RECOVERY_{label}\n{entries}\n"
            )

    if blocks:
        with open(LEARNING_LOG, "a", encoding="utf-8") as f:
            for block in blocks:
                f.write(block)

    return len(new_events)


def scan_antigravity_transcripts(days_back: int = 7, specific_conv: Optional[str] = None) -> list[dict]:
    """
    Scan Antigravity IDE transcript.jsonl files for learning events.
    Only USER_INPUT type steps are scanned (the actual user messages).
    """
    events = []
    if not ANTIGRAVITY_BRAIN.exists():
        return events

    cutoff = datetime.now() - timedelta(days=days_back)

    # Determine which conversations to scan
    if specific_conv:
        # In --conv mode, accept any directory name (not just UUIDs)
        conv_path = ANTIGRAVITY_BRAIN / specific_conv
        conv_dirs = [conv_path] if conv_path.exists() else []
        if not conv_dirs:
            print(f"  [WARN] Conversation dir not found: {conv_path}")
            return events
    else:
        conv_dirs = [
            d for d in ANTIGRAVITY_BRAIN.iterdir()
            if d.is_dir()
            and re.match(r"^[0-9a-f\-]{8,}", d.name)  # relaxed: any hex-dash prefix
            and datetime.fromtimestamp(d.stat().st_mtime) > cutoff
        ]

    for conv_dir in conv_dirs:
        transcript = conv_dir / ".system_generated" / "logs" / "transcript.jsonl"
        if not transcript.exists():
            continue

        source_label = f"ANTIGRAVITY:{conv_dir.name[:8]}"

        try:
            for line in transcript.read_text(encoding="utf-8", errors="ignore").splitlines():
                if not line.strip():
                    continue
                try:
                    step = json.loads(line)
                except json.JSONDecodeError:
                    continue

                # Only scan USER_INPUT — the actual user text
                if step.get("type") not in ("USER_INPUT",):
                    continue
                if step.get("source") not in ("USER_EXPLICIT", "USER"):
                    continue

                content = str(step.get("content", ""))

                # Strip XML-like wrappers injected by IDE
                content = re.sub(r"<USER_REQUEST>", "", content)
                content = re.sub(r"</USER_REQUEST>", "", content)
                # Remove ADDITIONAL_METADATA and USER_SETTINGS_CHANGE blocks entirely
                content = re.sub(r"(?s)<ADDITIONAL_METADATA>.*?</ADDITIONAL_METADATA>", "", content)
                content = re.sub(r"(?s)<USER_SETTINGS_CHANGE>.*?</USER_SETTINGS_CHANGE>", "", content)
                content = content.strip()

                # Skip empty after stripping
                if not content or len(content) < 5:
                    continue

                # Skip structured "Act like a senior..." prompts (meta-instructions, not corrections)
                # These are task definitions, not user feedback
                first_line = content.splitlines()[0].strip().lower() if content.splitlines() else ""
                if re.match(r'^(act like|your objective|simulate|you must|take a deep breath|this is not)', first_line):
                    continue

                # Extract timestamp from step if available
                timestamp = step.get("timestamp", datetime.now().isoformat())
                if isinstance(timestamp, (int, float)):
                    timestamp = datetime.fromtimestamp(timestamp / 1000).strftime("%Y-%m-%d %H:%M")

                step_events = extract_learning_from_text(content, source_label, str(timestamp))
                events.extend(step_events)
        except Exception as e:
            print(f"  [WARN] Error scanning {transcript}: {e}")

    return events


def scan_claude_sessions(days_back: int = 7) -> list[dict]:
    """
    Scan Claude Code session files for learning events.
    """
    events = []

    for sessions_dir in (CLAUDE_SESSIONS, OPENCLAUDE_SESSIONS):
        if not sessions_dir.exists():
            continue

        cutoff = datetime.now() - timedelta(days=days_back)
        session_files = [
            f for f in sessions_dir.rglob("*.json")
            if datetime.fromtimestamp(f.stat().st_mtime) > cutoff
        ]

        for session_file in session_files:
            try:
                data = json.loads(session_file.read_text(encoding="utf-8", errors="ignore"))
                source_label = f"CLAUDE:{session_file.stem[:8]}"
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

                # Handle different Claude session formats
                messages = []
                if isinstance(data, list):
                    messages = data
                elif isinstance(data, dict):
                    messages = data.get("messages", data.get("turns", []))

                for msg in messages:
                    if isinstance(msg, dict):
                        role = msg.get("role", msg.get("type", ""))
                        if role in ("user", "human"):
                            content = str(msg.get("content", msg.get("text", "")))
                            step_events = extract_learning_from_text(content, source_label, timestamp)
                            events.extend(step_events)

            except Exception as e:
                pass  # Skip malformed session files silently

    return events


def run_scan(days_back: int = 7, specific_conv: Optional[str] = None) -> dict:
    """
    Main scan orchestrator.
    Returns summary dict.
    """
    state = load_state()
    recovery_log = load_recovery_log()
    existing_hashes = load_existing_log_hashes()

    print(f"[SCANNER] Starting fault-tolerant scan (last {days_back} days)")
    print(f"[SCANNER] Existing log entries: {len(existing_hashes)}")

    # Scan all sources
    all_events = []

    print("[SCANNER] Scanning Antigravity transcripts...")
    ag_events = scan_antigravity_transcripts(days_back, specific_conv)
    all_events.extend(ag_events)
    print(f"  Found: {len(ag_events)} candidate event(s)")

    print("[SCANNER] Scanning Claude sessions...")
    cl_events = scan_claude_sessions(days_back)
    all_events.extend(cl_events)
    print(f"  Found: {len(cl_events)} candidate event(s)")

    # Deduplicate by hash
    seen_hashes = set()
    unique_events = []
    for event in all_events:
        if event["hash"] not in seen_hashes and event["hash"] not in existing_hashes:
            seen_hashes.add(event["hash"])
            unique_events.append(event)

    # Separate by priority
    high = [e for e in unique_events if e["priority"] == "HIGH"]
    medium = [e for e in unique_events if e["priority"] == "MEDIUM"]
    low = [e for e in unique_events if e["priority"] == "LOW"]

    print(f"[SCANNER] New events: HIGH={len(high)}, MEDIUM={len(medium)}, LOW={len(low)}")

    # Write HIGH + MEDIUM always. LOW only if < 50 total events.
    events_to_write = high + medium
    if len(unique_events) < 50:
        events_to_write += low

    written = append_recovered_events(events_to_write, existing_hashes)

    # Update state
    state["last_scan"] = datetime.now().isoformat()
    state["recovered_count"] = state.get("recovered_count", 0) + written

    # Update recovery log
    if events_to_write:
        recovery_log.append({
            "timestamp": datetime.now().isoformat(),
            "scanned_conversations": len(set(e["source"] for e in all_events)),
            "candidates": len(all_events),
            "new_high": len(high),
            "new_medium": len(medium),
            "new_low": len(low),
            "written": written,
        })

    save_state(state)
    save_recovery_log(recovery_log)

    summary = {
        "candidates": len(all_events),
        "written": written,
        "high_recovered": len(high),
        "medium_recovered": len(medium),
        "low_recovered": len(low),
        "total_recovered_ever": state["recovered_count"],
    }

    print(f"[SCANNER] Written to learning_log.md: {written} new entries")
    print(f"[SCANNER] Total recovered (all time): {state['recovered_count']}")
    print("[SCANNER] DONE")

    return summary


def main() -> None:
    args = sys.argv[1:]
    days_back = 7
    specific_conv = None

    if "--days" in args:
        idx = args.index("--days")
        if idx + 1 < len(args):
            days_back = int(args[idx + 1])

    if "--conv" in args:
        idx = args.index("--conv")
        if idx + 1 < len(args):
            specific_conv = args[idx + 1]

    run_scan(days_back=days_back, specific_conv=specific_conv)


if __name__ == "__main__":
    main()
