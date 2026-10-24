# Maintaining this plugin

This repository owns portable development-methodology instructions. Keep project-specific commands in the consuming repository's profile. Do not turn the package into a scheduler or enforcement service.

- Preserve scope, user authorization, existing project policy and meaningful proof.
- Keep the shared contract in `skills/development-workflow/references/methodology.md`; stage skills own their methods.
- Keep all runtime references within `skills/` so the bundle can be copied without private paths or external policy files.
- Preserve language, operating-system, agent and hosting independence.
- Run `python3 scripts/validate.py` after changes; validate the Claude manifest when that CLI is available.
- For material workflow changes, run relevant scenarios from `docs/evaluation.md` with an independent reviewer. Do not confuse packaging checks with behavioral proof.
- Update both manifest versions and `CHANGELOG.md` for releases.
- Do not change an adopting repository, deploy, send messages or mutate production merely because this plugin describes those actions.
