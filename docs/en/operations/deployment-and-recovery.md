# Deployment and Recovery

## Purpose

This specification defines the deployment and recovery expectations for a local OSIP installation. Executable definitions belong in `deployment/`; this page defines the required evidence and operator outcomes.

## Deployment contract

Every deployment identifies service versions, non-secret configuration, dependencies, network identities, health checks, data stores, backup scope, upgrade path, rollback point, and owner role. Configuration is reproducible from versioned source plus controlled secrets. Manual, unrecorded changes to a running installation are treated as drift and reconciled into the documented configuration or removed.

## Offline installation and recovery

An authorized installer must be able to commission, diagnose, and restore declared local-first capabilities without a WAN connection. The handover package includes local access instructions, network topology, software inventory, device/coordinator recovery procedure, backup location, restore verification, and emergency manual overrides. Optional cloud enrolment occurs after local acceptance and cannot block it.

## Backup, update, rollback

Backups are encrypted, access-controlled, and tested by restoration. They cover the data and configuration needed to meet the declared recovery objective, but never expose credentials in Git. Updates are staged against a compatibility matrix, have a defined rollback decision, and leave health evidence. A failed update must degrade visibly and preserve safe manual control.

## Acceptance scenarios

- Restore a local host or service from documented backup evidence.
- Restart an adapter and show that duplicate or delayed events do not corrupt state.
- Simulate WAN loss and prove declared local functions continue.
- Replace a device using the identity-lifecycle procedure.
- Roll back a compatible service update and retain auditability.

## Related documents

- [Deployment Architecture](../architecture/deployment-architecture.md)
- [Observability](observability.md)
- [Installer Playbook](installer-playbook.md)
