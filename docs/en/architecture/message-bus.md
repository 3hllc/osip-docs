# Message Bus

## Decision boundary

The OSIP bus provides durable, observable transport for canonical events and routed commands. It is a semantic boundary, not a commitment that every device or provider uses one transport. MQTT is a valid initial local transport and an important integration technology, but the selected bus implementation must follow the required delivery, ordering, replay, durability, request/response, and operational semantics. Domain contracts do not expose MQTT topics or client libraries.

## Responsibilities

The bus supports publish/subscribe delivery, retained state only where a documented state projection requires it, last-will or equivalent connectivity signals, authenticated client identities, topic-level authorization, and local operation. It does not decide automation policy, store the entire digital twin, or grant a client permission to bypass domain controls.

## Topic convention

Topics are transport-facing and segregate environment and traffic class. A starting convention is `osip/<environment>/<classification>/<domain>/<subject>`. Classification distinguishes event, command, state, diagnostic, and integration traffic. The event envelope carries the semantic contract and version; a topic name alone is never a sufficient API.

Separate clients and credentials are required for adapters, core services, administrative tooling, and installer tooling. Wildcard subscriptions and publication rights are granted only when necessary and are reviewed as part of a deployment.

## Resilience and migration

The selected local transport runs in the trusted environment and is monitored for availability, connection churn, rejected authorization, queues, lag, and persisted-state size as applicable. Clients reconnect safely, treat duplicates as normal, and do not assume a cached or retained value is current without its timestamp and provider health.

Bus-facing interfaces are specified independently of transport libraries. A transport adapter translates OSIP event and command contracts into MQTT topics and QoS choices, NATS subjects, or another selected mechanism. This preserves the option to introduce bridges or replace transport without changing the core domain.
