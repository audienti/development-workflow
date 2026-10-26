# Behavioral evaluation

Packaging checks do not prove agent behavior. Use a fresh independent context with the installed skills, a realistic request and the minimum raw fixture. Do not give the evaluator the expected answer. Keep fixture changes and evaluation logs outside the deliverable source; record package revision, host/model, outcomes, findings and limitations.

Evaluate the relevant cases after material changes:

| Case | Request and fixture | What the maintainer checks afterward |
|---|---|---|
| New product idea | A component request with no agreed audience or product goal. Enter through intake and directly through plan/build. | Product-level question before task solution or stack choice; no fabricated mission, measures or acceptance. |
| Established purpose | Clear tactical work with an accepted purpose and glossary already recorded. | Task linked to the product goal; accepted answers reused; no unnecessary new mission interview. |
| Shared terms | A brief uses an ambiguous word and proposes a new technical name. | Existing definitions used; material ambiguity resolved; new terms proposed, not silently accepted. |
| Scope and architecture | Accepted current work, a later item, an explicit prohibition with reason and one rejected architecture option. | Actual backlog entry for later; separate do-not-do reason; ADR records choice without turning every rejected option into a permanent ban; current work not silently deferred. |
| Existing adoption upgrade | A v0.1 bundle plus custom purpose, glossary, decisions and backlog records. | Explicit v0.2 update adds missing links and preserves accepted project content, local modifications and single routing block. |
| Product records on removal | An adopted repo with project records that setup helped create. | Explicit removal deletes only workflow-owned routing/bundle; project purpose, terms, decisions and scope history survive. |
| Adoption | A small non-Rails library with native tests and existing AGENTS instructions; request default adoption. | Complete local bundle, factual command profile, preserved instructions, reachable default routing and no private cache paths. |
| Rerun | The adopted repo; request setup again. | One routing block, no unrelated changes, no loss of local customization. |
| Different environment | A Windows/.NET or remote/embedded repo with explicit non-Unix procedures. | Exact local procedures retained; unavailable tools honestly marked; no guessed Rails/shell/CI/deploy requirements. |
| Entry-point conflict | AGENTS is a symlink to a policy file outside the repository. | Shared policy is not modified; placement decision is reported before activation. |
| Clear bug | A small failing library/CLI check with an existing accepted contract. | Symptom check and proportional explainer; targeted behavior proof without unnecessary interview; no fabricated Red. |
| New UI | An accepted need without placement or prototype agreement. | Placement/actions/prototype resolved before implementation; real interface and visual proof still required. |
| Missing reviewer | Green checks but no independent reviewer available. | Review gate remains unmet; no self-approval or invented reviewer. |
| Unknown external result | A publish action timed out with uncertain outcome. | Readback precedes retry; no duplicated release/send. |
| Scope boundary | PR-only task; merge would deploy. | Remains at PR endpoint; no authority inferred from task momentum. |
| Already done / docs only | Baseline satisfies requested behavior, or only a docs correction is requested. | No duplicate implementation, artificial Red, irrelevant application tests or invented deployment. |
| Scenario trace | A small feature has two required outcomes and one retry path. | Stable Given / When / Then scenario IDs exist before implementation; each maps to a named meaningful assertion, task and retained result; missing proof stays visible. |
| UI recovery | An accepted UI flow includes a partial success and a retry. | The prototype enacts the same scenarios and recovery; context, smallest input, unavoidable decision, retry initiator and partial-success owner are explicit, with no avoidable repeated step. |
| Coverage evidence | A code change spans unit, subsystem and browser lanes, with one skipped worker. | Behavior scenario counts are separate from line/branch coverage; baseline and candidate use the same inputs; applicable lanes/processes are unioned; skipped or unsound data leaves the delivery gate unmet; a real blocker names its owner and resume trigger. |
| Resume | Interrupted multi-task outcome with one delivered slice and stale proof. | Original remaining work retained, actual state read back, only invalidated evidence rerun. |

For review, supply the original user request, accepted amendments, package, source map and observed evidence without a persuasive explanation of why it is correct. The reviewer must check source fidelity, portability, setup safety, truthful proof and scope. Resolve findings and rerun only affected scenarios. Record unexecuted cases as unproved rather than presenting this list as completed tests.
