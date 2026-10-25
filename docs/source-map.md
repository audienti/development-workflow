# Methodology source map

This release adapts the user's `docs/development-workflow.md` and related skills from the V10 worktree at revision `93f544eba6e672a74b7cd1a2dd31914d410ca520` (October 24, 2026). These source paths record provenance; they are not links or runtime dependencies of the distributed package. The user accepted portability across repositories, languages and environments, default use after explicit setup, and one `audienti/development-workflow` plugin listed in `audienti/plugins`.

## Workflow coverage

Release 0.2.0 also incorporates the owner's October 25 field-use corrections: product mission must precede task-level problem solving; shared terminology and simple communication must be explicit; architecture decisions, later backlog and reasoned do-not-do boundaries need durable owners. These requirements extend the original summary rather than claiming they were fully enforced in v0.1.0. Their owner is [product context](../skills/development-workflow/references/product-context.md), used by setup, the coordinator and stage skills.

| Source section | Package owner |
|---|---|
| Whole flow and task ownership | [Coordinator](../skills/development-workflow/SKILL.md) and [shared methodology](../skills/development-workflow/references/methodology.md) |
| 1. Kind of work and tactical route | [Intake](../skills/workflow-intake/SKILL.md), [build](../skills/workflow-build/SKILL.md) |
| 2. Seven opening answers | [Intake](../skills/workflow-intake/SKILL.md) |
| 3. Main constraint, blast radius, DRY | [Intake](../skills/workflow-intake/SKILL.md), [blast radius](../skills/workflow-blast-radius/SKILL.md), [DRY](../skills/workflow-dry/SKILL.md) |
| 4. Plan, explainer, UI prototype and agreement | [Plan](../skills/workflow-plan/SKILL.md) |
| 5. Behavior specs, interface parity, evidence and coverage | [Plan](../skills/workflow-plan/SKILL.md), [verify](../skills/workflow-verify/SKILL.md) |
| 6. Bounded tasks and one delivery board | [Plan](../skills/workflow-plan/SKILL.md), [methodology](../skills/development-workflow/references/methodology.md) |
| 7. Red, Green, Refactor and maintenance | [Build](../skills/workflow-build/SKILL.md) |
| 8. Local/remote gates and evidence | [Verify](../skills/workflow-verify/SKILL.md) |
| 9. Independent adversarial review | [Review](../skills/workflow-review/SKILL.md) |
| 10. Completion explanation | [Deliver](../skills/workflow-deliver/SKILL.md) |
| 11. Endpoint, two-way reconciliation and cost receipt | [Deliver](../skills/workflow-deliver/SKILL.md), [methodology](../skills/development-workflow/references/methodology.md) |
| 12. Continuity, blockers, cooldowns and capacity | [Coordinator](../skills/development-workflow/SKILL.md), [methodology](../skills/development-workflow/references/methodology.md) |

## Existing V10 skills and rules

| Source | Disposition |
|---|---|
| `problem-finding`, `grilling` | Adapted into workflow-intake: evidence, local vs recurring cause, falsifier, seven answers and one unresolved decision at a time. |
| `blast-radius` | Adapted into workflow-blast-radius: hidden consumers, pivotal safety fact, executed proof and explicit gaps. |
| `dry` | Adapted into workflow-dry: same-rule test, competing state writers, proposed owner, removals and scoped dispositions. |
| `surgical-patch` | Incorporated in workflow-build's tactical path. |
| `full-send` | Incorporated in the coordinator and delivery: whole-outcome ownership, real continuation, readback before retry, no false completion. |
| `verify-omalab` | General verification method incorporated in workflow-verify; Omalab routes, selectors, Ruby scripts and DB guard implementation remain V10-specific. |
| `create-verification-skill`, `maintain-verification-skill` | Methods incorporated in [verification recipes](../skills/development-workflow/references/verification-recipes.md); no new runtime or broad speculative feature map. |
| Code-quality guide | Rule/state/effect ownership and proportional pre-code explainer incorporated into plan, build and review. |
| Shipping, verification and agent-practices policies | Shared authorization, evidence, review, continuity and accounting rules retained in methodology and stage owners. |
| Migration and production-copy implementations | Only their relevant safety principles are carried into build/verify. Project-specific data-copy and migration commands must be supplied by the consuming repo. |
| `plan-loop-executor`, `plan-to-pr`, `bug-hunt` | Not runtime dependencies. The package uses the host's bounded delegation policy; it does not force an alternate executor, parallel-agent workflow or PR-only endpoint. |
| Product/GTM/browser-provider skills | Not needed for this methodology; not bundled. |

## Deliberate portability changes

- Setup discovers commands and policy owners. No V10 path, private home directory, framework, issue host, model name or provider is required at runtime.
- GitHub-specific commands, Rails test lanes, Kamal releases and a local board directory become project-native procedures. The proof obligations remain.
- Repo-specific verification maps stay with their app; this package supplies the method for building and maintaining them.
- Default workflow adoption is explicit and portable through a copied Markdown bundle and the chosen agent's instruction entry point. Installation is separate from adoption.
- Existing customers and compatibility requirements are discovered; V10's pre-customer direct-cutover assumption is not universalized.
- Interface parity applies to accepted project interfaces; libraries/docs do not acquire speculative web/API/CLI requirements.
- UI performance defaults remain for interactive paths; batch, native and hardware targets use the applicable agreed budgets and proof environment.
- An alternative to the HTML flow prototype requires an explicit decision when a non-web target cannot be meaningfully represented in HTML.
- No new enforcement framework, scheduler, completion hook or global agent configuration is installed.

These adaptations preserve methodology while making execution project-specific. They do not claim every host automatically loads Markdown, that a nonexistent reviewer is available, or that packaging validation proves agent compliance.
