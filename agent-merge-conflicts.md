# Agent Merge: Conflicts

Paste the numbered rules into **Agent merge instructions > Conflicts**. These supplement Common only when conflict resolution or required base updates are authorized.

1. Verify live head/base, stack parent, open state, and mergeability; inspect branch, worktree, and history. Use `gh pr checkout <number>` before edits/merges. Never update from an unrelated or main-based worktree branch.
2. Update a conflict-free but behind branch only when policy requires it. Fetch, require a clean worktree, and record local/remote head SHAs, intended base SHA, and PR base; stop on unexpected differences.
3. Prefer merging the confirmed remote base INTO the PR head when policy allows. For `main`: `git fetch origin main && git merge origin/main`. A required rebase still needs authorization and history safeguards.
4. For an auto-retargeted stack, verify the new live base and exact intended parent SHA; never use a stale/deleted base or infer a new stack. Do not move siblings or fan out updates without branch-specific authorization and ownership.
5. Before history changes, create local unpushed backups for each changed branch. Inspect complete ancestry/diffs, exclude forbidden changes, and identify allowed commits/files. Use only the exact approved parent SHA.
6. For stacked rebases, establish the old parent boundary; replay only this PR's commits. Check patch-equivalent changes already in the new parent even when SHAs differ; never replay rebased parent commits.
7. Preserve approved base behavior plus the intended layer when resolving conflicts. Do not blindly choose whole files or restore unrelated history. Ask when intentional changes cannot be reconciled without product/UX decisions.
8. Reconstruct on a temporary branch from the exact approved base with selected commits in order. Confirm empty-commit behavior already exists before skipping; verify history/diff before updating the owned branch. Never use `git reset --hard`.
9. Before pushing, use `git range-diff` where applicable; scan complete history/diff for excluded commits/files/symbols and conflict markers. Flag unexpected diff growth. Validate affected stack links, base SHAs, PR bases, and per-layer ranges; parent changes must not leak into child review diffs. Inspect other links read-only.
10. Run impacted regressions and required repository checks; verify affected user flows. Restore dependencies with the project lockfile if merged dependency changes require it. Resolve introduced failures without weakening validation.
11. Prefer normal pushes. An authorized force-push must use `git push --force-with-lease=refs/heads/<branch>:<expected-old-sha>` tied to the recorded remote SHA. After pushing, verify local/remote equality, clean worktree, open PR, intended base, no GitHub conflicts, and clean live diff; unknown mergeability is not confirmation.
12. After history stabilizes, refresh affected description, review instructions, and evidence. Report old/new SHAs, backups, conflicts/skipped commits, changed files, tests, push outcome, and any verified base retarget.
