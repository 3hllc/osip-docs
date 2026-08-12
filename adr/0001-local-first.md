---
title: ADR-0001 - Local First Operation
status: accepted
date: 2026-08-07
deciders: [OSIP Project]
tags: [architecture, reliability, privacy]
---

# ADR-0001 - Local First Operation

## Context

Control in physical environments affects comfort, access, water protection, safety, and business operations. The reference apartment is the first validation deployment, but the same reliability principle applies to every supported space type. WAN and cloud outages are expected operational conditions, not exceptional events. A cloud-dependent control plane also increases latency, privacy exposure, and provider lock-in.

## Decision

OSIP operates local control, local automation, local event transport, supported-device connectivity, and the minimum contextual state required for critical behaviour inside the installation. Cloud connectivity is optional enhancement. Every product capability declares whether it is local-required, local-preferred, cloud-enhanced, or cloud-only; cloud-only functions cannot be prerequisites for core control in a supported deployment.

## Alternatives considered

| Alternative | Reason not selected |
| --- | --- |
| Cloud-first central platform | Makes a remote outage a local-control outage and weakens privacy and lifecycle control. |
| Local cache in a cloud-first design | A cache does not provide independent local identity, policy, orchestration, and recovery. |
| Fully isolated local system | Prevents useful optional remote service, analytics, backup, and high-capacity inference. |

## Consequences

Local deployments need compute, storage, update, backup, observability, and recovery design. Cloud features must degrade clearly and safely. This adds installation discipline, but produces a more reliable and commercially credible system.

## Links

- [Project Charter](../docs/en/foundation/project-charter.md)
- [Architecture Overview](../docs/en/architecture/architecture-overview.md)
