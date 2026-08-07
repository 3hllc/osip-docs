---
title: ADR-0006 — Spatial Model as a Core Domain Capability
status: accepted
date: 2026-08-07
deciders: [OSIP Project]
tags: [spatial, digital-twin, domain]
---

# ADR-0006 — Spatial Model as a Core Domain Capability

## Context

Device-centric automation cannot express that an activity occurred in a zone, a room is occupied, a robot can navigate to an object, or a user request refers to “the reading area.” These meanings require a durable representation of space and relationships.

## Decision

OSIP treats spaces, zones, objects, physical relationships, device locations, and semantic labels as core domain concepts. The digital twin has explicit ownership and provenance; inferred context is separate from immutable physical facts and includes freshness and confidence.

## Alternatives considered

| Alternative | Reason not selected |
| --- | --- |
| Keep room names only in automation configuration | Cannot support reusable reasoning, spatial queries, or cross-system consistency. |
| Use a particular CAD/BIM tool as the domain model | Couples the platform to a design tool and does not represent live contextual state. |
| Add spatial semantics later | Makes current identifiers and integrations difficult to migrate when spatial use cases arrive. |

## Consequences

The reference apartment must establish a coordinate, zone, identity, and change-management convention. This investment enables future contextual AI and robotics without making either mandatory for baseline operation.
