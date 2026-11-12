"""Preview or link repository skills into a client's personal skill directory."""

import argparse
import os
from pathlib import Path
import subprocess
import sys
from datetime import datetime
from uuid import uuid4


def resolved_target(path):
    return path.resolve(strict=True)


def create_link(source, destination):
    if os.name == "nt":
        env = dict(os.environ, SKILL_SOURCE=str(source), SKILL_DEST=str(destination))
        subprocess.run(
            [
                "powershell.exe",
                "-NoProfile",
                "-NonInteractive",
                "-Command",
                "$ErrorActionPreference = 'Stop'; "
                "New-Item -ItemType Junction -Path $env:SKILL_DEST "
                "-Target $env:SKILL_SOURCE | Out-Null",
            ],
            env=env,
            check=True,
        )
    else:
        destination.symlink_to(source, target_is_directory=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skills-dir", type=Path, default=Path.home() / ".copilot" / "skills")
    parser.add_argument("--apply", action="store_true", help="Create links; default is preview only")
    parser.add_argument("--replace", action="store_true", help="Back up conflicting copies before linking")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    source_root = root / ".github" / "skills"
    destination_root = args.skills_dir.expanduser().absolute()
    if not source_root.is_dir():
        parser.error(f"Skill source directory is missing: {source_root}")
    if destination_root.exists() and not destination_root.is_dir():
        parser.error(f"Destination is not a directory: {destination_root}")
    source_resolved = source_root.resolve()
    destination_resolved = destination_root.resolve()
    if (
        source_resolved == destination_resolved
        or source_resolved in destination_resolved.parents
        or destination_resolved in source_resolved.parents
    ):
        parser.error("Source and destination skill directories must not overlap.")

    pending = []
    conflicts = []
    for source in sorted(source_root.iterdir()):
        if not source.is_dir() or not (source / "SKILL.md").is_file():
            continue
        destination = destination_root / source.name
        occupied = os.path.lexists(destination)
        if occupied and destination.exists() and resolved_target(destination) == source.resolve():
            print(f"Already linked: {source.name}")
            continue
        pending.append((source, destination, occupied))
        if occupied:
            conflicts.append(destination)
        print(f"{'Back up and link' if occupied else 'Link'}: {destination} -> {source}")

    if not pending:
        print("No changes needed.")
        return
    if not args.apply:
        print("Preview only. Use --apply to install; add --replace to back up conflicting copies.")
        return
    if conflicts and not args.replace:
        parser.error("Existing skills would be replaced. Review the preview and use --replace to back them up.")

    backup_root = destination_root.parent / "skill-backups" / (
        datetime.now().strftime("%Y%m%d-%H%M%S") + "-" + uuid4().hex[:8]
    )
    destination_root.mkdir(parents=True, exist_ok=True)
    if conflicts:
        backup_root.mkdir(parents=True)
        print(f"Backups: {backup_root}")
    for source, destination, occupied in pending:
        backup = backup_root / source.name
        if occupied:
            destination.rename(backup)
        try:
            create_link(source, destination)
        except (OSError, subprocess.CalledProcessError):
            print(
                f"Link failed: {destination}. "
                f"Any previous copy is preserved at {backup}; no further skills were changed.",
                file=sys.stderr,
            )
            raise
        if resolved_target(destination) != source.resolve():
            raise RuntimeError(f"Link target verification failed: {destination}")
        print(f"Installed: {source.name}")
    print("Start a new client session to discover the linked skills.")


if __name__ == "__main__":
    main()
