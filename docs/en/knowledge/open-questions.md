# Open Questions

## Purpose and operating rule

This register contains unresolved questions that can materially affect OSIP architecture, reference-apartment delivery, safety, cost, or productization. It is deliberately not a list of general ideas. Each entry has a decision or evidence path; when resolved, it is moved to the decision log, an ADR, a specification, or the risk register as appropriate.

Question identifiers are stable. Status values are **Open**, **Investigating**, **Blocked**, or **Resolved**. “Resolved” requires a linked artefact, not merely a conversation outcome.

## Active register

| ID | Question | Why it matters | Next evidence or decision | Status |
| --- | --- | --- | --- | --- |
| OQ-001 | Which device categories and quantities are required in the 165 m² reference apartment to prove the initial spatial model and installer workflow? | Scope drives BOM, radio coverage, commissioning time, and acceptance criteria. | Create the room-by-room capability matrix and approve the minimum viable reference design. | Open |
| OQ-002 | What normalization contract is required between Zigbee2MQTT and OSIP for supported capabilities? | Raw vendor topics would couple automation, AI, and operations to one adapter. | Define supported capabilities, identity mapping, event schemas, command completion evidence, and error semantics. | Investigating |
| OQ-003 | Which functions remain fully local when the WAN, cloud account, or remote AI provider is unavailable? | The answer is the testable boundary of Local First rather than a slogan. | Write an outage matrix covering control, access, telemetry, backups, AI, and remote administration. | Open |
| OQ-004 | What local data retention periods and consent model apply to event history, audio, images, occupancy, and behavioural inferences? | Privacy and storage choices constrain data architecture before collection begins. | Produce a data classification and retention proposal; review it before enabling sensitive sources. | Open |
| OQ-005 | Which safety-relevant actuators are in scope for the first deployment, and what manual overrides and fail-safe states do they require? | Water, access, power, HVAC, and robotics require controls beyond ordinary automation. | Produce a hazard review and per-actuator command/override specification. | Open |
| OQ-006 | What installer evidence is necessary to accept a radio mesh, device commissioning, backup, and recovery as complete? | A repeatable Installer Edition needs observable handover criteria, not a technician’s implicit judgement. | Draft the commissioning checklist and test it on the reference apartment. | Open |
| OQ-007 | Which Home Assistant responsibilities are platform-facing integration functions, and which remain optional user-interface or automation conveniences? | Prevents a useful implementation from becoming an undocumented OSIP dependency. | Resolved by ADR-0008; validate the specific MVP provider contract in the reference deployment. | Resolved |
| OQ-008 | Which canonical event/command semantics are required before choosing a long-term OSIP bus transport? | Delivery, ordering, idempotency, replay, durability, request/response, and operational burden determine whether MQTT remains sufficient or another transport is justified. | Produce a semantic and failure-mode matrix, then create the transport-selection ADR. | Open |
| OQ-009 | What is the minimum HomeAssistantProvider contract for the MVP? | The provider must prove capability mapping, raw-telemetry provenance, health, command outcome, and asset-binding lifecycle without making HA mandatory. | Define one supported capability set and contract-test fixtures from the reference deployment. | Open |
| OQ-010 | Which first edge-required workflow and intent demonstrate the OSIP boundary? | A narrow end-to-end proof must show asset identity, canonical events, local policy, deterministic execution, observed completion, and outage recovery. | Select the workflow, define its continuity contract and acceptance evidence, and execute a WAN/HA-independence test. | Open |
| OQ-011 | Which private local LLM/runtime profile meets the first installer and natural-language interaction jobs on available reference-deployment hardware? | OSIP needs a private, operationally supportable option without binding architecture to a model or silently falling back to cloud. | Define hardware envelope and evaluation corpus; compare licensed candidates for typed-output reliability, latency, privacy, operating burden, and fallback behaviour. | Open |

## Lifecycle

An entry is added when postponing its answer is intentional and the consequence is known. The contributor must identify the owner role, expected resolution artefact, and target review milestone before a question is accepted. During each architecture or reference-design review, entries are either advanced, converted into risks, or closed with a link.

## Related records

- [Assumptions](assumptions.md)
- [Constraints](constraints.md)
- [Risks](risks.md)
- [Decision Log](decision-log.md)
- [ADR Process](../standards/adr-process.md)
