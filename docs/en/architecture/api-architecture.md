# API Architecture

## Interface types

OSIP uses different contracts for different interaction needs: events for asynchronous facts, commands for specific capability actions, intents for desired operational outcomes, queries for current or historical projections, configuration interfaces for reviewed durable changes, and human/installer interfaces for controlled operations. An intent is resolved into a policy-compliant execution plan; it is not an unbounded command or permission bypass. A UI is a client of these boundaries, not a privileged alternate API.

## Contract ownership and versioning

Every exposed interface has an owner, audience, authentication method, authorization scope, data classification, compatibility policy, and test fixture. External HTTP interfaces use versioned OpenAPI contracts when selected; event contracts follow the Event Model. Breaking changes use a new major contract and announced migration path. Undocumented endpoints, direct database access, and generic broker credentials are not supported integration APIs.

## Authorization

Authentication establishes a person, service, device, or installer-tool identity. Authorization evaluates the requested action against its role, installation scope, resource, safety policy, and optional resident approval. Administrative configuration, device commands, and read-only monitoring are separate grants. Service-to-service requests use purpose-limited identities, not an inherited human administrator token.

## Compatibility and observability

API responses and events expose correlation identifiers and meaningful errors without leaking secrets. Deprecation is announced in the contract and measured before removal. Contract tests cover authorization, validation, idempotency, error behaviour, and backwards compatibility; operational telemetry reports version use and failed requests.
