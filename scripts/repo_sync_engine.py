#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
"""
repo_sync_engine.py -- Motor de Auto-Sincronizacao do Second Brain Hub
======================================================================
Clona e/ou atualiza todos os 25 repositorios listados no repos_manifest.yaml.
Protecao Cold Snapshot: repositorios deletados/privatizados remotamente ficam
LOCKED localmente sem perda de dados.

Uso:
    python repo_sync_engine.py                  # sync completo
    python repo_sync_engine.py --clone-only     # apenas clone inicial
    python repo_sync_engine.py --repo nango     # sync de repo especifico
    python repo_sync_engine.py --dry-run        # simula sem executar
    python repo_sync_engine.py --status         # mostra status de todos
"""
import argparse
import io
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

# Force UTF-8 output on Windows to avoid cp1252 errors
if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


# ──────────────────────────────────────────────────────────────
# Configurações
# ──────────────────────────────────────────────────────────────
SB_ROOT = Path(r"C:\Users\USER\.second_brain")
REPOS_ROOT = SB_ROOT / "repos"
MANIFEST_PATH = REPOS_ROOT / "repos_manifest.yaml"
HISTORY_PATH = SB_ROOT / "scripts" / "repo_sync_history.json"
LOG_PATH = SB_ROOT / "scripts" / "repo_sync.log"

COLD_SNAPSHOT_STATUS = "COLD_SNAPSHOT_LOCKED"
OK_STATUS = "OK"
PENDING_STATUS = "PENDING"
ERROR_STATUS = "ERROR"


# ──────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────
def log(msg: str, level: str = "INFO") -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    line = f"[{ts}] [{level}] {msg}"
    print(line)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def load_manifest() -> dict:
    with MANIFEST_PATH.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def save_manifest(manifest: dict) -> None:
    with MANIFEST_PATH.open("w", encoding="utf-8") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False, default_flow_style=False)


