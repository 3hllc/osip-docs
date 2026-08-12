# Device Model

## Purpose

The asset model represents what a physical or virtual asset can do without making a vendor protocol the platform API. It joins stable physical identity, capability, state, location, health, and provider provenance. A field device is one kind of asset; HVAC equipment, doors, lighting circuits, cameras, and logical engineering assets may also be assets.

## Core concepts

| Concept | Meaning |
| --- | --- |
| Asset | A physical or virtual entity with a stable OSIP identity and lifecycle. |
| Device | A field endpoint or controller represented as an asset; its protocol identity is a binding, not the asset identity. |
| Capability | A documented behaviour such as dimming, temperature sensing, lock actuation, or leak detection. |
| State | An observed or projected value with timestamp, quality, and source. |
| Command | A typed requested state transition, never an assumption of successful change. |
| Provider | The bounded translator between external entities and OSIP capability contracts. |
| Binding | An explicit mapping between an asset and an external provider identity, with role and health. |
| Health | Connectivity, battery, diagnostics, last-seen, firmware, and adapter quality information. |

A provider maps vendor IDs and units to OSIP identities and capability contracts, preserving raw diagnostics at the boundary. It validates incoming values, reports health, and makes limitations explicit. An asset may expose multiple capabilities, have more than one binding, and be related to spaces or other assets through the digital twin. A binding declares whether it is primary control, observability, UI convenience, or critical fallback; selection is explicit and policy-scoped.

## Lifecycle

Discovery creates a candidate binding, commissioning verifies the asset identity, placement, capabilities, and control role, activation permits use by policy, service records replacement or maintenance, and retirement revokes access while retaining appropriate historical evidence. Replacement may preserve the logical asset/capability/space binding where the installer verifies compatibility; an intent must never require a specific serial number or provider identifier.
