# Fleet and Control Plane

## Purpose

The OSIP Fleet and Control Plane operates many sites, edge runtimes, providers, and deployment versions consistently. It is distinct from the site-local data and critical execution path. The control plane makes commissioning, configuration, health, support, audit, rollout, and tenant boundaries manageable across a fleet without making a remote service the owner of local safety.

## Scope

The control plane maintains fleet inventory and topology; site and edge registration; provider lifecycle/configuration; commissioning and asset-binding evidence; policy and automation distribution; versioning, staged rollout, rollback, health, drift, diagnostics, audit, access control, tenant scope, and approval workflows. It can register a Home Assistant instance, MQTT bridge, BACnet provider, or direct provider as a managed provider and show its health, configuration version, bindings, and provenance.

It must not carry raw high-volume site telemetry by default, issue an unreviewed remote command into a critical loop, or remove the authority of local policy. Data egress, remote support, and fleet analytics are explicitly classified and authorized per capability and tenant.

## Site lifecycle

1. Register a site and create its tenant/access boundaries.
2. Register an edge runtime and establish a purpose-limited management identity.
3. Register providers and discover candidate endpoints.
4. Commission verified endpoints into OSIP assets, relationships, capabilities, and binding roles.
5. Distribute versioned configuration, policies, and automation with acceptance criteria.
6. Observe health, drift, incidents, audit evidence, and recovery readiness.
7. Use staged rollout and explicit rollback for every material runtime, provider, policy, or contract change.

## Configuration authority and drift

The control plane owns reviewed desired configuration; the edge records the applied version and locally detected drift. An installer may make an authorised emergency correction, but it must become a reconciled configuration change rather than a permanent untracked local exception. Rollout requires compatibility checks for edge version, provider version, asset/capability contract, policy, and rollback target.

## Product sequencing

Fleet capability is a product direction, not an MVP prerequisite. The Reference Apartment establishes the data model and evidence needed for later multi-site operation: site scope, stable assets, provider registration, configuration version, policy version, health, audit, and recovery. A dedicated control-plane implementation begins only when multiple sites or repeatable Installer Edition deployments create an operational need.

## Related documents

- [Edge Runtime](edge-runtime.md)
- [Physical Asset Model](physical-asset-model.md)
- [Operations Overview](../operations/README.md)
- [Commercial and Installer Edition Strategy](../product/commercial-strategy.md)
