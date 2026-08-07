# Research Summary

## Purpose

This page indexes research themes that affect OSIP. It distinguishes accepted architectural direction from implementation evidence. Individual research records in the repository-level `research/` directory must state source, method, date, findings, limits, and the resulting decision or open question.

## Current research themes

| Theme | Question | Current position | Required evidence |
| --- | --- | --- | --- |
| Device networking | Which protocols meet local control, reliability, ecosystem, and installer needs? | Zigbee is an initial low-power device-network option; Matter and other protocols remain candidates. | Supported-device matrix, RF/commissioning tests, lifecycle and interoperability assessment. |
| Event transport | How should integrations exchange normalized events and commands? | MQTT is the initial local backbone behind OSIP contracts. | Topic/contract standard, authorization, duplicate/timeout handling, broker recovery test. |
| Automation integration | What role should Home Assistant perform? | Initial integration and automation platform, not the OSIP core. | Boundary map, ownership of state/policy, replacement feasibility test. |
| Edge runtime | What compute and container architecture is sufficient for local availability? | Containerized local services are preferred; hardware remains a sizing decision. | Resource profile, power-loss behaviour, backup/restore, upgrade and thermal tests. |
| Data and telemetry | Which stores support state, event history, operational metrics, and privacy retention? | Separate concerns are expected; a product choice is not yet accepted. | Data classification, retention policy, query/load tests, recovery and cost analysis. |
| Spatial sensing and AI | Which sources add useful context without disproportionate privacy cost? | Start with explicit, consented capability use cases and deterministic fallback. | Accuracy, latency, false-action, consent, retention, and local/cloud boundary evaluation. |
| Building systems | How can HVAC, water, power, lighting, access, and shading become repeatable integrations? | Model capabilities rather than vendor products. | Interface survey, fail-safe analysis, commissioning evidence, installer time estimate. |

## Evidence policy

Research must not convert a popular product into a platform dependency. A finding is accepted when it names the use case, constraints, tested version or environment, evidence quality, alternatives, and resulting recommendation. A result that applies only to the reference apartment is labelled accordingly.

## Immediate research outputs

1. Build the initial Technology Radar from the candidate stack.
2. Produce the Reference Apartment capability and engineering survey.
3. Define the MQTT/device-identity integration contract.
4. Evaluate local compute, storage, backup, and observability for outage recovery.
5. Establish the supported-device and BIM/BOM evidence model for Installer Edition.

## Related documents

- [Technology Radar](technology-radar.md)
- [Reference Apartment](../reference-designs/reference-apartment.md)
- [Open Questions](open-questions.md)
- [Risks](risks.md)
