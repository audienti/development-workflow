# Project profile outline

Used by workflow-setup to write `.development-workflow/project.md`. Fill the relevant fields from source; omit irrelevant examples. Mark unknown capabilities explicitly. This outline is not an executable configuration or a new policy authority.

## Adoption

- Package version, source repository/revision, adoption date.
- Repository instruction owner and selected agent entry points; observed loading behavior.
- Existing policy conflicts and accepted resolutions, if any.

## Project and environment

- Purpose and actual customer interfaces.
- Languages/runtime versions, operating systems and supported development/build targets.
- Dependency/bootstrap owner and relevant manifest/configuration paths.
- Working directory and shell/tool context for each command. Remote/container/hardware prerequisites where relevant.

## Commands and proof

| Purpose | Exact command or documented procedure | Source | Status |
|---|---|---|---|
| Focused behavior checks | Project-native command | Owning file | Observed / executed with result / unknown / not applicable |
| Required local gates | Project-native commands | Owning file | As above |
| Remote checks | CI/job and readback procedure | Owning file | As above |
| Launch and health | Owned instance and readiness | Owning file | As above |
| Interface proof | Real customer actions and assertions | Owning file | As above |
| Cleanup | Stop only owned instances; retain evidence | Owning file | As above |
| Delivery and verification | Publish/release/deploy and confirm exact revision | Owning file | As above |

Commands are project facts, not permission to execute arbitrary production actions. Do not put credential values here. Native build/IDE workflows may use a documented procedure instead of a shell command.

## Policy links and decisions

- Task tracker, existing plan/board and durable evidence location.
- Protected behavior: permissions, tenancy, data, public interfaces and compatibility.
- Safe data/environment setup, reset and external-effect controls.
- Accepted surfaces requiring parity; UI/visual/performance budgets where applicable.
- Delivery endpoint defaults, merge/release side effects and separately authorized actions.
- Independent reviewer route, allowed delegation, available tools and model/cost ceilings.
- Usage telemetry availability and accounting source.
- Unknowns, their impact, owner and resume condition. Do not let a placeholder become a command or an implied approval.
