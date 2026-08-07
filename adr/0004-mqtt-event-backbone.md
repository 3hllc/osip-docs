---
title: ADR-0004 — MQTT as the Initial Event Backbone
status: accepted
date: 2026-08-07
deciders: [OSIP Project]
tags: [mqtt, events, edge]
---

# ADR-0004 — MQTT as the Initial Event Backbone

## Context

The reference apartment requires a local, lightweight, widely supported event transport that works with constrained devices and common integration products. OSIP needs a useful starting point without embedding transport semantics in its core model.

## Decision

Use MQTT as the initial local message backbone. OSIP defines event and command contracts above MQTT topics, enforces authenticated client identities and least-privilege topic access, and isolates MQTT-client concerns in adapters. MQTT retained messages, QoS, and topic design are selected per documented contract.

## Alternatives considered

| Alternative | Reason not selected |
| --- | --- |
| Direct HTTP/webhook integrations | Less suitable as a common local device backbone and encourages point-to-point coupling. |
| Kafka or equivalent streaming platform | Operationally disproportionate for the initial local residential deployment. |
| No common backbone | Makes cross-vendor automation and observability harder to standardize. |

## Consequences

MQTT operational security, broker monitoring, reconnect behaviour, and duplicate handling are required. Transport replacement remains possible only if domain contracts do not leak MQTT details.

## Links

- [Message Bus](../docs/architecture/message-bus.md)
- [Event Model](../docs/architecture/event-model.md)
