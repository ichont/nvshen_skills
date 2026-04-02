#!/usr/bin/env python3
"""Version management for generated goddess skills."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from datetime import datetime


CORE_FILES = ["memory.md", "persona.md", "SKILL.md", "meta.json"]


def backup(base_dir: str, slug: str) -> str:
    skill_dir = os.path.join(base_dir, slug)
    versions_dir = os.path.join(skill_dir, "versions")
    meta_path = os.path.join(skill_dir, "meta.json")

    if not os.path.exists(meta_path):
        print("meta.json not found", file=sys.stderr)
        sys.exit(1)

    with open(meta_path, "r", encoding="utf-8") as fh:
        meta = json.load(fh)

    current_version = meta.get("version", "v0")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{current_version}_{timestamp}"
    backup_dir = os.path.join(versions_dir, backup_name)
    os.makedirs(backup_dir, exist_ok=True)

    for filename in CORE_FILES:
        src = os.path.join(skill_dir, filename)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(backup_dir, filename))

    print(f"Backed up to: {backup_dir}")
    return backup_name


def rollback(base_dir: str, slug: str, version: str) -> None:
    skill_dir = os.path.join(base_dir, slug)
    versions_dir = os.path.join(skill_dir, "versions")

    if not os.path.isdir(versions_dir):
        print("No version history found", file=sys.stderr)
        sys.exit(1)

    target_dir = None
    for name in os.listdir(versions_dir):
        if name == version or name.startswith(version):
            target_dir = os.path.join(versions_dir, name)
            break

    if not target_dir:
        print(f"Version not found: {version}", file=sys.stderr)
        list_versions(base_dir, slug)
        sys.exit(1)

    backup(base_dir, slug)

    for filename in CORE_FILES:
        src = os.path.join(target_dir, filename)
        dst = os.path.join(skill_dir, filename)
        if os.path.exists(src):
            shutil.copy2(src, dst)

    print(f"Rolled back to: {version}")


def list_versions(base_dir: str, slug: str) -> None:
    versions_dir = os.path.join(base_dir, slug, "versions")

    if not os.path.isdir(versions_dir):
        print("No version history found.")
        return

    versions = sorted(os.listdir(versions_dir), reverse=True)
    if not versions:
        print("No version history found.")
        return

    print(f"Versions for {slug}:\n")
    for version in versions:
        print(f"  {version}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Version manager for goddess skills")
    parser.add_argument("--action", required=True, choices=["backup", "rollback", "list"])
    parser.add_argument("--slug", required=True, help="Skill slug")
    parser.add_argument("--base-dir", default="./goddesses", help="Base directory")
    parser.add_argument("--version", help="Version to roll back to")
    args = parser.parse_args()

    if args.action == "backup":
        backup(args.base_dir, args.slug)
    elif args.action == "rollback":
        if not args.version:
            print("--version is required for rollback", file=sys.stderr)
            sys.exit(1)
        rollback(args.base_dir, args.slug, args.version)
    elif args.action == "list":
        list_versions(args.base_dir, args.slug)


if __name__ == "__main__":
    main()
