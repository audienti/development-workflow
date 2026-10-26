# Audienti Development Workflow

Give an agent a repeatable method to understand a problem, agree on a small complete solution, build it, prove it, independently review it, and finish the agreed delivery.

Start with the product goal: who it serves, the larger problem and the result it should achieve. Keep that purpose in view before choosing a task solution, including during idea and new-product work. A shared glossary, architecture decisions, explicit later backlog and separate do-not-do list keep agents from drifting in meaning or scope. See [product context](skills/development-workflow/references/product-context.md).

The methodology works across languages and environments: applications, libraries, CLIs, infrastructure and documentation. Repository setup supplies the actual commands, interfaces, safety rules and delivery endpoint. The skills do not require Rails, a Unix shell, GitHub issues, a particular CI system, cloud provider, agent vendor or model.

## Install and adopt

Install the plugin, then explicitly adopt it in each repository. Installation alone does not change a repository's default workflow or grant permission to deploy.

These instructions are for OMALab and users authorized under [LICENSE](LICENSE). Public availability does not grant additional use, copying or redistribution rights. Repository-local adoption and customization described below require that existing authorization; this release does not change the proprietary license.

For Codex:

```text
codex plugin marketplace add audienti/plugins
codex plugin add development-workflow@audienti
```

For Claude Code:

```text
claude plugin marketplace add audienti/plugins
claude plugin install development-workflow@audienti
```

Then ask your agent:

> Use workflow-setup to adopt this methodology as this repository's default development workflow. Discover this project's commands and preserve its existing instructions.

For another agent, obtain this repository and have the agent read [workflow-setup](skills/workflow-setup/SKILL.md). The package is ordinary Markdown. The agent needs file access and a supported way to load repository instructions; it does not need a plugin API. Agents that do not automatically read `AGENTS.md` need a pointer in their documented instruction entry point. Setup checks this explicitly.

Setup keeps a versioned copy of the skill bundle in `.development-workflow/skills/`, a project profile in `.development-workflow/project.md`, and a short default-routing block in the repository's existing instructions. No machine-private plugin-cache path is required by the adopted repo. It preserves existing content and symlinks, reports conflicts, and does not silently overwrite a locally customized bundle. See [setup](skills/workflow-setup/SKILL.md) for reruns, updates and removal.

The profile links to the project's product purpose, glossary, Architecture Decision Records (ADRs), backlog and do-not-do records. Setup reuses existing owners or creates proportionate records; it does not invent product decisions to fill templates. These records belong to the project and survive plugin removal. A missing material product goal must be resolved before planning a solution.

Communication aims for 80–85% ASD-STE100-inspired plain English. Important domain terms and specialized meanings belong in the glossary. This is a writing target, not an official compliance percentage. [ASD's guidance](https://asd-ste100.org/about_STE.html) permits project-specific terminology.

## Upgrade an adopted repository

Obtain the new plugin release through your host's plugin update process, then ask:

> Use workflow-setup to update this repository's adopted workflow to v0.3.0. Preserve our local changes and agreed product records. Add any missing purpose, glossary, architecture-decision, backlog and do-not-do links, and ask about unresolved product decisions.

Installing the new global package does not update the snapshot already copied into a repo. Setup must compare and update that snapshot explicitly. You do not need to repeat accepted product answers. The [release notes](CHANGELOG.md) describe the new requirements.

## Skills

| Skill | Use |
|---|---|
| [development-workflow](skills/development-workflow/SKILL.md) | Coordinate the whole accepted outcome; resume interrupted work. |
| [workflow-setup](skills/workflow-setup/SKILL.md) | Discover project capabilities and adopt the workflow explicitly. |
| [workflow-intake](skills/workflow-intake/SKILL.md) | Find the real problem, investigate facts and resolve product choices. |
| [workflow-blast-radius](skills/workflow-blast-radius/SKILL.md) | Find affected behavior and execute proof of critical safety assumptions. |
| [workflow-dry](skills/workflow-dry/SKILL.md) | Find duplicated decisions and competing state owners. |
| [workflow-plan](skills/workflow-plan/SKILL.md) | Define the smallest complete solution and its behavior proof. |
| [workflow-build](skills/workflow-build/SKILL.md) | Implement through Red, Green and Refactor; take the tactical path when appropriate. |
| [workflow-verify](skills/workflow-verify/SKILL.md) | Prove behavior on the actual interfaces and retain valid evidence. |
| [workflow-review](skills/workflow-review/SKILL.md) | Run an independent review and resolve findings without lowering acceptance. |
| [workflow-deliver](skills/workflow-deliver/SKILL.md) | Verify the authorized endpoint, reconcile the request and close the task. |

Use the coordinator after adoption; it loads only the skills the task needs. Individual skills can also be requested separately. Small changes use a short contract. Documentation changes do not trigger application tests or deployments merely because those stages exist.

## What it guarantees—and what it does not

These are instructions, not a scheduler, permissions bypass or enforcement service. They define the proof an agent must obtain and require it to report missing capabilities honestly. Installation does not establish that an agent follows the instructions. Independent review requires a real independent reviewer; a model reviewing its own work is not sufficient.

No model names are pinned. Discover available review and execution tools, respect the host's delegation policy and cost limits, and record unavailable capabilities. A project may have no deployment, UI or API; apply proof to its accepted interfaces rather than inventing them.

## Maintain the package

Run `python3 scripts/validate.py` for manifest, skill metadata and local-link checks. If Claude Code is available, also run `claude plugin validate . --strict`. These check packaging, not behavioral correctness. Exercise [the evaluation scenarios](docs/evaluation.md) and get independent review when workflow behavior changes.

The [source map](docs/source-map.md) records how the original workflow and relevant V10 skills were adapted. Source provenance is not a runtime dependency. Updates must preserve accepted methodology and make deliberate changes explicit.

## License

Copyright (c) 2026 OMALab, Inc. All rights reserved. See [LICENSE](LICENSE).
