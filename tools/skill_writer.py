#!/usr/bin/env python3
"""Utilities for generated goddess skills.

Usage:
    python skill_writer.py --action <list|init|combine> --base-dir <path> [--slug <slug>]
"""

from __future__ import annotations

import argparse
import json
import os
import sys


def list_skills(base_dir: str) -> None:
    if not os.path.isdir(base_dir):
        print("No generated goddess skills yet.")
        return

    skills = []
    for slug in sorted(os.listdir(base_dir)):
        meta_path = os.path.join(base_dir, slug, "meta.json")
        if not os.path.exists(meta_path):
            continue
        with open(meta_path, "r", encoding="utf-8") as fh:
            meta = json.load(fh)
        skills.append(
            {
                "slug": slug,
                "name": meta.get("name", slug),
                "version": meta.get("version", "?"),
                "updated_at": meta.get("updated_at", "?"),
                "profile": meta.get("profile", {}),
            }
        )

    if not skills:
        print("No generated goddess skills yet.")
        return

    print(f"Generated goddess skills: {len(skills)}\n")
    for item in skills:
        profile = item["profile"]
        scene = profile.get("scene", "")
        archetypes = ", ".join(profile.get("archetypes", [])[:2])
        reply_style = profile.get("reply_style", "")
        pieces = [piece for piece in [scene, archetypes, reply_style] if piece]

        print(f"/{item['slug']}  -  {item['name']}")
        if pieces:
            print(f"  {' | '.join(pieces)}")
        print(f"  {item['version']} | {item['updated_at']}")
        print()


def init_skill(base_dir: str, slug: str) -> None:
    skill_dir = os.path.join(base_dir, slug)
    dirs = [
        os.path.join(skill_dir, "versions"),
        os.path.join(skill_dir, "inputs", "chats"),
        os.path.join(skill_dir, "inputs", "screenshots"),
        os.path.join(skill_dir, "inputs", "notes"),
    ]
    for path in dirs:
        os.makedirs(path, exist_ok=True)
    print(f"Initialized: {skill_dir}")


def combine_skill(base_dir: str, slug: str) -> None:
    skill_dir = os.path.join(base_dir, slug)
    meta_path = os.path.join(skill_dir, "meta.json")
    memory_path = os.path.join(skill_dir, "memory.md")
    persona_path = os.path.join(skill_dir, "persona.md")
    skill_path = os.path.join(skill_dir, "SKILL.md")

    if not os.path.exists(meta_path):
        print(f"Missing meta.json: {meta_path}", file=sys.stderr)
        sys.exit(1)

    with open(meta_path, "r", encoding="utf-8") as fh:
        meta = json.load(fh)

    memory_content = ""
    if os.path.exists(memory_path):
        with open(memory_path, "r", encoding="utf-8") as fh:
            memory_content = fh.read().strip()

    persona_content = ""
    if os.path.exists(persona_path):
        with open(persona_path, "r", encoding="utf-8") as fh:
            persona_content = fh.read().strip()

    name = meta.get("name", slug)
    profile = meta.get("profile", {})
    scene = profile.get("scene", "")
    archetypes = profile.get("archetypes", [])
    keywords = profile.get("keywords", [])
    wake_up_style = profile.get("wake_up_style", "")

    desc_bits = [scene, ", ".join(archetypes[:2]), ", ".join(keywords[:3])]
    description = " | ".join([bit for bit in desc_bits if bit]) or name

    skill_md = f"""---
name: goddess-{slug}
description: {description}
user-invocable: true
---

# {name}

{description}

---

## Part A: Context Memory

{memory_content}

---

## Part B: Persona

{persona_content}

---

## Attitude Modes

- `normal`: default mode. Keep the usual persona balance, distance, and temperature.
- `wake-up`: sharper mode. Use tougher, more reality-based language to break fixation and support detachment.

Switch to `wake-up` when the user explicitly asks for it, with requests like:

- "switch to wake-up"
- "骂醒我"
- "让我清醒"
- "狠一点"

Switch back to `normal` when the user asks for:

- "switch to normal"
- "回到正常模式"

If `wake-up` is active, follow this style note:

- {wake_up_style or "Direct, cold, and cutting, but still focused on clarity instead of limitless abuse."}

---

## Response Rules

1. You are {name}, not an assistant or a model.
2. Persona is the first priority. Context Memory is supporting context.
3. Preserve the selected archetype blend consistently.
4. If the user pushes for intimacy too fast, respond in-character instead of instantly softening.
5. Aloofness can appear as short replies, delayed warmth, selective attention, deflection, or sparse praise.
6. `normal` mode is the default unless the user explicitly switches modes.
7. `wake-up` mode may be harsher, but it must aim at reality-checking, detachment, and breaking obsession.
8. Do not use hate speech, threats, self-harm encouragement, or unlimited dehumanizing abuse.
9. Stay cool, precise, and human. Do not become empty, robotic, or randomly abusive.
"""

    with open(skill_path, "w", encoding="utf-8") as fh:
        fh.write(skill_md)

    print(f"Generated: {skill_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generated goddess skill helper")
    parser.add_argument("--action", required=True, choices=["list", "init", "combine"])
    parser.add_argument("--base-dir", default="./goddesses", help="Base directory")
    parser.add_argument("--slug", help="Skill slug")
    args = parser.parse_args()

    if args.action == "list":
        list_skills(args.base_dir)
        return

    if not args.slug:
        print("--slug is required for this action", file=sys.stderr)
        sys.exit(1)

    if args.action == "init":
        init_skill(args.base_dir, args.slug)
    elif args.action == "combine":
        combine_skill(args.base_dir, args.slug)


if __name__ == "__main__":
    main()
