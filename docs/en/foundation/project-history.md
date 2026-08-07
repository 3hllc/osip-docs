# Project History

## Origin

OSIP began with the practical question of how to build a resilient, intelligent apartment rather than a collection of disconnected smart-home devices. The initial reference environment is an approximately 165 m² apartment with substantial engineering scope. Early discussions covered Zigbee, HVAC, leak protection, lighting, access, cameras, voice, robots, local compute, and cloud services.

The project deliberately expanded beyond a one-off installation. The apartment is the first laboratory and proof environment; the reusable models, contracts, installation practices, and operational evidence are the product assets.

## Founding decisions

The following decisions were established before implementation and remain the baseline:

| Decision | Rationale | Durable result |
| --- | --- | --- |
| Build a platform, not a Home Assistant distribution. | A controller alone does not provide a portable spatial model, integration contracts, or an installer-grade operating model. | OSIP owns the domain model, policy boundaries, and documentation; Home Assistant is an integration component. |
| Start with a real reference apartment. | Architecture must be exposed to physical installation, RF, reliability, safety, and daily-use constraints. | Reference design, commissioning evidence, and recovery tests precede productization. |
| Operate Local First and become Cloud Enhanced. | Core comfort, access, safety, and automation cannot be contingent on WAN availability. | Local services are the normal control path; cloud is additive and explicitly degraded. |
| Use event-driven boundaries. | Devices and integrations must evolve independently. | MQTT is the initial event backbone behind versioned OSIP contracts. |
| Treat space and context as first-class. | A device-centric system cannot express intent, zones, objects, or robot tasks robustly. | Spatial model and digital twin are core architecture concepts. |
| Make AI native but runtime-optional. | AI is a strategic differentiator, but it must not become a safety or availability dependency. | AI is designed into contracts, data governance, and user experience; essential deterministic paths work without it. |
| Treat documentation as source. | Decisions otherwise disappear into conversations and vendor configuration. | Git, ADRs, Markdown, PlantUML, Mermaid, review, and generated documentation are the project memory. |

## Evolution path

The expected evolution is Reference Apartment → Installer Edition → Commercial Installations → OSIP Platform → Spatial Intelligence Ecosystem. Each transition is evidence-driven: a pattern graduates only after it has been installed, observed, recovered, and documented well enough for another authorized party to reproduce it.

## Historical interpretation rules

This page explains why the project exists; it does not supersede current ADRs or specifications. Earlier named products and technology choices are historical candidates unless a current ADR or standard accepts them. New information is added as a dated milestone or converted into a decision, research record, risk, or requirement rather than rewriting the origin story.

## Related documents

- [Project Charter](project-charter.md)
- [Vision](vision.md)
- [Project Principles](project-principles.md)
- [Knowledge Extraction](../knowledge/knowledge-extraction.md)
- [Roadmap](../strategy/roadmap.md)
