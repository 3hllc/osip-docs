# Physical Asset Model

## Purpose

OSIP operates physical reality, not an integration inventory. A Home Assistant entity, MQTT topic, BACnet object, KNX group address, or vendor identifier is evidence about an asset; it is never the primary identity of the thing being operated. This specification defines the durable spatial hierarchy, asset identity, relationships, capabilities, and commissioning rules that make applications portable across providers.

## Spatial hierarchy and graph

The containment hierarchy gives every record an operational scope. Not every deployment needs every level, but a child may not belong to two parents of the same containment type without an explicit exception.

```text
Site
└── Building
    └── Floor
        └── Space
            ├── Room
            ├── Corridor
            └── Zone
```

Zones are semantic or operational areas and may cross room boundaries. The containment tree is complemented by a typed relationship graph. Examples are `HVAC-17 serves Room-204`, `Door-12 connects Room-204 to Corridor-2`, `Sensor-81 measures-temperature-of Room-204`, and `Room-204 belongs-to Fire-Zone-F2`. A graph avoids encoding safety, access, service, adjacency, or observation relationships into a room name or dashboard tag.

## Asset identity

An asset receives a stable OSIP `asset_id` at commissioning, for example `asset:hotel-001:hvac-17`. Its record includes site scope, type, lifecycle, relationships, capabilities, provenance, and a history of verified bindings. Identity is not reissued when a provider is changed, a short radio address changes, or a device is replaced with a compatible verified successor.

External identifiers are bindings, not aliases for `asset_id`:

| Provider | External binding example | Meaning |
| --- | --- | --- |
| Home Assistant | `climate.room_204` | Entity exposed by one HA instance. |
| Zigbee2MQTT | `room204_sensor` | Integration-level device name. |
| BACnet | `128 / analog-input:7` | Device/object address. |
| Vendor API | Vendor resource UUID | Provider-specific remote identity. |

Every binding records provider, external identifier, supported capabilities, control role, first/last verification, health, and provenance. A provider can become unavailable without erasing the asset, its audit history, policies, or relationships.

## Capability contract

The domain works with documented capabilities rather than with protocols. Initial examples include `TemperatureMeasurement`, `OccupancyDetection`, `LightingControl`, `HVACControl`, `DoorControl`, `EnergyMeasurement`, and `BatteryHealth`. A capability contract names supported observations, commands, units, state freshness, quality semantics, error states, authorization class, and evidence of command completion.

A physical asset may expose many capabilities. Several assets may provide the same capability for a space. Provider-specific features remain available through a bounded diagnostics interface until they are intentionally promoted to a general capability contract. This prevents the general model from accidentally becoming a copy of Zigbee clusters, MQTT payloads, Home Assistant entities, or a vendor API.

## Multiple bindings and control roles

Multiple bindings are normal when a deployment needs different paths for control, observability, UI convenience, and failure recovery. The asset record assigns an explicit role, not an implicit preference:

| Role | Example | Rule |
| --- | --- | --- |
| Primary control | BACnet HVAC command | Selected by an approved execution plan. |
| Observability | Home Assistant telemetry | May inform context and UI but does not prove command completion by itself. |
| UI convenience | Home Assistant dashboard | Cannot bypass OSIP policy for controlled actions. |
| Critical fallback | Local direct provider | Used only under documented policy and health conditions. |

The choice of binding is made by policy-scoped execution planning. It is never inferred merely because a provider was discovered first or reports the freshest value.

## Commissioning and lifecycle

Discovery creates a candidate provider endpoint. Commissioning links it to an asset only after an installer verifies physical placement, capability mapping, safety class, and expected control/observation role. Activation makes the binding eligible for policy. Service, replacement, disablement, and retirement are auditable lifecycle changes. A replacement preserves an asset identity only after compatibility and physical installation have been verified; otherwise it receives a new asset identity and a documented relationship to the retired asset.

## Invariants

- Site and asset identifiers are stable OSIP identifiers, not transformed provider IDs.
- A raw provider payload cannot create or modify an authoritative physical relationship without a reviewed commissioning/configuration change.
- An asset can be represented by several bindings; no single binding is assumed to be the source of truth for every capability.
- Every command and observation is attributable to an asset, capability, provider binding, and site scope.
- A user-facing application may address a space, asset, capability, or intent but must not need to know the underlying provider identifier.

## Related documents

- [Domain Model](domain-model.md)
- [Digital Twin](digital-twin.md)
- [Integration Providers](integration-providers.md)
- [Intent, Policy, and Execution](intent-policy-and-execution.md)
