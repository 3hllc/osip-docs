# Monitoring and Observability

## Purpose

Observability makes an OSIP installation supportable without guesswork. Every service, adapter, and critical device capability exposes ownership, health, logs or audit trail, and a diagnosis path. Observability is designed with the integration rather than added after an incident.

## Signals

| Signal class | Minimum question answered |
| --- | --- |
| Availability | Is the service, broker, adapter, device, or source currently reachable? |
| Freshness | When was the latest trusted observation and is it stale for this capability? |
| Correctness | Are schema validation, authorization, command completion, and policy decisions succeeding? |
| Capacity | Are resource, queue, storage, battery, and retry conditions approaching a limit? |
| Audit | Who or what proposed, approved, executed, and observed a consequential action? |

## Rules

Health is not inferred solely from an open TCP port or retained MQTT state. Dashboards and alerts distinguish local infrastructure failures, integration failures, device availability, stale sensing, and cloud degradation. Logs exclude secrets and minimize personal information; access and retention follow data classification. Alerts have an owner, severity, operator action, and suppression/maintenance rule.

## Testability

Every supported integration has fixtures or replayable samples, contract tests, and observable failure scenarios. Tests cover duplicate events, malformed payloads, unavailable devices, authorization denial, timeout, reconnect, and degraded local operation where relevant. Incident findings feed back into tests, runbooks, risks, or ADRs.

## Related documents

- [Deployment and Recovery](deployment-and-recovery.md)
- [Security Architecture](../architecture/security-architecture.md)
- [Risks](../knowledge/risks.md)