def load_history() -> list:
    if HISTORY_PATH.exists():
        with HISTORY_PATH.open("r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_history(history: list) -> None:
    with HISTORY_PATH.open("w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)


def run_git(args: list[str], cwd: Path, timeout: int = 120) -> tuple[bool, str]:
    """Execute a git command, return (success, output)."""
    try:
        result = subprocess.run(
            ["git"] + args,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            timeout=timeout,
            encoding="utf-8",
            errors="replace",
        )
        output = result.stdout.strip() + result.stderr.strip()
        return result.returncode == 0, output
    except subprocess.TimeoutExpired:
        return False, f"TIMEOUT after {timeout}s"
    except Exception as e:
        return False, str(e)


def get_commit_hash(repo_path: Path) -> str | None:
    ok, out = run_git(["rev-parse", "--short", "HEAD"], cwd=repo_path)
    return out.strip() if ok and out else None


def is_remote_accessible(url: str) -> bool:
    """Check if remote is accessible using git ls-remote."""
    try:
        result = subprocess.run(
            ["git", "ls-remote", "--heads", url],
            capture_output=True, text=True, timeout=30,
            encoding="utf-8", errors="replace"
        )
        return result.returncode == 0
    except Exception:
        return False


# ──────────────────────────────────────────────────────────────
# Clone / Update Logic
# ──────────────────────────────────────────────────────────────
def clone_repo(repo: dict, dry_run: bool = False) -> dict:
    """Clone a repo that doesn't exist locally yet."""
    local_path = REPOS_ROOT / repo["local_path"]
    url = repo["url"]
    name = repo["name"]

    log(f"Cloning {name} from {url}...")

    if dry_run:
        log(f"[DRY-RUN] Would clone {url} → {local_path}")
        return {**repo, "status": "DRY_RUN"}

    # Check remote accessibility first
    if not is_remote_accessible(url):
        log(f"Remote inaccessible for {name} — repo may not exist or be private.", "WARN")
        return {**repo, "status": ERROR_STATUS, "last_sync": _now()}

    local_path.mkdir(parents=True, exist_ok=True)
    ok, out = run_git(["clone", "--depth=1", url, "."], cwd=local_path, timeout=180)

    if ok:
        commit = get_commit_hash(local_path)
        log(f"[OK] Cloned {name} @ {commit}")
        return {**repo, "status": OK_STATUS, "last_sync": _now(), "commit_hash": commit}
    else:
        # If clone failed, remove empty dir to keep clean state
        try:
            if local_path.exists() and not any(local_path.iterdir()):
                local_path.rmdir()
        except Exception:
            pass
        log(f"[ERROR] Clone failed for {name}: {out[:200]}", "ERROR")
        return {**repo, "status": ERROR_STATUS, "last_sync": _now()}


def update_repo(repo: dict, dry_run: bool = False) -> dict:
    """Pull latest changes for a repo that already exists locally."""
    local_path = REPOS_ROOT / repo["local_path"]
    name = repo["name"]
    url = repo["url"]

    # If repo is COLD_SNAPSHOT_LOCKED, don't touch it
    if repo.get("status") == COLD_SNAPSHOT_STATUS:
        log(f"[COLD] {name} is COLD_SNAPSHOT_LOCKED — skipping remote sync, local preserved.")
        return repo

    log(f"Updating {name}...")

    if dry_run:
        log(f"[DRY-RUN] Would pull {name}")
        return repo

    # Check remote accessibility
    if not is_remote_accessible(url):
        log(f"[COLD] Remote for {name} is gone/private — locking as Cold Snapshot.", "WARN")
        return {**repo, "status": COLD_SNAPSHOT_STATUS, "last_sync": _now()}

    # Fetch + pull
    ok_fetch, _ = run_git(["fetch", "--depth=1", "origin"], cwd=local_path)
    ok_pull, out_pull = run_git(["pull", "--ff-only", "origin"], cwd=local_path, timeout=120)

    if ok_pull or ok_fetch:
        commit = get_commit_hash(local_path)
        log(f"[OK] Updated {name} @ {commit}")
        return {**repo, "status": OK_STATUS, "last_sync": _now(), "commit_hash": commit}
    else:
        log(f"[WARN] Pull failed for {name}: {out_pull[:200]}", "WARN")
        return {**repo, "status": ERROR_STATUS, "last_sync": _now()}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


# ──────────────────────────────────────────────────────────────
# Main Sync Loop
# ──────────────────────────────────────────────────────────────
def sync_all(filter_name: str | None = None, dry_run: bool = False, clone_only: bool = False) -> None:
    manifest = load_manifest()
    repos = manifest.get("repositories", [])
    history = load_history()

    if filter_name:
        repos = [r for r in repos if r["name"].lower() == filter_name.lower()]
        if not repos:
            log(f"[ERROR] Repo '{filter_name}' not found in manifest.", "ERROR")
            sys.exit(1)

    results = []
    ok_count = 0
    cold_count = 0
    error_count = 0

    for repo in repos:
        local_path = REPOS_ROOT / repo["local_path"]
        git_dir = local_path / ".git"

        if git_dir.exists():
            if clone_only:
                log(f"[SKIP] {repo['name']} already cloned (--clone-only mode)")
                results.append(repo)
                continue
            updated = update_repo(repo, dry_run=dry_run)
        else:
            updated = clone_repo(repo, dry_run=dry_run)

        results.append(updated)

        status = updated.get("status", "UNKNOWN")
        if status == OK_STATUS:
            ok_count += 1
        elif status == COLD_SNAPSHOT_STATUS:
            cold_count += 1
        elif status == ERROR_STATUS:
            error_count += 1

    # Update manifest with new statuses
    manifest["repositories"] = results
    manifest["meta"]["last_sync"] = _now()
    if not dry_run:
        save_manifest(manifest)

    # Record history entry
    history_entry = {
        "timestamp": _now(),
        "total": len(results),
        "ok": ok_count,
        "cold_snapshot": cold_count,
        "error": error_count,
        "dry_run": dry_run,
        "filter": filter_name,
    }
    history.append(history_entry)
    if not dry_run:
        save_history(history)

    # Summary
    print("\n" + "=" * 60)
    print(f"  SECOND BRAIN SYNC COMPLETE")
    print(f"  [OK]           OK:            {ok_count}")
    print(f"  [COLD]         Cold Snapshot: {cold_count}")
    print(f"  [ERROR]        Error:         {error_count}")
    print(f"  Total:            {len(results)}")
    print("=" * 60)

    if error_count > 0:
        print("\n⚠️  Some repos had errors. Check log:", LOG_PATH)


def show_status() -> None:
    manifest = load_manifest()
    repos = manifest.get("repositories", [])
    print(f"\n{'NAME':<35} {'CATEGORY':<28} {'STATUS':<25} {'LAST SYNC'}")
    print("-" * 110)
    for r in repos:
        local_path = REPOS_ROOT / r["local_path"]
        exists = "[local]" if (local_path / ".git").exists() else "[not cloned]"
        status = r.get("status", "PENDING")
        last = r.get("last_sync", "never")
        if last and len(last) > 19:
            last = last[:19]
        print(f"{r['name']:<35} {r['category']:<28} {status+' '+exists:<35} {last}")


# ──────────────────────────────────────────────────────────────
# CLI Entry Point
# ──────────────────────────────────────────────────────────────
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Second Brain Hub — Auto-Sync Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--repo", help="Sync only a specific repo by name")
    parser.add_argument("--dry-run", action="store_true", help="Simulate without executing git commands")
    parser.add_argument("--clone-only", action="store_true", help="Only clone repos that are not yet local")
    parser.add_argument("--status", action="store_true", help="Show status table of all repos")
    args = parser.parse_args()

    if args.status:
        show_status()
        return

    log("=" * 50)
    log("Second Brain Hub — Sync Engine starting")
    log(f"Manifest: {MANIFEST_PATH}")
    log(f"Repos root: {REPOS_ROOT}")
    log(f"Dry run: {args.dry_run} | Clone only: {args.clone_only}")
    log("=" * 50)

    sync_all(
        filter_name=args.repo,
        dry_run=args.dry_run,
        clone_only=args.clone_only,
    )


if __name__ == "__main__":
    main()
