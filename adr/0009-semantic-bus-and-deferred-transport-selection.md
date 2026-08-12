---
title: ADR-0009 - Semantic OSIP Bus and Deferred Transport Selection
status: accepted
date: 2026-08-12
deciders: [OSIP Project]
tags: [events, transport, mqtt, architecture]
supersedes: ADR-0004
---

# ADR-0009 - Semantic OSIP Bus and Deferred Transport Selection

## Context

ADR-0004 selected MQTT as the initial event backbone for the Reference Apartment. MQTT remains useful for constrained local networks and integrations such as Zigbee2MQTT. The platform now needs a stronger distinction: the OSIP bus is the canonical event/command boundary, while transport selection depends on delivery guarantees, ordering, idempotency, replay, durability, request/response behaviour, operational complexity, and site constraints that must first be specified.

## Decision

OSIP defines a transport-independent semantic bus for canonical events and routed commands. MQTT remains an allowed MVP and edge transport, and its topics/QoS remain provider or transport-adapter concerns. It is no longer an architecture-level commitment that the OSIP bus must be MQTT. A future transport-selection ADR will choose one or more implementations only after the required semantics, failure modes, operating model, and compatibility evidence are documented.

No physical device is required to use the selected OSIP transport. Providers may communicate southbound through MQTT, WebSocket, REST, BACnet, KNX, vendor SDKs, or other suitable technology. The unification happens after a provider translates the interaction into a canonical OSIP event, command, or diagnostic record.

## Alternatives considered

| Alternative | Reason not selected |
| --- | --- |
| Retain MQTT as the permanent architectural bus | Prematurely treats an implementation choice as the semantic platform boundary. |
| Remove MQTT from the reference deployment | Discards an effective local technology and a major integration ecosystem without evidence. |
| Allow every component to choose its own ungoverned transport | Reintroduces point-to-point coupling, weakens observability, and makes durable contracts impossible. |

## Consequences

ADR-0004 is superseded, not rewritten. Existing MQTT guidance remains valid when MQTT is selected, but new specifications must use transport-neutral language above the transport adapter. Event/command contracts, correlation, idempotency, authorization, diagnostics, and retention are mandatory regardless of the selected implementation.

## Links

- [Message Bus](../docs/en/architecture/message-bus.md)
- [Event Model](../docs/en/architecture/event-model.md)
- [ADR-0004 MQTT Event Backbone](0004-mqtt-event-backbone.md)
