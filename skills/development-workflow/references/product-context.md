# Product context

Read this reference with the repository's project profile and shared [methodology](methodology.md). Use it when this workflow is adopted or explicitly requested. Repository instructions and existing authority still govern the work.

Product context comes before task intake. A task can be well executed and still move the product away from its purpose. The agent must understand the product goal, then show how the proposed task supports it or identify the unresolved choice.

## Establish the product goal first

Before asking task-specific questions or proposing design, read the repository's recorded product purpose and the accepted task record. Reuse facts and decisions already agreed. Do not repeat an interview when the product goal is clear and the task is tactical.

For a new product, idea, or repository with no purpose record, establish the goal with evidence and one consequential question at a time. Cover:

1. **Who is served?** Name the people, organizations, or other users the product exists to help.
2. **What larger problem do they have, and why does it matter?** Use the user's evidence and words. Separate observed facts from beliefs.
3. **What result or value should the product create?** Describe a meaningful change for the people served.
4. **What is the high-level solution or concept?** State how the product is expected to create that result, without prematurely choosing implementation details.
5. **What evidence would show success?** Name observable evidence. Reuse existing measures where accepted. Do not invent numeric targets or claim evidence that does not exist.
6. **What are the product boundaries?** Record the intended scope, protected interests, and explicit exclusions that have been decided.

A missing answer is not an invitation to guess. If it could change whether or how the task should proceed, ask one consequential question and wait before dependent planning, design, or implementation. Continue independent fact finding. Label lesser gaps as unknown and keep their effect visible.

At intake and resume, link the task to the product purpose: explain which user need and intended result it advances, what it preserves, and whether it changes an accepted boundary. If the connection is weak or absent, state that plainly and resolve the product decision before planning the task. Preserve existing agreement; do not make the developer restate it.

Keep the product-purpose record short and evidence-backed. Name its owner and last review date. Mark each statement as an observed fact, an accepted product decision, a proposal, or an unknown when that distinction matters. Link claims to their source when available. A discovery or change in evidence does not itself change an accepted product decision; record the evidence and ask the product owner when the decision must change.

When an accepted purpose or boundary changes, record what changed and why, and link the prior decision so its history remains clear. Revisit open task plans whose outcome depends on that decision. Keep task-specific behavior and implementation choices in the task record; link them to product purpose instead of copying a second version of it.

Use the workflow stages in order: establish product context, then do task-specific [intake](../../workflow-intake/SKILL.md), then plan. If a material product choice appears during intake or planning, return to that choice before dependent work. This does not require a new approval round for an already accepted goal or a clear tactical task.

## Communicate in plain language

Aim for about 80–85% simple, direct wording inspired by ASD-STE100. This is a user communication preference, not an official compliance percentage or claim of ASD-STE100 certification. Use short active sentences, familiar words, and one main point per sentence. Keep exact code, product, and technical names when they are needed for accuracy. Expand an acronym at first use and explain important domain terms that are outside familiar vocabulary.

See the [ASD-STE100 overview](https://asd-ste100.org/) and [about ASD-STE100](https://asd-ste100.org/about_STE.html). The standard permits project-specific technical terms. Do not replace precise product or code terms with vague wording.

## Keep one shared glossary

Every adopted project must have one authoritative glossary owner. Reuse the repository's current glossary and its established location. Link to it from the project profile and relevant task records. Do not create a competing glossary in the plugin, profile, task, or a second docs folder.

For each important product, domain or specialized technical term outside the plain vocabulary, record the canonical term, a plain definition, a short example when useful, and distinctions from nearby terms that people may confuse. Define an ordinary word too when the project gives it a special meaning. Record established aliases and point them to the canonical term; use one agreed name for the same concept. Keep exact code identifiers when they differ from user-facing language, and explain the relationship.

Agents must use established terms consistently. A new term or a proposed change to meaning stays **proposed** until the product owner agrees. Do not silently add a term as if it were accepted. Ask one consequential question when ambiguity can change product behavior, scope, or architecture; otherwise mark the term proposed and continue independent work.

## Record architecture decisions

An Architecture Decision Record (ADR) records a meaningful choice about the product's architecture: a choice that shapes boundaries, dependencies, state ownership, interfaces, or future change. Reuse the repository's ADR format and index. Do not create an ADR for every routine coding choice.

A useful ADR includes:

- a stable identifier and title;
- context and the problem the decision addresses;
- the options considered, including relevant tradeoffs;
- the chosen option and reasons;
- consequences, constraints, and any follow-up;
- status, date, decision owner, and links to affected plans or records.

Mark a proposed choice as proposed until it is accepted. Update or supersede an existing ADR when the decision changes; preserve its history and link the replacement. An ADR that rejects an option records the architecture decision. It does not, by itself, add that option to the product's permanent do-not-do list.

## Keep scope dispositions distinct

Record scope in the accepted task plan and link to existing backlog or product records. Use these meanings:

- **Now** means accepted work in the current plan. Keep the complete parent outcome visible if it has several slices.
- **Later** means excluded from the current plan and explicitly tracked in the backlog. Give the item a description, reason, owner, and revisit condition. If an owner or condition is unknown, say **unknown**; do not invent a date or schedule.
- **Never** means an explicit product do-not-do decision. Record the prohibited scope, reason, and source of the decision in the separate do-not-do record. A user must explicitly supersede the decision before it changes. Preserve the previous decision and its history.
- **Unresolved** means no disposition has been accepted. Keep the choice open and ask before dependent work. Do not relabel it Later or Never to make the plan look complete.

Removing accepted work from Now requires an explicit, accepted scope change. Update the task record and relevant backlog or do-not-do record. Do not silently shrink the task. A Later item is not a promise or schedule. A Never decision is not inferred from an ADR, a missing feature, or an agent's preference.

## Reuse records and preserve them

Prefer records that already own the information: the tracker or plan for task scope, the product glossary for terms, the ADR index for architecture choices, and the project profile for links and local workflow facts. Avoid copies that can drift.

If the repository lacks an owner, create only the smallest useful, repository-owned record needed for the accepted work. Mark unverified facts as **unknown** and new decisions as **proposed**. Do not create five empty files and treat them as ready. Suitable defaults, when needed, are:

- `docs/product-purpose.md` for product purpose and boundaries;
- `docs/glossary.md` for the shared glossary;
- `docs/decisions/README.md` as an ADR index, with individual ADRs alongside it;
- the existing tracker backlog, or `docs/backlog.md` only when no backlog exists;
- `docs/do-not-do.md` for explicit Never decisions.

The project profile links to these records and names their owners; it does not duplicate their policy or contents. Keep product records in project-owned docs or the existing tracker, outside the copied skill bundle, so they remain available if this plugin is removed. A package upgrade may add guidance, but must preserve project-owned purpose, glossary, ADR, backlog, and do-not-do records. Do not replace accepted facts or decisions with defaults during setup or upgrade.
