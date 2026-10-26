# Shared methodology

Read this with the repository instructions and project profile. It is the shared contract; each stage skill owns its detailed method.

Apply this methodology as mandatory workflow only when the repository has explicitly adopted it or the user explicitly requests the methodology or the particular skill. A coordinator invocation within either scope can route to the stage skills. Merely installing the plugin or automatically selecting a skill does not adopt the workflow. If neither condition holds, follow the repository's existing process without changing its defaults; do not initiate setup unless requested.

## Product purpose, shared terms and boundaries

Read [product context](product-context.md) before applying a stage, including a directly requested skill. Establish the product-level goal before the task-level solution: who it serves, the larger problem, the intended result and the high-level concept. This applies in idea, new-product and existing-product work. Reuse accepted answers; ask one consequential question when material purpose is missing, unclear or contradicted. Do not choose a dependent solution or build while that question is unresolved.

Each task must show how it serves the accepted product purpose and respects its boundaries. Keep that link in plans, briefs and recovery records, and check it during review and delivery. A small task can use one sentence and existing links; it does not need another mission interview.

Maintain one owner each for product purpose, the glossary, Architecture Decision Records (ADRs), the later backlog and the do-not-do list. Reuse existing docs or tracker views. The profile links to their owners; it does not copy their definitions. Missing records are established proportionately under existing edit authority, with unknowns and proposed decisions visible. Empty files do not establish shared understanding.

Use about 80–85% ASD-STE100-inspired plain English as the project's writing target, not an invented compliance score. Use short active sentences and familiar words. Define important domain terms, specialized meanings and abbreviations in the shared glossary, and use those meanings consistently. Keep new agent-created terms proposed until agreed; do not disguise an unsettled idea with a new name. The product-context guide owns the detailed writing and terminology rules.

Keep scope explicit: **now** is the accepted current task; **later** has an actual backlog entry; **do not do** has an accepted, separately recorded prohibition with its scope and reason. An unresolved choice stays unresolved. A rejected architecture option does not automatically become a product prohibition, and an agent cannot quietly move prohibited work into the backlog. Changing an accepted boundary needs an explicit decision with history retained.

## Authority and scope

The user supplies product judgment; the primary agent owns requirements, integration, proof and the final decision. Reuse accepted decisions. Do not invent approvals for steps already authorized, or infer permission from a tool being installed.

Agree the delivery endpoint during intake. Where the user and repository authorize end-to-end delivery, an accepted plan covers ordinary implementation, independent review, merge and normal release once scope is preserved, confidence is High, required proof and CI are current, findings are resolved and the final explainer is complete. Confidence must follow the evidence; it cannot replace missing proof. Preserve local-only and PR-only boundaries. No skill grants broader production permissions than the user or repository has supplied.

Read-only authorization does not permit writes. Destructive changes, production-data changes, live sends, new or expanded provider execution, and out-of-scope work retain their own authorization. Inspect indirect release effects: a merge may deploy other pending changes too. Keep tenant isolation, identity, access control, action order and execution gates intact where applicable. If a platform denies an action, do not route around the denial.

## One outcome and one record

Keep original requirements, amendments, product-purpose link and task contribution, current-state disposition, accepted scope, linked later/do-not-do decisions, protected behavior, named proof, endpoint and unresolved assumptions together. Keep test status (Not run / Red / Green / Blocked), refactor, review and delivery status separate. Green is not Delivered.

The stage-specific acceptance, scenario-trace and coverage contract is defined in [workflow-plan](../../workflow-plan/SKILL.md) and [workflow-verify](../../workflow-verify/SKILL.md).

Substantial work uses bounded tasks with a readable board: Ready, Building, Verifying, Reviewing, Delivered; Blocked names a real dependency. The board can be a view of the existing tracker or native plan; do not add another specification or invent a required board service. The parent outcome remains open until all accepted work is proved.

At material boundaries retain cwd/workspace, branch or equivalent revision, changed files, valid evidence inputs, findings, endpoint, next action and blocker. After compaction or handoff, resume this record and inspect actual state. Do not reconstruct the task from memory or replay effects.

## Proportional quality and proof

Before every new feature or behavior fix, including tactical fixes, explain the affected rules, owners, authoritative state, allowed effects, failure/recovery, architecture fit, proof and open assumptions. Include a readable flow; use a tiny text diagram when sufficient. Review at the existing planning boundary, not a new approval ceremony.

