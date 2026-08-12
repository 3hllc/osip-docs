---
title: ADR-0008 - Integration Providers and a Canonical Semantic Boundary
status: accepted
date: 2026-08-12
deciders: [OSIP Project]
tags: [integration, providers, home-assistant, canonical-boundary]
---

# ADR-0008 - Integration Providers and a Canonical Semantic Boundary

## Context

OSIP must reuse useful device ecosystems without adopting their data models as its own. Home Assistant can accelerate discovery, local communication, dashboards, scenes, and broad vendor/protocol integration. Zigbee2MQTT, BACnet, KNX, MQTT bridges, Modbus, and vendor APIs offer different coverage and fidelity. Making any one of them mandatory would couple OSIP's physical identity, policy, applications, audit, and product lifecycle to an external product.

## Decision

OSIP introduces the `IntegrationProvider` abstraction and a canonical semantic boundary. A provider maps an external system into commissioned OSIP asset bindings, capabilities, canonical events, canonical commands, health, and bounded diagnostics. Above the boundary, OSIP uses only its own asset identity, capability contracts, events, commands, policies, intents, and application APIs. Raw payloads and provider identifiers remain below or beside the boundary with provenance and access controls.

Home Assistant is a first-class provider and the preferred MVP integration path. It is not mandatory for an OSIP deployment and never becomes the OSIP domain model, primary physical identity, or required critical execution path. Direct providers are added only when evidence shows an existing provider loses required information, cannot meet latency or availability requirements, cannot support a needed capability, or is not acceptable for a critical control path.

## Alternatives considered

| Alternative | Reason not selected |
| --- | --- |
| Make Home Assistant the OSIP foundation | Converts OSIP into a distribution or wrapper and imports HA lifecycle/entity assumptions into the product core. |
| Build all protocol drivers directly from the start | Delays validation, duplicates mature ecosystems, and creates unsupported operational breadth. |
| Expose raw provider payloads as the application API | Couples applications and automation to vendor details and prevents portable policy or audit. |

## Consequences

Providers, mappings, health, raw diagnostic retention, and contract tests become explicit product work. A provider command acknowledgement is not treated as physical completion; providers report dispatch and observed outcome separately. The model allows multiple bindings for one asset, with explicit primary, observability, convenience, and fallback roles. It preserves the ability to replace, augment, or operate without Home Assistant while still using it where it is valuable.

## Links

- [Integration Providers](../docs/en/architecture/integration-providers.md)
- [Physical Asset Model](../docs/en/architecture/physical-asset-model.md)
- [ADR-0003 Home Assistant Integration Platform](0003-home-assistant-integration-platform.md)
