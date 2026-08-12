# Constraints

## Purpose

Constraints are non-negotiable or presently binding conditions that shape the solution space. They differ from preferences: changing a constraint needs new authority, evidence, or a superseding decision. A design must name the constraints it relies on so that later changes can be assessed deliberately.

## Current constraints

| ID | Constraint | Source or rationale | Architectural effect |
| --- | --- | --- | --- |
| C-001 | Essential automation and device control must continue on the trusted local environment during WAN loss. | Local First project principle. | Core identities, control paths, selected local transport, integration providers, required state, policy, and deterministic execution cannot depend solely on cloud services. |
| C-002 | Cloud capabilities are additive and explicitly classified. | Cloud Enhanced project principle. | Remote access, backup, analytics, and AI may use cloud services only with a defined degraded local mode and privacy boundary. |
| C-003 | Domain contracts must remain independent of vendors and individual adapter topic formats. | Vendor Agnostic project principle. | Integrations pass through adapters; vendor payloads cannot become the general API or spatial model. |
| C-004 | Documentation is versioned, reviewable source in Git and the published site is generated from it. | Docs as Code decision and ADR-0000. | Markdown, text diagrams, ADRs, and validation steps are part of delivery; edits to generated site output are not authoritative. |
| C-005 | Sensitive credentials, network keys, device backups, and personal data must not be committed to Git. | Security and privacy principle. | Secrets require an external controlled store; documents reference procedures and redacted examples only. |
| C-006 | The initial platform is validated through a real 165 m² reference apartment before being presented as a repeatable installer product. | Product roadmap. | Designs require physical evidence, commissioning records, and recovery tests rather than only simulated success. |
| C-007 | Safety-relevant control must provide manual override and conservative failure behaviour. | Safety project principle. | Actuator integrations need explicit hazard analysis, access control, observability, and safe state definitions. |

## Change control

A proposed change to a constraint identifies the affected ADRs, specifications, reference designs, and tests. It is reviewed as an architecture decision, not folded into an implementation pull request. Temporary exceptions state their scope, compensating control, expiry or review trigger, and owner.

## Related records

- [Project Charter](../foundation/project-charter.md)
- [Project Principles](../foundation/project-principles.md)
- [Assumptions](assumptions.md)
- [Risks](risks.md)
