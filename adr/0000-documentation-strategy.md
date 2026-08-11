---
title: ADR-0000 - Documentation Strategy
status: accepted
date: 2026-08-07
deciders: [OSIP Project]
tags: [documentation, governance, mkdocs]
---

# ADR-0000 - Documentation Strategy

## Context

OSIP needs durable engineering memory that supports review, versioning, diagrams, research, decisions, and published documentation. Chat conversations and generated sites are useful working and presentation surfaces but cannot be the authoritative record.

## Decision

The OSIP documentation repository is the canonical source of knowledge. Documentation is maintained as versioned Markdown and text-based artifacts in Git. MkDocs Material and GitHub Pages publish a generated view of that source.

Each topic has one canonical location. ADRs live in `adr/`, research in `research/`, diagrams in `diagrams/`, bills of materials in `bom/`, and reusable templates in `templates/` or the canonical folder that owns them.

## Alternatives considered

| Alternative | Reason not selected |
| --- | --- |
| GitHub Wiki as the primary source | Does not provide the desired repository structure and review workflow for all engineering artifacts. |
| Published documentation site as the primary source | Generated output cannot be reviewed and versioned as the complete source of truth. |
| Separate documents outside Git | Encourages drift and makes collaboration and history difficult. |

## Consequences

### Positive

- One reviewable, versioned knowledge base.
- Published documentation can be recreated from Git.
- Architecture, research, and implementation stay traceable.

### Negative and risks

- Contributors must maintain documentation with changes.
- Navigation and publishing configuration require ongoing care.

## Implementation notes

- Use `mkdocs.yml` with MkDocs Material for the initial published site.
- Treat the GitHub Pages deployment as generated output.
- Add ADRs for future changes to this strategy.
