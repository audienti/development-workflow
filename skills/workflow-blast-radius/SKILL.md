---
name: workflow-blast-radius
description: 'Find affected callers, data, ordering, permissions, and neighboring behavior before finalizing a bug-fix or feature plan. Use when planning a behavior change or checking its likely unintended effects.'
---

# Blast radius

Follow the shared [methodology](../development-workflow/references/methodology.md). Work within the accepted task and current authorization. This is a scoped investigation, not permission to inspect unrelated systems or perform external changes.

## Trace the change

1. State the proposed behavior and the rule or state owner it touches.
2. Find the source of truth, direct callers, indirect entry points, and existing tests. Search only the changed area and affected callers.
3. Follow the behavior through the interfaces and execution paths that this product actually supports. These may include a UI, API, command line, library entry points, jobs, or callbacks. Do not add hypothetical interfaces to the scope.
4. Check hidden effects that could change the outcome: persisted or cached state, user or customer boundaries, action order, retries, scheduled work, provider gates, and neighboring use cases, where they apply.
5. Separate confirmed paths from plausible but unproved paths. Do not infer runtime safety from names, comments, or route coverage alone.

## Prove the pivotal safety fact

Name the assumption that matters most to safe behavior, such as whether a caller shares the same rule owner or whether an action checks current permission at execution time. Trace it through source, then execute a focused test or safe isolated reproduction against the real code. Record how far the evidence goes: assertion only, source citation, traced failure path, executed code, or real customer path. Source inspection alone is not executed proof. If execution is unavailable, state the safety fact as unproved and name the concrete check that would resolve it. Do not perform a live mutation for this proof without separate authorization.

A prepared, cached, or queued record does not by itself prove that an external action is allowed. Preserve the product's existing customer and user boundaries, fail-closed behavior, execution gates, and action order where these exist. Do not expand authority or weaken a gate as part of impact analysis.

## Record useful findings

For each material affected path, record:

- the caller or data touched;
- the possible unintended result;
- the safeguard or behavior that must remain;
- the evidence or check that can prove it.

Keep findings tied to the proposed change. Do not create a broad test matrix. Use existing behavior contracts and verification routes where they cover the risk.

If review is part of the task, use the repository's existing independent reviewer and review rules. Do not launch a second reviewer for this skill. An independent review cannot replace runtime or test proof.

Carry safeguards and gaps into [the plan](../workflow-plan/SKILL.md), and coordinate shared-rule or state findings with [DRY analysis](../workflow-dry/SKILL.md). Do not edit product code when the task is only to assess impact.
