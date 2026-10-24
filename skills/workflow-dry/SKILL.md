---
name: workflow-dry
description: 'Check an affected area for repeated business decisions, competing state owners, and obsolete paths before finalizing a bug-fix or feature plan. Use after blast-radius analysis when planning behavior changes.'
---

# DRY analysis

Use the shared [methodology](../development-workflow/references/methodology.md). Inspect only the proposed change and its affected callers. Similar-looking code does not prove that two paths enforce the same rule.

## Find semantic duplication

Look for:

- the same business decision implemented in more than one place;
- multiple writers or competing owners for the same authoritative state;
- copied policy checks that can disagree over time;
- obsolete paths that still execute or preserve conflicting behavior;
- abstractions that add a new owner without a shared rule or clear boundary.

For each candidate, compare inputs, conditions, outcomes, side effects, and failure behavior. Keep genuinely different rules separate, even when their code looks similar. Preserve customer or user boundaries, provider gates, action order, and other accepted safety rules that apply to the product.

## Keep findings actionable

Return at most five material findings. For each, state:

- concrete files or paths and the duplicated decision, state, or obsolete route;
- the current owner, if one is clear, and the proposed single owner or flow;
- what code or path could be removed and which callers or data it affects;
- the behavior proof needed to show that the accepted result and safety limits remain intact;
- disposition: **with this change**, **later**, or **not duplication**, with a brief reason.

Distinguish necessary corrections from optional cleanup. Do not widen the task just because another issue is nearby. If removing a path would change accepted behavior, keep it open for a product decision rather than silently simplifying it.

This skill is an audit only: do not edit product code. Feed accepted findings and deferred work into [the plan](../workflow-plan/SKILL.md). Use [blast-radius analysis](../workflow-blast-radius/SKILL.md) first to identify affected callers and risks.
