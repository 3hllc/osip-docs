# Risks

## Purpose

The risk register makes uncertainty visible before it becomes an outage, costly rework, unsafe behaviour, or an unrepeatable installation. It tracks project and operational risks, not individual bugs. A risk is closed only when its exposure is retired, transferred, accepted by an appropriate owner, or reduced to an explicitly accepted residual level.

Likelihood and impact use **Low**, **Medium**, or **High**. Risk owners are roles until named project owners are assigned.

## Active register

| ID | Risk | Likelihood | Impact | Mitigation and trigger | Owner role |
| --- | --- | --- | --- | --- | --- |
| R-001 | Zigbee radio coverage or routing proves unreliable in portions of the reference apartment. | Medium | High | Design powered-router placement, perform a site survey and router-loss tests. Trigger: recurring unavailable devices, command latency beyond acceptance criteria, or route instability. | Reference-design lead |
| R-002 | Vendor-specific integration payloads leak into general automation or AI logic. | Medium | High | Enforce adapter contracts and review topic/schema usage. Trigger: a core consumer subscribes to raw adapter topics or uses vendor identity as domain identity. | Architecture lead |
| R-003 | A cloud dependency is introduced into a function declared local-first. | Medium | High | Maintain an outage matrix and run WAN-loss acceptance tests. Trigger: loss of WAN blocks local command, identity, or required state. | Platform lead |
| R-004 | Credentials, Zigbee network material, backups, or personal data enter Git or shared logs. | Low | High | Secret scanning, redacted examples, controlled secret storage, and access review. Trigger: secret-like material in a change, issue, or generated artefact. | Security lead |
| R-005 | The reference apartment becomes a bespoke installation with no reusable commissioning evidence. | Medium | High | Require design records, capability matrix, test evidence, and installer-oriented checklists. Trigger: a feature works only through undocumented manual intervention. | Product and installer lead |
| R-006 | AI features infer or retain sensitive behavioural information without clear consent and retention controls. | Medium | High | Classify data before collection; keep AI optional; introduce consent, retention, and audit requirements. Trigger: proposal to collect audio, images, location, or behavioural history without an approved policy. | Privacy lead |
| R-007 | Documentation language branches drift, giving users different architecture meaning by language. | Medium | Medium | Keep EN canonical, maintain structural parity, and label untranslated pages explicitly. Trigger: an RU page claims a decision not present in EN. | Documentation lead |
| R-008 | A provider selection or fallback path is treated as safe without evidence of its authority, physical completion, and degraded behaviour. | Medium | High | Require binding roles, execution-plan verification, outage tests, and policy-gated fallback selection. Trigger: provider acknowledgement is treated as actuator completion or a fallback activates without an approved policy. | Architecture and safety lead |

## Review and escalation

Risks are reviewed at architecture, reference-design, and release milestones, and immediately after a trigger. A high-impact risk without a mitigation owner blocks the affected production-like deployment. Incident-specific follow-up belongs in the incident record but must update this register when it reveals a systemic exposure.

## Related records

- [Open Questions](open-questions.md)
- [Assumptions](assumptions.md)
- [Constraints](constraints.md)
- [Security Architecture](../architecture/security-architecture.md)
