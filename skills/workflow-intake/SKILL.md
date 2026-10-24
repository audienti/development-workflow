---
name: workflow-intake
description: 'Establish or resume the evidence-backed problem, current disposition, intended outcome, and protected behavior. Use when starting a substantial bug, feature, UX, or idea task, or when a report has unclear scope or cause.'
---

# Intake

Use the shared contract in [methodology](../development-workflow/references/methodology.md). Keep one visible issue, plan, or short contract as the task record. Do not create extra records when an existing one is current.

## Open with the seven answers

Show the questions with researched answers. Do not make the developer repeat facts or decisions already recorded. Separate evidence, accepted decisions, proposals, and unknowns.

1. **What is the real problem?** State the reported symptom, the owned cause if known, and the link between them.
2. **Why does this matter, and is it still needed?** State the user or business effect and the current disposition: unfixed, partly fixed, fixed, or no work needed. Support the disposition with current evidence.
3. **What is true now?** Check relevant code, tests, task records, branches or releases as needed. Mark facts separately from assumptions.
4. **What should be true afterward?** Name customer use cases and observable outcomes.
5. **What must not change?** Name relevant behavior, data, access, safety limits, and performance expectations, with a check for each material risk.
6. **What is the smallest complete outcome?** State the useful path, dependencies, exclusions, and intended delivery endpoint.
7. **Why is this the right minimum?** Compare a symptom repair with the underlying repair when both are plausible. State remaining uncertainty and simpler alternatives.

## Diagnose with evidence

For a tactical bug, do a bounded symptom check: search open/closed task history for the same behavior, inspect recent revisions of the affected files, and consult the repo's existing lessons or incident record if it has one. Record what was searched and whether a related recurrence exists. Two earlier fixes of the same failure, another related incident, or a documented lesson are evidence of a pattern; unrelated edits are not. Missing history is a confidence limit, not an invented clean result.

- Reproduce the behavior or retain credible failure evidence. Compare expected and actual results.
- Trace the shortest supported cause chain from symptom to owned cause. Do not turn one local cause into a system-wide theory.
- Call it an underlying recurring problem only if it explains another observed symptom. Otherwise call it a local cause, with the bounded history/source searches and unchecked falsifier recorded.
- Record evidence for each link, confidence, and one falsifier: what observation would disprove the diagnosis. Check the falsifier when practical.
- Identify the main constraint: the unknown cause or capability most likely to prevent the outcome. Put a small proof of it early in the eventual plan.
- Look for repeated symptoms and earlier fixes. If two fixes failed on the same assumption, investigate that assumption before proposing another repair.
- Do not treat a closed issue as proof that runtime behavior is fixed, or an open issue as proof that code is absent.

## Keep the conversation focused

Ask one consequential unresolved question at a time. Give a recommendation and its tradeoff, then wait before doing work that depends on the answer. Continue independent investigation while a decision is pending.

Reuse explicit agreement from the current conversation and task record. On resume, report only what changed or remains unknown. Do not ask again for accepted choices or add an approval round for routine implementation details.

If intent is clear and the work is tactical, use a short contract: problem, scope, expected result, protected behavior, and proof. Do the symptom check and proportional design explanation, but skip a substantial-task interview. Repeated symptoms, broad consequences, or unresolved choices make the task substantial.

For substantial work, continue to [plan](../workflow-plan/SKILL.md).
