# Copilot instructions and skills

Personal agent guidance and portable skills for focused implementation, UX review, and clear pull requests.

## Why

Use one Git checkout as the source for personal skills on Windows and macOS. Installed links read directly from the checkout, so pulling updates changes the linked skills without copying them again.

This collection includes `github-spot-illustration`, `implement-prototype`, `request-pr-review`, `subtle-svg-animation`, and `ux-review`. The GitHub illustration skill includes guidance, not official artwork. Work-specific skills, managed app/plugin skills, and illustration asset libraries are intentionally excluded.

## Quickstart

Prerequisites: Git, Python 3.9 or newer, and a Copilot client that supports personal skills in `~/.copilot/skills`. This repository is public; authentication is not required to clone it.

Clone outside OneDrive or other file-sync folders on each device:

```shell
git clone https://github.com/unthinkmedia/copilot-instructions.git
cd copilot-instructions
```

Preview installation on macOS:

```shell
python3 scripts/install_skills.py
```

On Windows, use `python` instead of `python3`. The preview lists the skill links that would be installed; it does not change installed skills.

Install after reviewing the preview:

```shell
python3 scripts/install_skills.py --apply --replace
```

Existing copies of the included skills are moved to a timestamped folder under `~/.copilot/skill-backups` before replacement. Other skills remain untouched. Windows uses directory junctions; macOS uses symbolic links. For a different client location, supply `--skills-dir "<path>"`.

Start a new client session and check its available skills or command picker. Skill discovery and slash-command support depend on the client; GitHub sign-in alone does not install skills in cloud products.

Before working on either device:

```shell
git pull --ff-only
```

Edit skills in this checkout, then commit and push intentional changes. Pull on the other device before using them. Sync is explicit, not instant or scheduled; stop and reconcile conflicting edits rather than overwriting them.

Copy `AGENTS.md` into a product repository only when you want its baseline there. Paste the numbered rules from `assisted-approval.md` and the four `agent-merge-*.md` files into their matching app settings fields. Those copied instructions and settings do not update through the skill links.

To share the collection, send the repository URL. Anyone can view and clone its published contents and history. Review permissions before adding any work-derived material, private references, or third-party assets.
