---
name: workflow-plan
description: 'Turn accepted intake into the smallest complete, evidence-backed implementation plan. Use after intake for substantial bugs, features, UX changes, or when the developer asks for a plan.'
---

# Plan

Use the shared [methodology](../development-workflow/references/methodology.md). Keep the plan in the current issue, plan, or task record. Existing agreement counts; do not ask for approval again when the scope and decisions are already accepted.

## Define the whole outcome

Start with the accepted product purpose and state how this task contributes to it. Carry forward the seven task answers, current disposition, named use cases, accepted decisions, open assumptions and protected behavior. State the smallest complete customer path and its observable result. Do not replace the accepted task with a smaller slice; keep any slices as a checklist under the same task. If product purpose is materially missing, use [intake](../workflow-intake/SKILL.md) before choosing a solution.

Use the records in [product context](../development-workflow/references/product-context.md). List current scope, link actual backlog entries for agreed later work, and link the separate do-not-do decisions with their reasons. Do not treat “not in this release” as “never,” or leave later work only in a chat or exclusions paragraph. Missing authority to write a backlog item is a visible gap. Removing accepted current work still requires a scope decision.

For a clear tactical change, use a short contract instead of a substantial plan. Include the problem, scope, expected result, must-preserve behavior, proportional design explanation, and proof. Do not add routine approvals or documents.

## Explain the design before code

Write a proportional code-quality explainer in the existing record before implementation. It must identify:

- each affected business rule, its condition, owner, result, and allowed side effects;
- current source-backed behavior for a fix, or proposed architecture and fit for new work;
- authoritative state, allowed writers, transitions, and failure and recovery behavior when relevant;
- the responsibilities of rule owners, workflow coordination, external effects, and the adapters or interfaces that exist for this change;
- a readable flowchart, plus a state or dependency diagram only when it clarifies the design;
- accepted decisions, proposed assumptions, unresolved questions, and established terms. Keep new terms proposed until agreed.

Do not begin dependent implementation while a material behavior or architecture choice remains unresolved. Continue independent investigation.

Record consequential architecture choices as Architecture Decision Records (ADRs), using the existing owner and the product-context format: context, options, choice, reasons, consequences, status, decision source and links. Keep proposed choices separate from accepted ones. Routine implementation choices do not each need an ADR. An ADR's rejected option is not automatically a do-not-do decision. Maintain the glossary for agreed terms; do not use an invented term as an accepted design premise.

## Check impact and duplication

Before finalizing a bug-fix or feature plan, complete [blast-radius analysis](../workflow-blast-radius/SKILL.md), then [DRY analysis](../workflow-dry/SKILL.md). Carry forward safeguards, unproved assumptions, findings, and their with-this-change or later dispositions. Do not turn these checks into permission to expand scope.

## Specify behavior and work

Write behavior examples before coding. Include positive outcomes and meaningful negative cases for protected behavior, permissions, invalid input, or failure paths affected by the change. Name the expected observable result and the check that proves it. Test the actual outcome through each accepted interface this change affects; do not require extra API or command-line surfaces that the product does not have. Route or entry-point coverage alone is not proof.

Use Given / When / Then to state the starting condition, customer action and expected result. Keep one requirement-to-proof table in the existing record:

| Requirement / behavior | Task | Named check and level | Expected assertion | Evidence / status |
|---|---|---|---|---|
| Stable requirement ID and outcome | Bounded task | Native test or real interface recipe | Meaningful success/failure result | Not run, Red, Green or Blocked |

Each task brief includes its parent outcome, allowed files/scope, inputs and current evidence, expected output, protected behavior, dependencies, owner, named assertions, endpoint and unresolved findings. Keep test, refactor, review and delivery status separate. Substantial work uses the existing readable board; do not create a competing specification.

For user-visible UI work, agree where it belongs and how the user reaches it, completes the task, and leaves. Create a standalone HTML prototype with synthetic data, relevant states, and actions. Link it from the plan and review placement and missing functions before implementation. Keep the prototype proportionate to the change.

Break implementation into small, complete tasks with clear owners, inputs, outputs, dependencies, and proof. Put the main constraint proof early. Include verification, independent review where required, and the agreed delivery endpoint. Give a rough effort or token estimate with uncertainty; do not present it as a promise.

## Agree and continue

Resolve material product and architecture choices at the existing planning boundary. Record the accepted scope and exclusions. Do not add a second approval gate when existing agreement covers the work.

Once the plan is accepted, the primary owns implementation integration, verification, review, and delivery through the agreed endpoint. Link [intake](../workflow-intake/SKILL.md) for problem framing. Later stages follow the package's build, verify, review, and deliver skills.
