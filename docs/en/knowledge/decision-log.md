# Decision Log

## Purpose

The decision log is the index of decisions that shape OSIP. It gives readers a quick answer to “what did we decide, why, and where is the authoritative record?” Significant, cross-cutting, or difficult-to-reverse decisions require an ADR. Smaller implementation, sequencing, or documentation decisions are recorded here until they are superseded or no longer relevant.

Status values are **Accepted**, **Provisional**, **Superseded**, and **Proposed**. A decision is not accepted merely because it appears in an issue, chat, or code change.

## Architecture and documentation decisions

| ID | Decision | Status | Authoritative record |
| --- | --- | --- | --- |
| D-001 | OSIP means Open Spatial Intelligence Platform. | Accepted | [Project Charter](../foundation/project-charter.md) |
| D-002 | Required control operates locally; cloud services enhance rather than replace the normal local path. | Accepted | ADR-0001 - Local First |
| D-003 | Use event-driven interaction with explicit contracts between components. | Accepted | ADR-0002 - Event-Driven Architecture |
| D-004 | Treat Home Assistant as an initial integration platform, not as the OSIP domain core. | Accepted | ADR-0003 - Home Assistant Integration Platform |
| D-005 | Use MQTT as the initial local event backbone, behind adapter and contract boundaries. | Accepted | ADR-0004 - MQTT Event Backbone |
| D-006 | Maintain a vendor-agnostic domain model and isolate vendor implementations in adapters. | Accepted | ADR-0005 - Vendor-Agnostic Components |
| D-007 | Use a spatial model and digital twin as durable, contextual platform concepts. | Accepted | ADR-0006 - Spatial Model |
| D-008 | Keep AI native to the architecture but optional, bounded, and unable to replace safety-critical deterministic control. | Accepted | ADR-0007 - AI Native, Optional |
| D-009 | Keep English as the canonical technical source while publishing a structurally equivalent Russian site with incremental translations. | Provisional | ADR-0000 - Documentation Strategy and current MkDocs configuration |
| D-010 | Model Zigbee Mesh as a physical-device integration layer and MQTT as a separate local event transport. | Accepted | [Zigbee Mesh and MQTT Bridge](../architecture/zigbee-mesh-and-mqtt-bridge.md) |

## Recording rules

New entries include a stable ID, status, concise statement, decision date in the underlying record, and one authoritative link. A decision log entry never replaces the reasoning in an ADR. When a decision is superseded, retain its entry, mark the status, and link the successor; do not rewrite history.

## Related records

- [Open Questions](open-questions.md)
- [Documentation Standards](../standards/documentation-standards.md)
