# Edge Runtime

## Purpose

The OSIP Edge runtime is the site-local execution environment for declared local-first functions. It receives canonical events, projects relevant state, hosts the locally required part of the Constrained Spatial Reasoning Layer, evaluates assigned policy, executes deterministic plans, and issues commands through eligible providers. It is a product boundary: a site remains safely operable when WAN access, cloud services, AI services, or the fleet/control plane are unavailable.

## Responsibilities

- Maintain the site-scoped subset of asset bindings, capabilities, relationships, policies, desired state, and authorization scope required for local operation.
- Consume and publish canonical events and commands through the selected local OSIP transport.
- Run the local CSRL workflow, deterministic plan execution, command verification, health evaluation, and audit buffering for assigned local functions.
- Enforce conservative degradation and manual-override behaviour for safety- or business-critical actions.
- Reconcile configuration, policy, software versions, and audit evidence with the fleet/control plane when connectivity is available.

The edge runtime does not require Home Assistant to be present for a declared critical path. Home Assistant may operate in parallel as a provider, discovery source, dashboard, or non-critical automation platform. A provider failure produces an explicit degraded state; it does not silently transfer authority to an unrelated component.

## Local continuity contract

Every supported capability declares whether it is `edge-required`, `edge-preferred`, `centrally-assisted`, or `cloud-enhanced`. For `edge-required` capability, the deployment documents the local inputs, provider bindings, policies, command path, verification evidence, failure state, manual override, recovery objective, and outage test. A cache alone is not local-first: the edge must have enough current authorised configuration and executable logic to act safely.

## Control plane separation

The fleet/control plane distributes reviewed configuration and policy, registers sites and providers, coordinates rollout, and receives operational evidence. It never becomes a synchronous dependency for the site’s declared critical control loop. During disconnection, the edge enforces its last valid assigned configuration, records drift and audit data, and reconciles through an explicit versioned process when connectivity returns.

## Minimum reference-deployment evidence

The Reference Apartment must demonstrate at least one end-to-end `edge-required` workflow using a canonical event, asset/capability mapping, local policy, deterministic execution, observed completion, and an outage test that removes WAN access and Home Assistant from the required path. The test evidence includes command latency, failure behaviour, recovery steps, audit record, and known limits.

## Related documents

- [Constrained Spatial Reasoning Layer](constrained-spatial-reasoning-layer.md)
- [Intent, Policy, and Execution](intent-policy-and-execution.md)
- [Integration Providers](integration-providers.md)
- [Deployment Architecture](deployment-architecture.md)
- [Deployment and Recovery](../operations/deployment-and-recovery.md)
