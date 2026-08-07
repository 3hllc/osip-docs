# Device Model

## Purpose

The device model represents what a physical or virtual asset can do without making a vendor protocol the platform API. It joins installation identity, capability, state, location, health, and adapter provenance.

## Core concepts

| Concept | Meaning |
| --- | --- |
| Device | A physical or virtual asset with a stable OSIP identity and lifecycle. |
| Capability | A documented behaviour such as dimming, temperature sensing, lock actuation, or leak detection. |
| State | An observed or projected value with timestamp, quality, and source. |
| Command | A typed requested state transition, never an assumption of successful change. |
| Adapter | The bounded translator between a vendor/protocol entity and OSIP capability contracts. |
| Health | Connectivity, battery, diagnostics, last-seen, firmware, and adapter quality information. |

An adapter maps vendor IDs and units to OSIP identities and capability contracts, preserving raw diagnostics at the boundary. It validates incoming values, reports health, and makes limitations explicit. A device may expose multiple capabilities and be linked to one or more spaces or objects through the digital twin.

## Lifecycle

Discovery creates a candidate, commissioning verifies identity and placement, activation permits use by policy, service records replacement or maintenance, and retirement revokes access while retaining appropriate historical evidence. Replacement should preserve the logical capability/space binding where the installer verifies compatibility; an automation must not require a specific serial number to express its intent.
