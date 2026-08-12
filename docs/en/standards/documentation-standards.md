# Documentation Standards

## Purpose

Documentation is an engineering deliverable and OSIP's long-term memory. Markdown and text diagram sources in Git are authoritative. MkDocs Material and GitHub Pages render a convenient, generated view; generated pages are never edited as a separate source.

## Canonical locations

| Artifact | Canonical location | Rule |
| --- | --- | --- |
| Foundation, strategy, specifications, guides | `docs/` | One topic, one canonical page; use links instead of copies. |
| Architecture decisions | `adr/` | Numbered sequentially; accepted records are superseded, not rewritten. |
| Research evidence and evaluation | `research/` | State question, sources, method, findings, limits, and resulting decision. |
| C4 and infrastructure diagrams | `diagrams/*.puml` | PlantUML source is versioned with the document that references it. |
| Process, sequence, state, and journey diagrams | Markdown Mermaid fences or `diagrams/*.mmd` | The textual source is reviewable and has a named owner. |
| Equipment choices | `bom/` | Include model, compatibility, lifecycle, and decision links. |
| Deployment and operational execution | `deployment/` | Pair executable artifacts with human-readable runbooks. |

## Lifecycle

The default sequence is: idea → architecture → ADR (when material) → specification → implementation → tests and operational evidence. A pull request changing a system behaviour updates the associated specification, diagram, ADR impact, and runbook in the same change whenever applicable.

## Writing requirements

Documents use a clear title, purpose, status where it matters, scope, and links to related decisions. State facts separately from proposals and assumptions. Requirements use observable language: prefer “must continue local operation during WAN loss” to “should be reliable.”

Do not create placeholder pages for a decision that is ready to be documented. If a subject is genuinely unresolved, create a short question record that names the owner, needed evidence, decision deadline or trigger, and links to the relevant ADR or research.

## Diagrams

Use PlantUML for C4, deployment, component, infrastructure, and network views. Use Mermaid for flows, sequences, states, journeys, timelines, and simple relationships embedded in Markdown. Diagrams identify their scope and source file, and must not duplicate diverging copies of an architecture model.

## Language policy

English is the canonical language for platform specifications and ADRs to make the repository broadly usable. Every English documentation page has a structurally equivalent Russian translation. Russian pages must link to the English canonical record, include a translation status/date, and be updated in the same change as their English source. CI verifies the paired file paths and current translation metadata; review verifies the translated meaning.

## Review checklist

- Is this the canonical place for the fact?
- Does the change require an ADR or update the consequences of one?
- Are assumptions, security/privacy effects, and operational impacts explicit?
- Do linked diagrams and navigation still resolve?
- Was the Russian translation updated with the English source, with the same decisions, diagrams, and links?
- Does the change leave a future installer or operator with enough evidence to understand it?
