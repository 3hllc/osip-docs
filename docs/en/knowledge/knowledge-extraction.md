# Knowledge Extraction from the Founding Conversation

## Purpose

This record converts the founding “What is Zigbee” conversation into durable project knowledge. It is intentionally a decision map, not a transcript. The authoritative form of an accepted decision is its ADR or specification; a technology listed as a candidate remains a hypothesis until validated.

## Extracted architectural knowledge

| Area | Accepted direction | Authoritative destination |
| --- | --- | --- |
| Product identity | OSIP is the Open Spatial Intelligence Platform, not another smart-home controller. | Project Charter and Vision |
| Local operation | Essential control remains available locally; cloud enhances remote access, heavy inference, backup, analytics, and fleet capabilities. | ADR-0001 and Architecture Overview |
| Component boundaries | Components communicate through explicit events and contracts; direct vendor coupling is avoided. | ADR-0002 and Event Model |
| Initial implementation candidates | Home Assistant, MQTT, Zigbee2MQTT, Docker, Grafana, local compute, and selected databases are useful candidates, not architectural ownership boundaries. | ADR-0003, ADR-0004, Technology Radar |
| Physical integration | Zigbee is one local device-network option; its mesh is distinct from MQTT transport. | Zigbee Mesh and MQTT Bridge |
| Spatial intelligence | Spaces, zones, objects, devices, people, robots, and contextual relationships have durable meaning. | ADR-0006, Context Model, Digital Twin |
| AI | AI is architecturally native; local deterministic and safety paths do not depend on it. | ADR-0007 and AI Architecture |
| Commercialization | The reference apartment validates repeatable patterns for Installer Edition and commercial deployments. | Product Strategy and Reference Apartment |
| Documentation | Git is the project memory; Markdown sources, ADRs, diagrams, review, and generated site are the evidence trail. | ADR-0000 and Documentation Standards |

## Explicit design guardrails

- No external vendor, broker, automation controller, cloud provider, model, coordinator, or database owns the OSIP domain model.
- A device report is not a contextual fact until an adapter identifies its source, capability, time, quality, and relationship to a space.
- MQTT delivery and Zigbee delivery do not prove physical completion; commands require observable completion semantics.
- AI recommendations are typed intents subject to policy, authorization, audit, and human override.
- Every installation lesson becomes a reference-design, operational, or installer artefact instead of remaining private experience.

## Candidate, not decided

Specific compute hardware, database products, Matter adoption scope, ESPHome use, camera model, lock model, HVAC controller, and cloud provider were discussed as possible directions. They must be evaluated through research records and a capability/compatibility matrix before they become BOM selections or product commitments.

## Follow-up records

This extraction creates the initial research backlog: technology radar, reference-apartment engineering design, integration standards, operations/installer procedures, AI capability roadmap, and commercial strategy. Each has been created as a separate site section so that the founding rationale and the evolving evidence remain linked but distinct.

## Related documents

- [Project History](../foundation/project-history.md)
- [Research Summary](research-summary.md)
- [Technology Radar](technology-radar.md)
- [Open Questions](open-questions.md)
