# Event Model

## Purpose

Events are immutable statements that something was observed, changed, requested, rejected, or completed. They distribute facts across bounded components without requiring a consumer to call a producer directly. An event is not a database dump, an undocumented vendor topic, or a command disguised as a state change.

## Contract

Each event envelope must carry a stable event name and version, unique event identifier, occurrence timestamp, producer identity, correlation identifier when it belongs to a workflow, subject identity, site scope, schema reference, provenance reference, and data classification. Payloads contain the minimum data required by consumers; sensitive information is not placed in a broad topic merely for convenience.

Suggested names use the form `osip.<domain>.<fact>.v<major>`, for example `osip.device.state-changed.v1` or `osip.space.occupancy-inferred.v1`. The topic or routing key is transport configuration; the event name is the domain contract.

## Semantics

- Delivery is at-least-once unless a chosen transport and consumer explicitly establish a stronger guarantee.
- Consumers must be idempotent using `event_id`, subject version, or an equivalent deduplication strategy.
- Ordering is only assumed within an explicitly defined subject or partition. Consumers tolerate late or duplicated events.
- Commands are separately named requests with a correlation ID; a resulting observation or completion event confirms the outcome.
- Schema evolution is additive within a major version. Breaking changes receive a new major event name and a migration period.

## Lifecycle and observability

Events have owners, retention expectations, access policies, and redaction requirements. The system records publish and processing failures, lag, retry counts, dead-letter handling, and correlation links so an operator can trace an automation from input to effect.

## Boundaries

Raw protocol events are provider inputs. A provider normalises them into OSIP contracts only after validating asset binding, timestamp, units, and capability semantics. Raw payloads remain available through a bounded diagnostics/reprocessing interface with provenance and access controls; they never become a general core-domain API.
