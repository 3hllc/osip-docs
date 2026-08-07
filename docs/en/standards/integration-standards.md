# Integration Standards

## Purpose

These standards keep OSIP integrations vendor-agnostic and evolvable. They apply to HTTP APIs, MQTT, device adapters, gateways, and future transports. A transport topic or vendor payload never becomes an undocumented public contract.

## Contract rules

Every published OSIP command, event, state projection, or query contract declares an owner, semantic version, identifier, source, occurrence time, correlation/causation information, privacy classification, schema, and failure semantics. Backward-compatible changes are additive; breaking changes create a new version and migration plan. Consumers must tolerate unknown additive fields and duplicate delivery.

## MQTT boundary

MQTT topics are transport routing, not business meaning. The initial convention is `osip/<environment>/<classification>/<domain>/<subject>`, where classification is `event`, `command`, `state`, `diagnostic`, or `integration`. QoS, retention, expiry, and last-will behaviour are chosen per contract. Retained messages require source health and timestamp; they are never proof that a physical device is currently reachable.

Adapter-originated raw topics stay in an integration namespace. An ingress adapter validates credentials and payloads, maps identities, normalizes supported capabilities, and publishes OSIP contracts with separate credentials. Core consumers must not command devices through raw adapter topics.

## Identity

OSIP assigns stable domain IDs such as `device_id`, `space_id`, and `integration_id`. Vendor serial numbers, IEEE/EUI-64 addresses, short radio addresses, friendly names, endpoints, and cloud identifiers are integration attributes with source and lifecycle timestamps. Replacement, merge, or retirement is an explicit lifecycle operation; identifier reuse is prohibited.

## APIs and compatibility

Synchronous APIs expose explicit resource, command, and query boundaries. They authenticate every caller, authorize by least privilege, validate input, return typed errors, and emit auditable correlation IDs. API descriptions are versioned source artefacts; event contracts use the same vocabulary and identity rules. New adapters demonstrate contract conformance through fixtures and integration tests before they are supported.

## Naming and releases

Names are lowercase, stable, and domain-led. Avoid vendor names in general contracts. Documents, schemas, diagrams, and executable configuration are versioned together when one change alters observable behaviour. A release notes contract changes, migration, compatible adapter versions, operational impact, and rollback boundary.

## Related documents

- [Event Model](../architecture/event-model.md)
- [Message Bus](../architecture/message-bus.md)
- [Device Model](../architecture/device-model.md)
- [Zigbee Mesh and MQTT Bridge](../architecture/zigbee-mesh-and-mqtt-bridge.md)
