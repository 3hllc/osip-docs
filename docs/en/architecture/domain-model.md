# Domain Model

## Bounded domain

The OSIP domain describes a physical environment and its intentional behaviour independently of protocols and vendors. Its core concepts are Site, Building, Floor, Space, Zone, Asset, Capability, Binding, Provider, Person, Role, Event, Context, Policy, Intent, Execution Plan, Task, and Audit Record. An installation is a deployable OSIP runtime associated with a site; it is not the sole owner of physical identity.

A Site owns a digital twin, supported identities, configuration, policies, and operational history. Buildings, floors, spaces, and zones provide physical and semantic context. Assets expose capabilities through providers and produce observations. A Binding links an OSIP asset to an external provider identity without replacing its stable identity. Policies decide whether an intent is permissible; the Constrained Spatial Reasoning Layer creates an execution plan; tasks coordinate multi-step work; audit records preserve the reason, actor, decision, and outcome.

## Invariants

- Stable OSIP asset identifiers are never derived solely from vendor identifiers.
- A provider binding can be unknown or unhealthy without invalidating the asset or its containing space.
- A site hierarchy and an asset relationship graph are distinct: zones, service relationships, safety boundaries, and access areas may cross a containment tree.
- An observation is evidence, not a command and not an authorization decision.
- A policy decision is attributable to a versioned policy and an identity or system actor.
- An intent's requested outcome is distinct from its execution plan, attempts, and observed results.

Protocol-specific addresses, protocol payloads, and vendor entity IDs remain inside provider models. Their mapping to an OSIP asset, capability, and binding is explicit, testable, and auditable.
