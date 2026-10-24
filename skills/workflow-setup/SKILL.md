---
name: workflow-setup
description: "Adopt, update or remove the portable development workflow in a repository when explicitly requested. Discover local commands and preserve existing agent instructions."
---

# Adopt the workflow deliberately

Run setup only on an explicit adoption or setup request. Installing the plugin alone is not adoption. Setup authorizes scoped repository instruction edits; it does not authorize production actions, installing unrelated dependencies or changing machine-wide agent settings.

These adoption instructions are for the package owner and already-authorized users under the package's proprietary license. A setup request does not grant intellectual-property rights that the user does not hold. Preserve the package license; do not imply a new redistribution grant.

Read the current repository instructions first, then the [methodology](../development-workflow/references/methodology.md). Locate the repository root and this skill's actual package location through the host runtime. Do not assume a home directory, operating system, agent CLI, language or shell.

## 1. Discover the repo

Inspect the actual manifests, build scripts, test configuration, CI, release docs and existing agent instructions. Read a narrow relevant sample, not every file. Identify:

- Languages, package/runtime tools, operating systems and required execution environment, including remote/container/embedded targets when applicable.
- The real customer interfaces: library, CLI, API, web, desktop, mobile, infrastructure, docs or other outputs.
- Focused checks, required local and remote gates, safe launch/health/cleanup recipes and release verification.
- Existing acceptance, security, data isolation, compatibility, performance and production boundaries.
- Task/evidence storage, independent reviewer options, host delegation policy and model/cost limits.
- Which instruction files each chosen agent actually reads. A plugin's presence is not proof that a future agent reads `AGENTS.md`.

Separate a command found in source from a command successfully executed. Use exact project-native syntax and working directory. Do not translate a PowerShell, IDE, remote build or hardware command into a guessed Unix equivalent. Where an item is absent, record **not applicable** with evidence, or **unknown** with the dependent action blocked. Do not invent CI or deployment for a docs-only repository.

Ask only consequential questions discovery cannot answer. Existing project rules and user decisions win; surface material conflicts before changing their meaning. Do not turn setup into a product audit or application rewrite.

## 2. Prepare the local bundle and profile

Copy the complete package `skills/` tree into `.development-workflow/skills/` so relative skill/reference links remain valid. Use the filesystem tools available to the agent, preserving bytes and paths; no helper runtime is required. Never flatten the tree or copy just the coordinator. Keep existing files until their ownership is understood.

Create `.development-workflow/project.md` from the [profile outline](../development-workflow/references/project-profile.md), filled from observed repository facts. Record package version and source revision from the installed manifest or checkout when available; mark an unavailable revision honestly. This profile supplies commands and policy links, not a second copy of those policies. Do not store secrets, credentials or private machine paths.

On a rerun, compare existing content with the requested package and preserve local changes. An unchanged setup produces no duplicate block or file churn. If the existing bundle/profile differs, show the material diff and distinguish source upgrades from local customization; resolve conflicts before overwriting. Update only workflow-owned content under the authorized setup request. If copying fails, report incomplete setup and do not activate default routing.

## 3. Connect the agent entry points

After the bundle and profile exist, add this bounded section to the existing `AGENTS.md`, adapting its placement to the file's structure:

```markdown
<!-- audienti-development-workflow:start -->
## Default development workflow
For development tasks in this repository, read
`.development-workflow/skills/development-workflow/SKILL.md`
and `.development-workflow/project.md`, then follow the applicable stage skills.
Use a short contract for clear tactical changes. Preserve this repository's
instructions and the user's scope, safety rules and delivery authority.
<!-- audienti-development-workflow:end -->
```

If `AGENTS.md` is a symlink, inspect its target and ownership. Preserve the link. Edit an in-repo owned target only when that is the intended policy owner. If the target is shared outside the repo or would affect another project, stop that write and resolve the placement; do not mutate shared instructions as a side effect.

For each chosen agent that does not read `AGENTS.md`, connect its documented project instruction entry point to that same block or owner. For example, preserve an existing `CLAUDE.md` symlink or file and add only the needed pointer if that host requires one. Do not replace existing files, create circular links, or claim support for agents whose instruction-loading behavior is unknown. Generic Markdown access is supported; automatic loading is host-dependent.

If the repository already has equivalent routing, reconcile it in place. Multiple contradictory default workflows need a product/policy decision, not another appended policy owner.

## 4. Verify adoption

Read back the diff, every entry-point link, the copied bundle and the profile. Check that all referenced local files exist and no plugin-cache or V10-only paths are required. Run an appropriate safe readiness command when available; record the actual result separately from discovered commands.

Using a fresh context or independent reviewer when available, start a representative task from the repo's documented entry point. Verify that it reaches the coordinator and profile, selects the right stage and local commands, and preserves scope and permissions. Rehearse rerunning setup: there must be one routing block and unrelated instructions must remain intact. Do not claim the consuming app's behavior is verified by this setup rehearsal.

Report whether the default is connected for each selected host, which commands were actually verified and any unknown capability. Missing test, CI or reviewer capability must remain visible; it does not justify a fabricated pass or an alternative weaker gate.

## Update or remove

Updates are explicit: compare the pinned bundle with the new package, preserve local customization, update provenance and recheck routing. Installing a new global plugin version does not silently update adopted repo snapshots.

On an explicit removal request, remove only the bounded routing block and unmodified workflow-owned files after checking other references. Preserve user edits and evidence. Never delete a general instruction file or replace a symlink merely to remove this workflow.