Build the smallest complete useful path. Preserve accepted behavior and meaningful data. Remove replaced paths within the agreed change when safe; add compatibility or transition layers only for a demonstrated current need. Unlike the source V10 project, a consuming repo may have existing customers and compatibility obligations. Do not assume a direct cutover is safe.

Describe behavior before implementation. Prove meaningful positive and negative outcomes with the same accepted assertions; do not weaken tests to get green. Use project-native tests and runtime proof. Documentation and behavior-preserving refactors do not require an artificial Red result.

Use backend/API integration tests for relevant backend outcomes and side effects, not merely route existence. Use native library or CLI tests where those are the product. Accepted interfaces share business rules and capabilities; do not force a web UI, API or CLI into a project that does not have or require one.

For UI work, agree placement and reach/complete/leave actions using a standalone HTML prototype with synthetic data before implementation, then prove the real interface. HTML describes the flow even for a native UI; if the target cannot meaningfully be represented that way, resolve a concrete equivalent prototype with the user before replacing the requirement. Retain before/after visual evidence and independent visual review. For a brand-new surface, retain the agreed prototype as the design baseline and label the lack of a preexisting runtime view.

Compare baseline and candidate on the same representative inputs. Keep correctness, visual quality and performance separate. For interactive UI paths, the default target is a usable response within 2 seconds; agreed fast paths require p95 below 1 second. Discover stricter or different established project budgets and resolve conflicts during planning, before measuring. Long work needs prompt acknowledgement, progress and a separate completion budget. Do not apply interactive UI budgets to a batch job or compiler build without a relevant requirement.

## Execution and review

Prefer direct tools, APIs, local files and focused checks. Use a real browser or native UI driver for interface/visual proof. Investigate repeated tool failures. Use isolated environments and synthetic, sanitized or separately authorized representative data; never connect development to production for convenient proof. Preserve evidence during cleanup.

Follow the host's delegation policy and cost ceiling. Do not require delegation when unavailable or prohibited. If implementation is delegated, default to one bounded writer with explicit scope, acceptance and stop conditions; the primary integrates. Delegates do not delegate. Never start a costlier model or reasoning setting than authorized, including defaults hidden in wrappers.

Independent review is required for material workflow or business behavior and its tests. Prefer another model family; a same-family independent instance is an availability fallback with its reason recorded. A human independent reviewer can satisfy the role. Keep one active reviewer per obligation. No independent reviewer means the gate is unmet, not self-approved.

Review the current artifact, original request, acceptance and actual proof; challenge tests and simplification. Resolve material findings through bounded, scoped rounds. Disputes remain open until resolved with evidence; agreement cannot substitute for a missing check. Stop a failed/stalled invocation before replacing it within existing authority and cost limits. Do not repeat unchanged attempts or lower proof to obtain agreement.

Run focused checks during changes, then the required gates. Reuse still-valid evidence; rerun affected checks after artifact, requirement or input changes. Keep skipped, unavailable and failed gates visible. Read remote results and the actual deployed revision when those endpoints apply.

## Communication and cost

Lead with what happened and whether it is solved, partly solved or still open. Name completed functionality, what remains unbuilt and what remains unproved, plus the highest delivery stage actually observed. Apply the product-context writing target to questions, plans, handoffs, reviews and final replies. Use the agreed glossary and keep proposals separate from accepted decisions. Record agreed terminology in its owner when edits are in scope; missing edit authority stays visible instead of becoming an invented definition.

Estimate effort and token use for substantial work with uncertainty. Prefer narrow reads, bounded delegation and reused evidence. Retain usage counters where exposed, aggregate each request once, and report missing attribution rather than fabricated totals. At closure include per-model tokens and API-equivalent cost when measurable, using current official provider rates, currency, pricing date and tier. Distinguish the estimate from a subscription bill. Missing telemetry does not block otherwise completed work.

A cost estimate or context checkpoint is not permission to abandon an accepted task. Real tool, runtime and permission limits remain binding. For active bug troubleshooting, ask once whether cooldowns must be respected (default no), then continue immediately within existing action authorization. That time preference never authorizes live sends, data resets or bypassing provider safety controls.
