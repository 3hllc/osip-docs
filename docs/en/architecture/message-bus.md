# Message Bus

## Decision boundary

The message bus provides durable, observable transport for events and routed commands. MQTT is the preferred initial backbone because it works well on constrained local networks and has a mature device ecosystem. MQTT is not the platform: contracts, authorization, adapters, and observability must make later transport evolution possible.

## Responsibilities

The bus supports publish/subscribe delivery, retained state only where a documented state projection requires it, last-will or equivalent connectivity signals, authenticated client identities, topic-level authorization, and local operation. It does not decide automation policy, store the entire digital twin, or grant a client permission to bypass domain controls.

## Topic convention

Topics are transport-facing and segregate environment and traffic class. A starting convention is `osip/<environment>/<classification>/<domain>/<subject>`. Classification distinguishes event, command, state, diagnostic, and integration traffic. The event envelope carries the semantic contract and version; a topic name alone is never a sufficient API.

Separate clients and credentials are required for adapters, core services, administrative tooling, and installer tooling. Wildcard subscriptions and publication rights are granted only when necessary and are reviewed as part of a deployment.

## Resilience and migration

The broker runs on the local trusted environment and is monitored for availability, connection churn, rejected authorization, queued messages, and retained-state size. Clients reconnect safely, treat duplicates as normal, and do not assume retained data is current without its timestamp and source health.

Bus-facing interfaces are specified independent of MQTT client libraries. An adapter layer is responsible for translating OSIP event and command contracts into MQTT topics and QoS choices. This preserves the option to introduce bridges or replace transport without changing the core domain.
