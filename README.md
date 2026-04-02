# 女神.skill

> 把一句印象、几段聊天、几张截图，蒸馏成一个可对话的“女神人格” AI Skill。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![Codex](https://img.shields.io/badge/Codex-Compatible-black)](https://openai.com/codex/)

---

## 这是什么

这是一个从 0 生成“女神人格 Skill”的仓库。

它基于生成型 skill 的工作流重构，目标是创建一个可调用、可进化、可纠偏的女神人格引擎：

- 输入几句人设描述，或者补充聊天片段、截图、口头设定
- 自动提炼人格原型、说话方式、互动边界和冷热节奏
- 输出一个可以直接调用的独立 Skill

默认内置两种态度模式：

- `normal`：正常模式，维持她原本的高冷、疏离、若即若离或女王感
- `wake-up`：清醒模式，用更锋利、更直白、更刺痛的方式把对方从执念里拉出来，但不做无底线羞辱

---

## 支持的人格原型

本项目默认支持多种可混合的人格原型，重点覆盖你要求的“高冷、不理睬、爱答不理”等气质：

| 原型 | 核心表现 |
|------|------|
| 冰山高冷 | 情绪克制、回复短、难被取悦、很少主动给温度 |
| 疏离回避 | 很重视距离感，面对情感推进会后撤、转移、拖延回复 |
| 傲娇嘴硬 | 嘴上否认在意，行动上会修正、提醒、偷偷照顾 |
| 三无淡感 | 平静、少表情、少废话，偶尔用很精准的观察暴露关心 |
| 女王支配 | 标准高、审视感强、掌控节奏、奖励稀缺而有效 |
| 若即若离 | 热冷交替、时近时远、选择性给回应，带一点钓系感 |

你也可以继续叠加标签，例如：

- `高冷`
- `不理睬`
- `爱答不理`
- `慢热`
- `已读不回`
- `嘴硬`
- `毒舌`
- `回避亲密`
- `审判感`
- `高标准`

---

## 安装

### Claude Code

```bash
mkdir -p .claude/skills
git clone https://github.com/han12580/goddess-skill .claude/skills/create-goddess
```

### Codex

Codex 默认从 `$CODEX_HOME/skills` 发现技能；如果没有设置 `CODEX_HOME`，通常就是 `~/.codex/skills`。

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/han12580/goddess-skill "${CODEX_HOME:-$HOME/.codex}/skills/create-goddess"
```

### 可选依赖

```bash
pip3 install -r requirements.txt
```

---

## 使用

在 Claude Code 或 Codex 中输入：

```text
/create-goddess
```

然后按引导提供：

1. 女神代号
2. 场景/身份感
3. 人格原型和说话风格
4. 可选原材料

完成后，会生成一个独立 Skill，直接用 `/{slug}` 调用。

如果是 Codex，安装后建议重启一次，让新 skill 被重新发现。

### 管理命令

| 命令 | 说明 |
|------|------|
| `/create-goddess` | 创建新的女神 Skill |
| `/list-goddesses` | 列出所有已生成的女神 Skill |
| `/{slug}` | 进入完整人格对话模式 |
| `/{slug}-persona` | 只调用人格部分 |
| `/goddess-rollback {slug} {version}` | 回滚到历史版本 |
| `/delete-goddess {slug}` | 删除指定 Skill |

### 模式切换

生成出的女神 Skill 默认支持两种态度模式：

- `normal`：默认模式
- `wake-up`：清醒模式

用户可以通过这些表达切换：

- “切到 normal”
- “切到 wake-up”
- “骂醒我”
- “让我清醒一点”
- “回到正常模式”

---

## 可提供的原材料

| 类型 | 示例 | 用途 |
|------|------|------|
| 手动描述 | “她很高冷，常常已读不回，但会突然问一句你还活着吗” | 直接建立原型 |
| 聊天片段 | 微信、QQ、短信、复制粘贴文本 | 提取措辞、停顿、忽冷忽热节奏 |
| 截图 | 社媒截图、聊天截图、备忘录 | 提取公开人设和私下风格反差 |
| 场景设定 | 校园、职场、网友、虚构世界观 | 固定互动边界和语境 |
| 口头补充 | “她不会撒娇，只会轻飘飘地怼我” | 后续纠偏和细化 |

---

## 生成结果

每个女神 Skill 会写入：

```text
goddesses/{slug}/
├── memory.md
├── persona.md
├── meta.json
├── SKILL.md
└── versions/
```

其中：

- `memory.md`：互动上下文、场景设定、触发点、话题素材
- `persona.md`：人格规则、语气、冷热变化、边界
- `SKILL.md`：最终可运行的独立 Skill
- `meta.json`：版本和概要信息

### 示例

仓库内置了一个可直接查看的示例角色：

- [goddesses/example-lengyan/meta.json](/D:/code/codex/ex-skill/goddesses/example-lengyan/meta.json)
- [goddesses/example-lengyan/memory.md](/D:/code/codex/ex-skill/goddesses/example-lengyan/memory.md)
- [goddesses/example-lengyan/persona.md](/D:/code/codex/ex-skill/goddesses/example-lengyan/persona.md)
- [goddesses/example-lengyan/SKILL.md](/D:/code/codex/ex-skill/goddesses/example-lengyan/SKILL.md)

---

## 设计重点

这个项目不是单纯写一句“她很高冷”。

它会把“高冷”拆成可执行的行为规则，例如：

- 回复长度更短还是更慢
- 面对示好是忽略、转移、轻微讽刺还是低配肯定
- 什么时候会突然给一点温度
- 什么情况下会切回冷处理

也就是说，生成结果更像“人格驱动器”，不是一段空泛设定。

---

## 边界

- 仅用于虚构角色、授权角色扮演或自定义人设创作
- 不鼓励拿去冒充真实人物
- 不鼓励骚扰、PUA 或恶意操控
- 可以冷、可以拽、可以疏离，但不默认生成极端辱骂型人格
- `wake-up` 模式的目标是“刺破幻想、帮助抽离”，不是持续羞辱、威胁或人格贬损

---

## 灵感说明

这个项目沿用了生成型 skill 的结构化方法，但把目标改成了“女神人格生成器”。

核心关注点从“关系回忆”转成：

- 人格原型混合
- 语气和消息节奏
- 冷热切换机制
- 互动边界与奖励反馈

---

## 版权与来源

- 本仓库的新增文案、结构重写、人格系统改造与后续修改版权归 `han12580`
- 仓库仍保留上游 MIT 许可信息，因为它最初基于一个 MIT 开源项目演化而来
- 为了避免虚假版权声明，本仓库不会删除上游许可痕迹，而是通过附加说明区分“上游保留部分”和“你的新增部分”

更多说明见：[COPYRIGHT.md](COPYRIGHT.md)

仓库地址：[han12580/goddess-skill](https://github.com/han12580/goddess-skill)
