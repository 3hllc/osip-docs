---
title: ADR-0005 — Vendor-Agnostic Replaceable Components
status: accepted
date: 2026-08-07
deciders: [OSIP Project]
tags: [vendor-independence, architecture]
---

# ADR-0005 — Vendor-Agnostic Replaceable Components

## Context

Device vendors, cloud providers, brokers, AI models, and open-source projects evolve on different schedules. Their capabilities are valuable, but platform lock-in would make OSIP costly to operate, migrate, and commercialize.

## Decision

OSIP owns stable domain contracts and integrates external systems through adapters. Every external dependency has an explicit boundary, ownership, health expectation, credential model, and replacement/migration consideration. Prefer open and documented protocols; isolate necessary proprietary protocols at the edge.

## Alternatives considered

| Alternative | Reason not selected |
| --- | --- |
| Select one strategic vendor as the core | Simplifies the first installation but creates commercial and technical dependency. |
| Support every vendor natively in the core | Spreads vendor details across the system and is not maintainable. |
| Refuse proprietary products | Is unnecessarily restrictive where an adapter can contain the risk. |

## Consequences

Adapters introduce initial design work and a supported-compatibility matrix. They protect the core model and create a clearer product surface for partners and installers.
