---
name: workflow-deliver
description: "Deliver reviewed work to its agreed local, PR, release or production endpoint, read back the result and reconcile every accepted requirement before closing."
---

# Finish at the agreed endpoint

Read repository instructions, the project profile, [shared methodology](../development-workflow/references/methodology.md), original request/amendments and current proof/review record. Establish the exact endpoint and existing authorization before taking external action.

## Explain readiness

Give a clear account of the accepted problem and why it matters, planned versus built behavior, rule/state owners, why the solution works, executed proof, resolved review findings and simplifications. State confidence (High, Medium or Low) and its evidence, exclusions, remaining uncertainty and the actual delivery stage. If the design cannot be explained plainly, inspect its complexity; prose alone is not proof.

Reconcile in both directions:

1. Every accepted requirement has implementation or an accepted no-work disposition, meaningful current proof, resolved review and the required delivery evidence.
2. Every claimed capability maps to accepted scope. Nothing was silently added, substituted or dropped.

Missing, stale, failed, deferred or blocked required work remains open. A completed slice does not close the parent task. A changed deliverable returns to affected verification/review before release.

## Deliver and read back

Use the project's publication procedures, PR template/checks, changelog and release gates when they exist. Do not assume GitHub, a default branch name or a CI vendor. Inspect final head/base and remote checks after publication; local green is not remote green. Review all actionable threads, including pagination when necessary.

An accepted end-to-end plan can authorize ordinary merge and normal deployment under the repository's policy once scope is preserved, confidence is High, required proof and CI are current, review findings are resolved and the final explainer is complete. Do not ask for redundant confirmation. Preserve local-only/PR-only endpoints and separate permission for destructive effects, live sends, production-data writes, provider-gate expansion or scope changes. Inspect merge-triggered deployments and other pending changes in the release. Stop at the safe endpoint if it would cross an unapproved boundary.

For a release/deployment, confirm the actual artifact or exact revision and exercise the agreed customer path at the required scope. Name disabled flags, missing configuration and rollout gaps. A deployed revision alone does not prove the feature is usable. A package release may need import/install proof; a library need not have a running service.

If an external action times out or its result is unknown, read back state before retrying. A failed runtime check keeps the task open; diagnose or use an authorized rollback rather than declaring delivery complete.

## Close the loop

Report only the highest applicable stage proved: changed locally, verified locally, pushed, PR green, merged, released/deployed exact revision, required runtime behavior verified. Use the stage vocabulary relevant to the project; docs-only work may finish as a reviewed local artifact if that is its endpoint.

Update the existing tracker, board and recovery record to match reality. Close the original task only when the whole accepted outcome is proved, linking evidence and a useful reopen condition. Do not create an undelivered bookkeeping commit after closure; keep completion receipts in the existing evidence/tracker when possible.

Give the user a concise result: solved/partly solved/still open, what works, what remains unbuilt or unproved and the delivery stage. Include per-model token/API-equivalent cost attribution where available; otherwise state that it is partial or unavailable. Keep detailed rates/counters in the evidence, not repeated updates.

If blocked, name the missing dependency, owner, exact next action and resume trigger. Continue any executable authorized next step instead of handing agent-owned work back to the user.
