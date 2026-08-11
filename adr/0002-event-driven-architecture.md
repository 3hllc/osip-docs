---
title: ADR-0002 - Event-Driven Architecture
status: accepted
date: 2026-08-07
deciders: [OSIP Project]
tags: [architecture, integration, events]
---

# ADR-0002 - Event-Driven Architecture

## Context

OSIP must integrate heterogeneous devices, services, automation, AI, and future robotics without making each component aware of every other component. Direct point-to-point integrations become brittle as installations and products grow.

## Decision

OSIP uses documented events as the default asynchronous integration mechanism. Components publish domain facts and consume only the contracts they need. Commands remain explicit requests and are confirmed by acknowledgements or observed resulting state. Event contracts include ownership, version, correlation, privacy classification, and observability expectations.

## Alternatives considered

| Alternative | Reason not selected |
| --- | --- |
| Synchronous service calls as the default | Couples availability and release cadence; unsuitable for many device and edge workflows. |
| Vendor events used directly by all consumers | Exposes vendor semantics throughout the platform and makes replacement expensive. |
| Periodic polling only | Loses timeliness, increases network load, and obscures causal history. |

## Consequences

Consumers must be idempotent and tolerate duplicates, reordering, and delayed delivery. Schema governance and operational telemetry become required product work. In return, adapters and new consumers can evolve with less coupling.

## Links

- [Event Model](../docs/architecture/event-model.md)
- [ADR-0004 MQTT Event Backbone](0004-mqtt-event-backbone.md)
