# Installer Playbook

## Purpose

The playbook turns a validated reference pattern into repeatable installer work. It does not assume hidden founder knowledge or unrestricted administrative access.

## Delivery sequence

1. Confirm approved reference design, capability matrix, constraints, customer consent, and safety boundaries.
2. Survey power, network, RF, equipment interfaces, manual overrides, and installation access.
3. Install infrastructure and local runtime; capture baseline configuration and backup evidence.
4. Commission powered network and radio foundation before battery endpoints.
5. Join and map devices through controlled identity lifecycle; verify normalized capability contracts.
6. Execute acceptance scenarios, including WAN loss, recovery, access control, and safety overrides.
7. Deliver handover: inventory, topology, credentials procedure, local access, backup/recovery, support contacts, limitations, and customer training.

## Evidence standard

Each step records installer role, date, artefact, test result, exception, and next action. A failed or deferred test is visible in the handover package. Photos, plans, and personal layout data are handled under the documented privacy classification and are not committed to a public repository.

## Escalation

If a proposed field change alters a capability contract, security boundary, radio topology, recovery objective, or repeatability assumption, the installer pauses that work package and records an open question, risk, or proposed ADR. The reference apartment is allowed to explore; an Installer Edition deployment is not.

## Related documents

- [Reference Apartment Engineering Design](../reference-designs/reference-apartment-engineering.md)
- [Deployment and Recovery](deployment-and-recovery.md)
- [Open Questions](../knowledge/open-questions.md)
