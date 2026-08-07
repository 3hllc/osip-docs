---
title: OSIP Project Charter
status: accepted
version: 1.0
date: 2026-08-07
---

# OSIP Project Charter

## Authority and purpose

This Charter is the governing statement for the Open Spatial Intelligence Platform (OSIP). It establishes the product's mission, durable decision principles, and Phase 0 direction. The OSIP knowledge-base repository is the canonical storage for this Charter and all related engineering knowledge; an accepted ADR is required to intentionally change a material architectural decision.

The Charter does not prescribe a vendor, a final product implementation, or a complete apartment design. It constrains those choices so that short-term delivery does not compromise the platform.

## Mission

Build an open platform that transforms physical spaces into intelligent environments. OSIP brings together engineering systems, IoT devices, automation, robotics, AI, and a digital representation of space while retaining reliable local operation and meaningful human control. The first validation profile is residential, but OSIP's platform model is designed to be applicable to apartments, houses, offices, hospitality, healthcare, campuses, industrial environments, and other spaces once their domain-specific requirements are explicitly designed.

OSIP is not another collection of device dashboards, a Home Assistant distribution, or a cloud service that happens to control a home. It is a platform that can reason about the relationship between people, places, objects, events, context, and tasks. External products contribute capabilities; OSIP owns the architectural model and integration boundaries.

## Product and business direction

The first installation is an approximately 165 m² reference apartment. It is an engineering laboratory, validation environment, demonstrator, and source of real installation requirements—not the end product. The platform is designed for a commercial business and for a useful progression:

```mermaid
flowchart LR
  A[Reference Apartment] --> B[Installer Edition]
  B --> C[Commercial Installations]
  C --> D[OSIP Platform]
  D --> E[Spatial Intelligence Ecosystem]
```

Each stage must deliver customer value, produce reusable knowledge or product capability, and preserve the longer-term architecture. A technically attractive feature without user, installer, operational, or commercial value is outside the current priority.

## Decision principles

| Principle | Required outcome |
| --- | --- |
| Local First | Safety- and comfort-critical functions continue when the Internet, cloud services, or a remote account are unavailable. |
| Cloud Enhanced | Cloud may add remote access, large-scale analytics, backup, and optional inference; it cannot be a single point of failure for local life safety, comfort, or control. |
| Event Driven | Components publish facts and react through explicit events instead of fragile point-to-point coupling wherever practical. |
| AI Native | AI is a first-class capability for understanding, recommendation, and orchestration, but ordinary operation never depends on AI availability. |
| Spatial Native | The model begins with spaces, zones, physical relationships, and semantic meaning—not only device IDs. |
| Vendor Agnostic | Devices, brokers, clouds, models, and integration products are replaceable behind explicit boundaries. |
| Open Standards First | Prefer stable, documented standards and portable contracts. Proprietary integrations are isolated adapters, not the domain model. |
| Security by Design | Identities, least privilege, segmentation, updates, auditability, and secure defaults are design inputs. |
| Privacy by Default | Local data processing and data minimisation are defaults; external sharing is explicit, scoped, and reversible. |
| Docs as Code | Architecture, decisions, specifications, diagrams, and operating knowledge are versioned reviewable artifacts in Git. |
| API and Testability First | Boundaries are contractable and verifiable; hidden UI-only integrations are not a platform interface. |
| Observability by Design | Operators can establish health, provenance, timing, and the reason for consequential actions. |

## Scope boundaries

Phase 0 establishes the documentation system, architecture baseline, core models, ADR foundation, technology direction, and reference-apartment design. It may use Home Assistant, MQTT, Zigbee2MQTT, ESPHome, Docker, Grafana, and similar tools as implementation candidates.

Those products are not platform-defining dependencies. Hardware procurement, detailed vendor selection, and production cloud construction follow only when requirements and acceptance criteria are documented.

## Governance

1. Propose the architecture or product change in the appropriate canonical document.
2. Record consequential or difficult-to-reverse choices in an ADR, including alternatives and consequences.
3. Review the change for reliability, maintainability, security, privacy, installer experience, and commercial viability.
4. Implement only after the decision and specification are coherent.
5. Update the documentation and runbooks as part of any implementation change.

Accepted ADRs are historical records. Do not rewrite their decisions to make history appear different; supersede them with a new ADR and link the two records.

## Success criteria

OSIP succeeds when a reference installation remains usable during cloud loss, its decisions and topology are explainable to an installer, its integrations can be replaced without rewriting the core model, and each validated capability can be carried into a repeatable commercial deployment.

## Related records

- [Project principles](project-principles.md)
- [Architecture overview](../architecture/architecture-overview.md)
- [Product strategy](../strategy/product-strategy.md)
- ADR index: `adr/README.md` at the repository root
