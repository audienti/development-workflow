---
name: development-workflow
description: "Coordinate an accepted development task from intake through verified delivery when the repository has adopted this workflow or the user explicitly requests it. Resume the whole outcome after interruptions."
---

# Own the accepted outcome

Read the repository's current instructions, its `.development-workflow/project.md` profile when present, and the [shared methodology](references/methodology.md). Higher-priority instructions, repository policy and actual authorization govern execution. This skill is a method, not permission or a background scheduler.

If the repository has not adopted the package, explicit use can guide the current task without installing anything. Discover the relevant commands from source; ask only about material unknowns. Use [setup](../workflow-setup/SKILL.md) only when adoption is requested. Installation or discovery alone must not edit repo instructions.

## Route the work

Recover the current accepted task and evidence before starting a new record. Preserve the original request and amendments, definition of done, remaining work, endpoint, current revision, findings and next action. Read back actual repository/runtime state before replaying an interrupted external effect.

| Current need | Read next |
|---|---|
| Idea, unclear request, substantial bug or feature | [Intake](../workflow-intake/SKILL.md) |
| New bug/feature plan | [Blast radius](../workflow-blast-radius/SKILL.md), then [DRY](../workflow-dry/SKILL.md), then [Plan](../workflow-plan/SKILL.md) |
| Clear tactical fix or accepted implementation plan | [Build](../workflow-build/SKILL.md) |
| Evidence of behavior, visual quality or speed | [Verify](../workflow-verify/SKILL.md) |
| Current artifact and proof ready for challenge | [Review](../workflow-review/SKILL.md) |
| Reviewed work ready for its agreed endpoint | [Deliver](../workflow-deliver/SKILL.md) |

Do not load every skill or create a document for every stage. One task can hold the intake, plan, proof and recovery record. Substantial work uses bounded tasks and a readable delivery board; a short tactical contract is enough for a single clear change. Use the repo's tracker or a supported native plan, not an assumed GitHub account or a second competing tracker.

## Continue until the whole outcome is proved

Choose the smallest useful next action for an unmet requirement. Execute it, inspect the result, update the evidence and proceed. A completed slice, passing subset, worker reply, status question or context checkpoint does not complete the parent request.

When proof fails, return to the responsible step. Test failures usually return to build or diagnosis; a disproved design returns to planning; a failed release check keeps delivery open. After two fixes based on the same failed assumption, investigate that assumption instead of repeating it.

Respect explicit pause, cancellation or replacement. Stop dependent work for a material missing product decision, permission or capability; continue independent authorized work. Name the blocker, owner, next action and resume trigger. Do not ask the user to say “continue” for work the agent already owns.

Use supported callbacks or bounded inline waits for external jobs. A saved record cannot schedule a future turn. Do not claim autonomous resumption unless the runtime actually provides it. Before retrying an action with an unknown result, read back its state.

## Finish honestly

Reconcile the whole latest request against current evidence in both directions. Every accepted requirement needs proof and delivery; every claimed capability needs an accepted requirement. Keep missing, stale, skipped and blocked proof visible. Close only at the agreed endpoint, with the clear explanation and receipt in [delivery](../workflow-deliver/SKILL.md).
