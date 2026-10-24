# Project-specific verification recipes

Use when an accepted customer path has no reliable recipe, or an existing recipe has drifted. Reuse the current harness and its policy owner. Do not copy V10's launch scripts, database rules or feature selectors into another project.

## Create or extend a recipe

Interview the repo: find the surface, exact launch/build command, safe data setup, authentication procedure, real driver and relevant source/test paths. Discover the target environment and instance ownership. Missing or broken prerequisites remain explicit; do not publish guessed steps as verified.

Store the recipe in the repo's existing verification guide/skill or the location selected during setup. Include only what the next agent needs:

1. **Launch:** exact environment and command/procedure; readiness and teardown.
2. **Health:** read-only check for the correct revision, owned instance, destination and authentication. Recheck after surprising results; do not drive a foreign instance.
3. **Drive:** real customer actions and stable selectors/API calls/CLI invocations. Backend edge cases stay in backend tests; interface checks prove wiring and usable outcomes.
4. **Evidence:** accepted scenario IDs, expected assertions, persisted effects, comparable baseline/candidate data, images and timings when relevant, and durable artifact locations.
5. **Cleanup:** stop only what this run started, including bounded jobs; preserve the evidence. Never kill all processes with the same name or run all copied pending work.

Execute at least one complete accepted scenario, inspect its assertions, clean up and confirm the evidence still exists. A recipe that has never run is a draft, not verified capability.

## Maintain a recipe

For a focused update, check the changed scenarios and affected neighbors. For an explicitly requested full map audit, cover every mapped feature from source and through the real interface. Report the actual scope; do not call a subset a full audit.

Separate documentation drift, a harness gap and a product regression. Correct a recipe against accepted behavior; do not rewrite expectations to hide a product defect. Limit edits to the recipe/harness unless product repair is authorized. Drive every changed recipe again before calling it fixed.

Keep one owner for the live instance. Check health before first drive and after a failure. Clean up failed iterations. Mark unreachable scenarios unproved with their real prerequisite; knowing why a check is unreachable is not a pass.
