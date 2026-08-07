# OSIP Project Principles

## How to use these principles

Principles are decision filters, not marketing language. A proposal that conflicts with one may still be accepted, but the ADR must state the conflict, why it is justified, which compensating controls are required, and how the exception will be revisited.

## Local First and Cloud Enhanced

Local control is the normal execution path for lighting, environmental control, access, leak response, automation, device discovery, and the local message bus. Local does not merely mean that a cache exists: the required identities, state, control logic, and interfaces must work without a WAN connection.

Cloud services are valuable for remote access, opt-in backup, fleet-wide insights, heavy AI inference, and synchronisation. They are additive. A cloud outage must degrade optional experiences clearly and safely rather than silently changing local behaviour.

## Event driven, explicit boundaries

Events communicate observations, state changes, and completed commands. Consumers must not infer hidden meaning from a vendor topic or directly mutate another component's internal state. Commands, events, queries, and configuration are distinct interaction types and are documented separately.

The event backbone makes loose coupling possible but does not remove the need for contracts. Each event has an owner, schema version, correlation information, privacy classification, and observable delivery path.

## Spatial and human context before device control

The durable model represents spaces, zones, objects, occupants, devices, capabilities, and relationships. A device adapter can report that a motion sensor changed state; the platform derives the contextual fact that activity occurred in a named zone. Automation and AI work against contextual intent wherever possible, not against opaque vendor identifiers.

## Replaceable components and open standards

OSIP keeps its domain model, event contracts, access model, and operational expectations independent of providers. MQTT, Home Assistant, Zigbee2MQTT, databases, cloud vendors, LLMs, and user interfaces may all be useful implementations. Each is integrated through an adapter or contract so it can be changed without redefining what a room, device, task, or event means.

## Security, privacy, and safety

Security is not deferred until deployment. Devices and services receive distinct identities; credentials are not committed to Git; networks are segmented by trust and function; privileged actions are audited. Data collection is purposeful and minimized. Camera, microphone, location, and behavioural data require documented retention, access, and consent boundaries.

Automations affecting water, access, electricity, HVAC limits, or robots are treated as safety-relevant. They require clear manual override and conservative failure behaviour.

## Documentation and operational excellence

Markdown and text-based diagrams are reviewable source artifacts. MkDocs is a presentation layer, not a second place to edit facts. Every significant component has an owner, health signals, logs or traces, backup and recovery expectations, and a path for an installer or operator to diagnose it.

## Commercial durability

The reference apartment is allowed to explore, but the lessons must result in repeatable installation patterns. Decisions are evaluated for installation time, serviceability, lifecycle cost, support burden, partner enablement, and customer clarity in addition to technical elegance.

