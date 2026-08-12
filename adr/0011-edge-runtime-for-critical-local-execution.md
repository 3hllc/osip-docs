---
title: ADR-0011 - Edge Runtime for Critical Local Execution
status: accepted
date: 2026-08-12
deciders: [OSIP Project]
tags: [edge, local-first, safety, resilience]
---

# ADR-0011 - Edge Runtime for Critical Local Execution

## Context

Local First requires more than a locally installed dashboard, broker, or cache. A site must retain enough approved configuration, identity, policy, state, deterministic execution logic, and provider path to perform declared critical functions during WAN loss or control-plane unavailability. Home Assistant and cloud services may be useful, but neither can be a required link in a safety- or business-critical OSIP loop.

## Decision

OSIP defines a site-local Edge runtime. The edge consumes canonical events, holds the local subset of asset bindings, policy, desired state, and authorization scope required for declared functions, hosts the locally required Constrained Spatial Reasoning Layer, and runs deterministic execution/command-verification paths. The fleet/control plane distributes reviewed configuration and collects evidence but is not synchronously required for edge-required behaviour. Home Assistant may be an optional provider or UI component, never the mandatory critical path.

## Alternatives considered

| Alternative | Reason not selected |
| --- | --- |
| Cloud-first control with local caching | Cannot provide a dependable local policy and command path when the central service is unreachable. |
| Make Home Assistant the universal local executor | Creates a mandatory third-party dependency and prevents direct provider paths for critical needs. |
| Implement full fleet functionality before edge validation | Delays the primary reliability hypothesis and creates unneeded early complexity. |

## Consequences

Each edge-required capability must have an outage-testable local continuity contract, conservative failure state, manual override, recovery objective, and observed-completion evidence. The Reference Apartment must demonstrate at least one such workflow. Edge configuration distribution, version reconciliation, local audit buffering, and provider degradation handling become required architecture work.

## Links

- [Edge Runtime](../docs/en/architecture/edge-runtime.md)
- [Deployment Architecture](../docs/en/architecture/deployment-architecture.md)
- [ADR-0001 Local First](0001-local-first.md)
