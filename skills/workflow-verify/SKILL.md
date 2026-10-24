---
name: workflow-verify
description: "Prove accepted behavior using project-native tests and real customer interfaces; retain current correctness, visual and performance evidence before claiming completion."
---

# Prove the accepted behavior

Read the repository instructions, project profile, [shared methodology](../development-workflow/references/methodology.md), accepted requirement-to-proof table and current artifact. Name the expected outcomes and protected behavior before executing checks. Do not redefine acceptance to fit observed behavior.

## Select the real proof

- Library: exercise the public callable contract and relevant compatibility/error cases with the native test tools.
- CLI: run real commands; assert exit status, output, saved state and relevant side effects.
- Backend/API: use integration tests for shared business outcomes, permissions, tenant boundaries where applicable, persisted state, jobs and side effects. Route existence is not behavior proof.
- UI: use the actual controls through a browser or native driver; prove navigation, usable results and saved effects. Retain before/after images and independent visual review against the agreed prototype. Backend tests do not replace interface proof.
- Infrastructure, embedded or other outputs: use the accepted target/environment and observable success conditions. A simulator can supplement but cannot silently replace required hardware or production proof.
- Documentation: verify consistency, references and realistic use. Do not invoke an application suite or deployment that does not serve the accepted task.

Apply parity only to the accepted interfaces. Shared capability should use shared business rules; do not invent an API or UI for a library just to satisfy a template.

## Execute with comparable inputs

Establish baseline and candidate on the same named scenarios and representative data. Record revisions, environment, inputs and any transformation/reset recipe. Use synthetic or sanitized data unless a production-shaped copy is separately authorized. Keep development isolated from production and block unintended external effects.

Run focused assertions, then each required local/remote gate. Distinguish fast checks, broad regression and runtime/UI/performance proof when the repo has those lanes; use its actual names and commands. If there is no CI, record that fact and the agreed alternative proof rather than claiming CI passed.

Separate behavior coverage from line/branch coverage. Inspect uncovered changed code and affected high-risk paths; verify the measurement includes the intended test lanes and parallel workers before relying on a percentage. Never exclude production code or weaken assertions to improve the number.

For performance, retain raw first-load and repeated warm measurements to the correct usable result, sample count, outliers and concurrency. Compare the same inputs and declared budgets. Never discard slow attempts or replace the baseline to get green. A faster local run does not prove production latency. Correctness, visual quality and speed each need their own result.

Use existing harnesses. If a repeatable project-specific recipe is missing, read [verification recipes](../development-workflow/references/verification-recipes.md) to create only the needed recipe. Do not generate a new framework or speculative feature map as part of ordinary proof.

## Retain evidence and gaps

Each result identifies requirement, check, command/procedure, assertion, tested revision, declared inputs, environment, timestamp and outcome. Retain failures, skips and missing prerequisites. A zero exit code with no meaningful success assertion is insufficient. Check that a meaningful bad case is detected; do not trust a no-op checker.

Mocks and offline request replays are useful at isolated external boundaries. State what they skip. They supplement rather than replace any agreed real-path proof. Do not trigger an external mutation to gain evidence without authorization.

Bind evidence to the current artifact and contract. A changed file, assumption or input invalidates affected proof; retain unaffected valid results. Preserve screenshots/logs after teardown and keep private data out of public artifacts.

Return requirement-by-requirement results: Green, failed/Red, Not run or Blocked, with refactor/review/delivery recorded separately. Pass the current evidence to [independent review](../workflow-review/SKILL.md). Missing required proof keeps completion open.
