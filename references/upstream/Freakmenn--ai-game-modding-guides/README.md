# AI Game Modding Guides

Beginner guides for two kinds of project, both built with an AI coding agent:

- **Passthrough mods:** two games running at once and linked together, like SkyCraft (Minecraft inside Skyrim).
- **Rust rewrites and ports:** rebuilding a game's engine in Rust so it reads data from your own copy, like hl2-rs.

These guides answer the questions people asked on the Discord. If something is missing or wrong, [open an issue](CONTRIBUTING.md) or send a pull request.
Also do note that everyone has their own methods/prompting style and workflows, it will probably be impossible to cover everything so take the methods used in the guides with a grain of salt and use it to create your own Methods

[![Licence: MIT](https://img.shields.io/badge/Licence-MIT-green.svg)](LICENSE)
[![Contributing welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Discord](https://img.shields.io/badge/Discord-join%20the%20server-5865F2?logo=discord&logoColor=white)](https://discord.gg/ccFpNC26Ts)
[![Single-player and offline games only](https://img.shields.io/badge/scope-single-player%20%26%20offline%20games%20you%20own-lightgrey.svg)](guides/06-rules-legal-and-publishing.md)

> **Status:** draft. Tools, models, plan limits, and mod loaders change fast. Verify a detail before you rely on it.
>
> **Single-player and offline games you own only.** Nothing here covers anti-cheat, DRM, or online play. Rocket League works offline with anti-cheat off; see [the rules](guides/06-rules-legal-and-publishing.md).
>
> **Windows.** Every example project here targets Windows. hl2-rs says other systems are unverified.

## Start here

Never done this before? Read **[Start here](guides/00-start-here.md)**.

Want an answer rather than a read? Go to the **[FAQ](guides/07-faq.md)**.

## The short version

1. **Use an AI agent, not a chat website.** An agent (Claude Code, Codex, OpenCode, and others) runs on your PC, reads your game folders, writes files, and runs builds. A browser chat can't do that.
2. **Check whether your game has a mod loader.** This decides whether your idea is realistic. See [guide 8](guides/08-mod-loaders-and-script-extenders.md).
3. **Install the games first.** The agent finds the files itself, so you don't upload anything.
4. **Point it at an example project** (SkyCraft for passthrough, hl2-rs for rewrites) and tell it what you want.
5. **Expect many rounds.** The first prompt rarely finishes the job. You playtest, report what happened, and the agent fixes it.
6. **Never commit game files.** Your repo holds your code only. Players use their own copies.

## Guides

| # | Guide | Read it if |
|---|-------|-----------|
| 0 | [Start here](guides/00-start-here.md) | You have never done this before |
| 1 | [Choosing and setting up an AI agent](guides/01-choose-and-set-up-an-ai-agent.md) | You don't know which tool or model to use, or what it costs |
| 2 | [Passthrough mods](guides/02-passthrough-mods.md) | You want to link two games |
| 3 | [Rust rewrites and ports](guides/03-rust-rewrites-and-ports.md) | You want to rebuild a game's engine |
| 4 | [Prompting and workflow](guides/04-prompting-and-workflow.md) | You want to know what to say and how to keep a project on track |
| 5 | [Testing and troubleshooting](guides/05-testing-and-troubleshooting.md) | Something broke, or the AI is stuck |
| 6 | [Rules, legal, and publishing](guides/06-rules-legal-and-publishing.md) | Before you share anything |
| 7 | [FAQ](guides/07-faq.md) | Quick answers to the most common questions |
| 8 | [Mod loaders and script extenders](guides/08-mod-loaders-and-script-extenders.md) | You need to know what you can install, or whether your idea is possible |
| 9 | [Worked example: a passthrough mod, start to finish](guides/09-worked-example-passthrough-mod.md) | You want the whole process with the actual prompts |
| 10 | [Posting your project](guides/10-posting-your-project.md) | You've got something that runs and want people to use it |

## Templates

Drop these into your own project.

- [`templates/AGENTS-starter.md`](templates/AGENTS-starter.md): a rules file that makes the agent follow your rules every session
- [`templates/STATUS-handoff.md`](templates/STATUS-handoff.md): the note you give a fresh chat when the old one gets stuck
- [`templates/MODLOG-template.md`](templates/MODLOG-template.md): a running log of what changed and what was tested
- [`templates/workflow-writeup.md`](templates/workflow-writeup.md): for sharing how you made your project

## Examples worth studying

| Project | What it shows |
|---------|---------------|
| [SkyCraft](https://github.com/chasmlol/SkyCraft) | Passthrough: Minecraft inside Skyrim (script extender plugin + Fabric mod) |
| [FalloutCraft](https://github.com/zeyvu/FalloutCraft) | Passthrough: SkyCraft's design reused for Fallout 4 |
| [OWCraft](https://github.com/Yaekai/OWCraft) | Passthrough: SkyCraft's design reused for Outer Wilds, with a development log and design doc |
| [GTA San AnSkateas](https://github.com/ryglizzy/GTA-San-AnSkateas) | Skate 3's engine running inside GTA San Andreas |
| [2010 Rust Rewrite Mashup](https://github.com/chasmlol/2010-rust-rewrite-mashup) | A Rust rewrite combined with other games |
| [hl2-rs](https://github.com/kvalls/hl2-rs) | Rust rewrite of Half-Life 2, with an honest list of what's missing |
| [gang-beasts-rust](https://github.com/muffinmxn/gang-beasts-rust) | Rust/Bevy rewrite with Python extractors and a whitelist `.gitignore` |
| [benilla](https://github.com/samwhosung/benilla) | A large Rust/Bevy rewrite (a WoW 1.12.1 client) |
| [universal-modder](https://github.com/rehan-remade/universal-modder) | Skills and tools that guide an AI agent through modding a game |

Finished open-source engine reimplementations, if you want to see what the long game looks like: [OpenMW](https://github.com/OpenMW/openmw), [OpenRCT2](https://github.com/OpenRCT2/OpenRCT2), [OpenTTD](https://github.com/OpenTTD/OpenTTD).

## Who these guides are for

People who have never written code and want to try something anyway. You don't need to be a programmer to start, and you don't need Rust or reverse engineering either.

You do need to be willing to describe problems clearly and to spend most of your time playtesting and reporting back. That is the job.

You also need Windows. Every project these guides point at is Windows-only, and hl2-rs says other systems are unverified. On Linux, run the Windows build under Wine or Proton and expect to debug it yourself.

## Get help

Guides can only cover so much. For anything specific to your setup, ask in **#support-help** on the [chasm server](https://discord.gg/ccFpNC26Ts). That's where people post problems, and where the answers get turned into better guides.

Include your games and exact versions, the loaders, the agent and model, what you tried, and the logs. If the chat got stuck, the `STATUS.md` trick in [guide 4](guides/04-prompting-and-workflow.md#the-handoff-trick-for-stuck-chats) writes most of that for you.

Corrections to the guides themselves are better as a pull request. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Open questions

Nobody has settled these. If you know the answer, post it on the Discord:

- Does a detailed prompt or a short loose one work better? [Both camps are quoted here.](guides/04-prompting-and-workflow.md#the-prompting-debate-as-members-put-it)
- Which free model can finish a project?
- How do you handle Unreal Engine games?
- Can local models handle a real project on a 12 GB GPU?

## Contributing

Experienced developers are welcome. Technical write-ups, corrections, dead ends worth documenting, and workflow examples all help.

To fix a typo or a broken link, [edit the page on GitHub](CONTRIBUTING.md#how-to-contribute). You don't need to clone anything.

## Disclaimer

These are unofficial fan projects. They are not affiliated with or endorsed by any game's developer or publisher. Nothing here is legal advice.

Everything described here is for single-player and offline games that you own. Nothing in these guides covers anti-cheat, DRM, or online play.

## Licence and attribution

Guides: [MIT](LICENSE). Linked projects keep their own licences, so check each one before reusing its code.

If you write a guide based on one of these, credit it by name and keep its licence. FalloutCraft and OWCraft both credit SkyCraft that way.
