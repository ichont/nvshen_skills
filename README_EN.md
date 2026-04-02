# goddess.skill

Generate a runnable “goddess persona” AI Skill from a short brief, chat snippets, screenshots, or scene notes.

Compatible with both Claude Code and Codex.

## What it does

This repo turns a loose vibe such as “aloof, unreadable, barely replies, but occasionally soft” into a structured, reusable persona Skill.

Each generated persona supports two attitude modes:

- `normal`: the default cool / distant / selective style
- `wake-up`: a sharper, tougher mode meant to snap the user out of fixation, not to devolve into unrestricted abuse

It supports blended archetypes such as:

- Ice queen
- Dismissive / avoidant
- Tsundere
- Kuudere
- Queen / dominant
- Hot-and-cold

## Install

### Claude Code

```bash
mkdir -p .claude/skills
git clone https://github.com/han12580/goddess-skill .claude/skills/create-goddess
```

### Codex

Codex auto-discovers skills from `$CODEX_HOME/skills`, or `~/.codex/skills` when `CODEX_HOME` is unset.

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/han12580/goddess-skill "${CODEX_HOME:-$HOME/.codex}/skills/create-goddess"
```

## Use

Invoke:

```text
/create-goddess
```

Then provide:

1. Codename
2. Scene or role
3. Archetypes and speaking style
4. Optional raw material

Generated skills are written to:

```text
goddesses/{slug}/
```

After installing into Codex, restart Codex so the new skill is picked up.

## Output files

- `memory.md`: context memory and interaction fuel
- `persona.md`: layered persona rules
- `meta.json`: metadata and version info
- `SKILL.md`: final runnable skill

## Mode switching

Generated skills should support:

- `normal`
- `wake-up`

Example triggers:

- `switch to normal`
- `switch to wake-up`
- `wake me up`
- `be harsher`

## Safety

- Intended for fictional personas or consented roleplay
- Not intended for impersonating real people
- Cool, distant, and difficult personas are supported
- Explicit harassment or coercive manipulation is not the goal
- `wake-up` mode should aim for clarity and detachment, not slurs, threats, or dehumanizing abuse

## Copyright

- New structure, rewritten prompts, persona system changes, and later modifications are copyright `han12580`
- Upstream MIT licensing notice remains because this repository evolved from an MIT-licensed project
- See [COPYRIGHT.md](COPYRIGHT.md) for the repository lineage and attribution boundary

## Repository

[han12580/goddess-skill](https://github.com/han12580/goddess-skill)
