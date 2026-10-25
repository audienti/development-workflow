---
name: workflow-build
description: "Implement an accepted plan or clear tactical change through meaningful Red, Green and Refactor evidence while preserving surrounding behavior."
---

# Build one complete useful path

Read repository instructions, the project profile and the [shared methodology](../development-workflow/references/methodology.md). Recover the accepted requirements, current disposition, delivery endpoint and proof. If substantial work lacks an accepted design, use [intake](../workflow-intake/SKILL.md) and [plan](../workflow-plan/SKILL.md); agreement on the symptom alone does not approve a repair design.

Recover the product-purpose link, glossary meanings, applicable ADRs and current/later/do-not-do boundaries too. Build only the accepted current work. If a shortcut conflicts with the product goal or a recorded prohibition, stop that dependent choice and resolve it; do not redefine terms, implement a backlog item or reopen a do-not-do decision on your own.

For a clear tactical bug, perform the intake symptom check, state the short contract and proportional rule/state/architecture explainer, and fix the narrowest responsible owner. No broad interview is needed. Repeated related failures or unclear consequences require substantial diagnosis. UI changes still need agreed placement/prototype and real interface proof.

## Implement and prove

1. Check the workspace/revision and preserve unrelated edits. State the mode, scope, invariant, endpoint and expected proof before editing. Use the repo's environment and isolated data; do not guess runtime versions or use another workspace's test database.
2. **Red:** run the named behavior check and show that it fails for the missing/wrong behavior. An environment, syntax or fixture failure is not the expected Red. Keep credible reproduction evidence if a direct failing run is unavailable, and label the gap.
3. If the baseline already passes, determine whether the behavior exists or the assertion misses the failure. Do not break correct behavior to manufacture Red, or implement a capability already present.
4. **Green:** make the smallest sound implementation that satisfies the same assertion and the meaningful positive path. Keep protected neighboring behavior, permission, persistence and side-effect checks relevant to the change.
5. **Refactor:** simplify ownership/control flow within scope. Reuse the existing rule owner and remove obsolete execution paths when the accepted cutover permits it. Inspect the diff and affected callers for duplicate decisions, competing writers, hidden ordering, swallowed failures and unnecessary abstractions.
6. Run focused checks and then the required project gates. Send the current artifact and evidence to [verification](../workflow-verify/SKILL.md) and [review](../workflow-review/SKILL.md). After review fixes, rerun affected checks and refresh invalidated proof.

Documentation and behavior-preserving maintenance use consistency or preservation checks, not an artificial new behavior test. Add tests that assert useful behavior; do not mirror implementation merely to increase a count.

Changing an accepted assertion is a specification change. Record its reason and obtain independent review; changing accepted behavior needs the corresponding scope decision. A passing test cannot authorize removal of a requirement.

## Keep the work bounded

Before data/schema/API/config transitions, identify readers, writers, deployment ordering and current consumers. Use the repo's migration contract, preserve required data/compatibility and distinguish expand/backfill from destructive contraction. An accepted ordinary release does not authorize destructive migration effects.

Delegation follows the host policy and cost ceiling. If allowed and useful, give one writer a bounded brief with files, behavior, inputs, assertions and stop conditions. The primary owns integration and final verification; delegates do not delegate. Do not depend on a named model or external worker service.

After two failed fixes based on one assumption, investigate that assumption. Record unrelated defects separately when tracking is authorized, without expanding this task. Continue remaining accepted slices; a green slice is not a completed parent request.
