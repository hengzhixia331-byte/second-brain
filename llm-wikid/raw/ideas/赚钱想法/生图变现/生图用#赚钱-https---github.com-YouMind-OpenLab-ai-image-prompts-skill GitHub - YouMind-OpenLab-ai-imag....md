---
description: 生图用#赚钱 https://github.com/YouMind-OpenLab/ai-image-prompts-skill/
author: unknown
source: GitHub
url: https://github.com/YouMind-OpenLab/ai-image-prompts-skill
saved: 2026-07-01
tags:
  - 笔记同步助手
id: 398e9b79-879e-4893-95b7-b3a1f9aa2435
---

# GitHub - YouMind-OpenLab/ai-image-prompts-skill: AI Image Prompts — 10,000+ curated prompts for any model. Works with Nano Banana Pro, Nano Banana 2, Seedream 5.0, GPT Image 1.5, Midjourney, DALL-E, Flux, Stable Diffusion, and more.
#笔记同步助手
## 来源
[原文链接](https://github.com/YouMind-OpenLab/ai-image-prompts-skill)
## 正文
![[llm-wikid/raw/assets/images/67c3c1a14896b3d69765e7ccb1ce168a_MD5.svg|Prompts]] ![[llm-wikid/raw/assets/images/48cc3833aa8d06b7fb4b41327dfea4eb_MD5.svg|OpenClaw]] ![[llm-wikid/raw/assets/images/8d6e69ec488ac0437a36fb0bb0a4d445_MD5.svg|Claude Code]] ![[llm-wikid/raw/assets/images/687bc26c35b3caefdfb85f185224ef90_MD5.svg|Daily Updates]] ![[llm-wikid/raw/assets/images/387a19b994df8ab29ce135115f0b25bb_MD5.svg|Multi-language]] ![[llm-wikid/raw/assets/images/2ab89154b201f68d496aef14569d1962_MD5.svg|License]]

> **Stop spending hours hunting for the right AI image prompt.** Tell your AI assistant what you need in one sentence — it searches 10,000+ curated prompts and returns the top 3 matches with sample images, ready to use with any model.
> 
> 🖼️ [Browse the Prompt Gallery →](https://youmind.com/nano-banana-pro-prompts)

## What Is This?

[](#what-is-this)

An **AI agent skill** that gives Claude, OpenClaw, Cursor, and other AI assistants the ability to intelligently search a curated library of **10,000+ image generation prompts**, recommend the best matches for your use case, and even customize prompts based on your content.

These prompts are **model-agnostic** — they work with:

-   🍌 **Nano Banana Pro** & **Nano Banana 2** (Google Gemini image generation)
-   🎨 **Seedream 5.0** (ByteDance's latest image model)
-   🖼️ **GPT Image 1.5** (OpenAI's newest image model)
-   ✨ **Midjourney**, **DALL-E 3**, **Flux**, **Stable Diffusion**, and more

High-quality prompts are the key to great results — regardless of which model you use.

## Why Use This Skill?

[](#why-use-this-skill)

-   ✅ **10,000+ prompts, organized by use case** — not a random dump, but professionally categorized
-   ✅ **Every prompt includes sample images** — see the result before you copy
-   ✅ **Smart semantic search** — describe what you need, the AI finds the match
-   ✅ **Content remix mode** — paste your article or video script, get a custom prompt
-   ✅ **Updated twice daily** — always reflects the latest viral prompts from the community
-   ✅ **Multi-language** — responds in your language, always provides English prompt for generation

---

## Installation

[](#installation)

### OpenClaw (Recommended)

[](#openclaw-recommended)

```
clawhub install ai-image-prompts
```

Or search inside OpenClaw chat:

> "Install the ai image prompts skill from clawhub"

### Claude Code

[](#claude-code)

```
npx skills i YouMind-OpenLab/ai-image-prompts-skill
```

### Other AI Assistants (Cursor, Codex, Gemini CLI, Windsurf)

[](#other-ai-assistants-cursor-codex-gemini-cli-windsurf)

```
# Universal installer — auto-detects your AI assistant
npx skills i YouMind-OpenLab/ai-image-prompts-skill
```

### Manual / openskills

[](#manual--openskills)

```
npx openskills install YouMind-OpenLab/ai-image-prompts-skill
```

---

## How to Use

[](#how-to-use)

### Mode 1: Direct Search

[](#mode-1-direct-search)

Just describe what you need:

```
"Find me a cyberpunk-style avatar prompt"
"I need prompts for travel blog article covers"
"Looking for a product photo on white background"
"Help me find a YouTube thumbnail for a tech review video"
```

You'll get up to 3 recommendations with:

-   Translated title & description (in your language)
-   Truncated prompt preview + link to full prompt
-   Sample image showing the result
-   One-click customization option

### Mode 2: Content Illustration

[](#mode-2-content-illustration)

Provide your content and let the AI find matching visual styles:

```
"Here's my article about remote work productivity. Find me a good cover image prompt."
[paste article text]
```

The skill will:

1.  Analyze your content's theme, tone, and audience
2.  Search for matching prompt templates
3.  Let you pick a style
4.  Remix the prompt with your specific content details

---

## Categories

[](#categories)

Prompts are organized into 11 use-case categories:

| Category | Count | Use For |
| --- | --- | --- |
| Social Media Post | 6,382 | Twitter, Instagram, LinkedIn visuals |
| Product Marketing | 3,709 | Ads, promo banners, marketing materials |
| Profile / Avatar | 1,064 | Profile pictures, AI portraits, headshots |
| Poster / Flyer | 485 | Event posters, flyers, announcements |
| Infographic / Edu Visual | 458 | Data visualizations, educational graphics |
| E-commerce Main Image | 382 | Product photos, listing images |
| Game Asset | 378 | Game sprites, characters, environments |
| Comic / Storyboard | 290 | Comics, manga, visual storytelling |
| YouTube Thumbnail | 173 | Video thumbnails, channel art |
| App / Web Design | 167 | UI mockups, app screenshots, web design |
| Uncategorized | 910+ | Everything else — landscapes, abstract, experimental |

---

## Data Source

[](#data-source)

All prompts are curated from the open community by [YouMind.com](https://youmind.com/) — sourced from real creators sharing their best image generation results on social media. Each prompt includes the actual generated image as a sample.

The library is updated **twice daily** via GitHub Actions, syncing with the latest community contributions.

---

## Keep Prompts Fresh

[](#keep-prompts-fresh)

The skill auto-checks for updates on each use. To manually sync:

```
# Check if update needed (silent if fresh)
node scripts/setup.js --check

# Force update all references
pnpm run sync
```

---

## License

[](#license)

MIT — prompts are community-sourced and free to use.

---

Curated with ❤️ by [YouMind.com](https://youmind.com/)

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/1685dbf1_1782885898764?u=https%3A%2F%2Fgithub.com%2FYouMind-OpenLab%2Fai-image-prompts-skill&s=obsidian)
