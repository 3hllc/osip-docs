# Diagram Standards

## Purpose

Diagrams are reviewable engineering source, not decorative screenshots. Their source belongs in Git beside the specification it explains, has a stated scope, and is updated when the represented boundary changes.

## Notation selection

| Need | Required notation |
| --- | --- |
| System, container, component, deployment, infrastructure, or network architecture | PlantUML, using C4 where it clarifies responsibility and boundaries. |
| Process, sequence, state, lifecycle, journey, simple relationship, or roadmap | Mermaid embedded in the relevant Markdown document. |
| Physical/reference-design placement | PlantUML or a versioned text/vector source with documented coordinate convention. |

## Content requirements

Each diagram names its level and audience, shows only the decision-relevant boundary, and labels interfaces with a protocol or contract type where useful. It distinguishes OSIP core services from external systems, shows trust boundaries for sensitive flows, and avoids implying a vendor dependency merely by using a vendor example.

Diagrams do not contain secrets, personal layouts, credentials, or unredacted production addresses. A diagram that includes a physical apartment plan uses the agreed privacy classification and access policy.

## Validation

PlantUML sources are rendered locally in CI to SVG before MkDocs collects files. Mermaid is rendered by the site theme from fenced source. A strict MkDocs build validates diagram links; an architectural change is incomplete if its diagram source, rendered asset, and specification diverge.

## Related documents

- [Documentation Standards](documentation-standards.md)
- [Architecture Overview](../architecture/architecture-overview.md)
