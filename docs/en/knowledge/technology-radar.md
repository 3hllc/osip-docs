# Technology Radar

## Purpose

The radar records technologies discussed for OSIP without mistaking them for irreversible platform decisions. Ring placement expresses adoption intent, not product endorsement. Every entry still needs version, licence, support, security, operational, and replacement analysis before production use.

## Rings

| Ring | Meaning |
| --- | --- |
| **Adopt** | An accepted architectural baseline, subject to its ADR and operational constraints. |
| **Trial** | A candidate to validate in the reference apartment. |
| **Assess** | Worth researching; no integration commitment exists. |
| **Hold** | Do not introduce until a stated concern is resolved. |

## Initial radar

| Technology area | Ring | OSIP position |
| --- | --- | --- |
| MQTT | Adopt | Initial local event backbone; contracts stay transport-independent. |
| Home Assistant | Adopt | Initial integration platform; never the OSIP domain core. |
| Zigbee with a replaceable adapter | Trial | Validate RF design, supported-device lifecycle, commissioning, and mesh recovery in the reference apartment. |
| Zigbee2MQTT | Trial | Strong initial adapter candidate; raw topic model remains outside OSIP contracts. |
| Docker / Docker Compose | Trial | Candidate local packaging approach; assess upgrade, backup, secret, and operator workflows. |
| Grafana | Trial | Candidate observability presentation layer; assess local operation and access controls. |
| Matter / Thread | Assess | Assess by capability, maturity, commissioning UX, and local-control evidence rather than market claims. |
| ESPHome and custom MCU firmware | Assess | Assess only where a defined capability cannot be met with supported products. |
| Intel N100-class edge host | Assess | Candidate for local services; validate compute, storage, thermals, power, and serviceability. |
| Raspberry Pi-class node | Assess | Candidate for constrained edge roles, not an assumed universal runtime. |
| InfluxDB and PostgreSQL | Assess | Evaluate separately for telemetry/history and durable relational configuration/state needs. |
| Direct cloud-only device APIs | Hold | Incompatible with Local First unless a documented local degraded path exists. |

## Review cadence

Review the radar at each reference-design milestone and before an Installer Edition release. A change from Trial or Assess to Adopt requires evidence and, when architectural, an ADR. A technology can be removed without changing the platform if its adapter and contract boundary were respected.

## Related documents

- [Research Summary](research-summary.md)
- [Open Questions](open-questions.md)
- [Architecture Overview](../architecture/architecture-overview.md)
