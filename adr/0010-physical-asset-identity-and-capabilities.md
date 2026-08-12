---
title: ADR-0010 - Physical Asset Identity and Capability Model
status: accepted
date: 2026-08-12
deciders: [OSIP Project]
tags: [domain, identity, assets, capabilities, digital-twin]
---

# ADR-0010 - Physical Asset Identity and Capability Model

## Context

Device-centric integration systems commonly use an entity ID, topic, protocol address, or vendor resource as the practical identity of a thing. That identity changes when integrations change and cannot express the difference between a physical HVAC asset, a field controller, its capabilities, its space, and its several possible control/observation paths. OSIP needs a model that remains valid for residential, commercial, and managed-space deployments.

## Decision

OSIP owns stable identities for sites, spaces, assets, capabilities, and typed relationships. A physical or virtual asset has a stable `asset_id`; its provider identities are explicit bindings with health, lifecycle, provenance, and operational role. The domain expresses capabilities rather than protocol primitives. A site containment hierarchy and a typed relationship graph coexist so that service, access, safety, observation, adjacency, and control relationships are not encoded as tags.

## Alternatives considered

| Alternative | Reason not selected |
| --- | --- |
| Use provider entity IDs as domain identities | Breaks audit, policy, history, and applications when a provider or address changes. |
| Treat every device as the only modelled asset | Cannot model engineering equipment, circuits, doors, logical assets, or multi-device systems correctly. |
| Postpone the capability model | Forces automation and applications to depend on protocol/vendor semantics and makes migration costly. |

## Consequences

Commissioning becomes an explicit verification process that links discovered endpoints to assets, locations, capabilities, and control roles. Providers must maintain mapping and compatibility evidence. Multiple bindings are supported by design, while selection is made by policy-scoped execution planning rather than discovery order. This increases model and commissioning discipline but creates portability across providers and applications.

## Links

- [Physical Asset Model](../docs/en/architecture/physical-asset-model.md)
- [Digital Twin](../docs/en/architecture/digital-twin.md)
- [Device Model](../docs/en/architecture/device-model.md)
