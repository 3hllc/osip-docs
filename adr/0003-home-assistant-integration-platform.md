---
title: ADR-0003 — Home Assistant Is an Integration Platform, Not the OSIP Core
status: accepted
date: 2026-08-07
deciders: [OSIP Project]
tags: [integration, vendor-independence, home-assistant]
---

# ADR-0003 — Home Assistant Is an Integration Platform, Not the OSIP Core

## Context

Home Assistant can accelerate device integration, local automation, and reference-apartment delivery. Defining OSIP in terms of Home Assistant, however, would make a third-party product's data model, lifecycle, and deployment assumptions the platform's architecture.

## Decision

Home Assistant may be used as a supported integration and experience component. OSIP's canonical domain concepts, event contracts, spatial model, policy, and product boundaries remain independent. Integration occurs through documented adapters and contracts; Home Assistant entity identifiers are external references, not primary OSIP identities.

## Alternatives considered

| Alternative | Reason not selected |
| --- | --- |
| Build all integrations from scratch | Delays validation and discards a mature ecosystem without proving a need. |
| Make OSIP a Home Assistant distribution | Prevents product independence and makes Home Assistant's internal model the platform model. |
| Avoid Home Assistant entirely | Removes a valuable reference implementation and installer ecosystem. |

## Consequences

Adapter work and model translation are intentional costs. The result is a credible migration path if Home Assistant is replaced, augmented, or used differently across products.

## Links

- [Architecture Overview](../docs/architecture/architecture-overview.md)
- [ADR-0005 Vendor Agnostic Components](0005-vendor-agnostic-components.md)
