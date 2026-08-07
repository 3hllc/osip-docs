# ADR Process

## Purpose

An Architecture Decision Record preserves the context and consequences of a significant choice. ADRs prevent important reasoning from being lost in chats, issues, or implementation details. They are stored in the repository-level `adr/` directory and numbered sequentially.

## When an ADR is required

Create an ADR when a decision changes a foundational principle, cross-service boundary, data or security model, local/cloud responsibility, supported technology direction, compatibility promise, operational model, or a choice that will be expensive to reverse. Small implementation choices belong in code review, a specification, or the decision log.

## Lifecycle

1. Describe the context, decision drivers, constraints, alternatives, and consequences.
2. Mark the record `proposed` while evidence or review is incomplete.
3. Mark it `accepted` only when the project intentionally adopts it.
4. Mark a record `superseded` rather than rewriting history; link its successor.
5. Update affected specifications, diagrams, risks, tests, and runbooks in the same change.

## Minimum content

An ADR has a title, status, date, deciders, context, decision, alternatives considered, and consequences. Consequences include negative effects, migration work, observability, privacy/security effects, and rollback or review trigger where relevant. The ADR template is the starting point, not a substitute for reasoning.

## Review test

Reviewers ask whether the decision preserves Local First, vendor independence, explicit contracts, safety and privacy boundaries, and commercial repeatability. A decision conflicting with a project principle must name the exception, compensating control, owner, and revisit condition.

## Related documents

- [Documentation Standards](documentation-standards.md)
- [Decision Log](../knowledge/decision-log.md)
- [Project Principles](../foundation/project-principles.md)
