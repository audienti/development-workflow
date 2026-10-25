---
name: workflow-review
description: "Obtain independent adversarial review of a current plan, implementation or evidence and resolve findings while preserving the accepted request and proof requirements."
---

# Challenge the artifact independently

Read repository instructions, the project profile and [shared methodology](../development-workflow/references/methodology.md). Establish the review obligation and current revision. The primary coordinates; delegates must not start their own reviewers.

## Choose a permitted reviewer

Prefer a different model family from the author, or an independent human reviewer. Use only available tools within the host's permissions and model/effort cost ceiling. Inspect effective wrapper defaults; no fixed provider or CLI is required.

If the preferred family is unavailable, stop any failed invocation before selecting a permitted alternative. A same-family independent instance is a recorded availability fallback. Author self-review is not independent review. If no independent reviewer is available, leave the gate unmet and report the specific missing capability; do not weaken it or repeatedly launch unchanged failures.

Keep one active reviewer per obligation. Use scoped rounds rather than councils or gratuitous parallelism. A separate visual obligation may require a reviewer that can actually inspect the saved images; prose about screenshots is not visual review.

## Give a neutral brief

Provide the original request and amendments, accepted requirements and exclusions, current artifact/revision, relevant source context, executed proof and known gaps. Give paths and reproduction instructions, not the author's persuasive rationale or desired verdict.

Ask the reviewer to check:

- Is the product-level purpose understood, including who it serves and the intended result, and does this task serve that purpose rather than only its local symptom?
- Are important terms defined and used consistently, with short plain communication and proposed terms kept separate from agreed meanings?
- Are consequential architecture choices recorded, later exclusions linked to real backlog entries, and do-not-do decisions kept separately with reasons? Did the change silently move a boundary or misclassify a rejected option?
- Do the requirements faithfully cover the request, including meaningful positive paths and protected behavior?
- Does the current artifact meet them, including permissions, state, side effects, failure/recovery and compatibility where relevant?
- Do tests and runtime checks detect plausible failure, and do their results apply to this revision and inputs?
- What accepted behavior or assertion did the change remove or weaken?
- Are owners clear, or did the change add duplicated rules, competing writers, obsolete paths or unnecessary machinery?
- Does delivery stay within the agreed endpoint and actual authorization?

Each finding needs a concrete failure or evidence gap, location, affected requirement and severity. Separate material corrections from optional simplification. A simplification proposal identifies removed paths, replacement owner, affected callers/data/jobs and preservation proof; a line-count reduction alone is not a reason.

## Resolve and recheck

Record findings and dispositions in the existing record. Fix a valid finding or respond with concrete evidence. A disputed finding stays open. A product tradeoff that changes accepted functionality goes to the user; neither party may agree away a requirement.

After changes, rerun affected proof and ask the same reviewer to recheck the changed artifact and unresolved findings. Do not repeat unchanged review scope. If rounds stop producing progress, identify whether the cause is a missing decision, evidence or tool capability; report a precise blocker instead of looping indefinitely.

Review is complete only when no material findings remain and the required phase proof is current. Agreement alone cannot replace an unrun check. Retain reviewer identity/model, independence/fallback reason, artifact revision, findings, dispositions and remaining limits, then route to [delivery](../workflow-deliver/SKILL.md).
