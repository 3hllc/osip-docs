# Domain Model

## Bounded domain

The OSIP domain describes the installation and its intentional behaviour independently of protocols and vendors. Its core concepts are Installation, Space, Zone, Object, Device, Capability, Person, Role, Event, Context, Policy, Intent, Task, and Audit Record.

An Installation owns a digital twin, supported identities, configuration, policies, and operational history. Spaces and zones provide physical and semantic context. Devices expose capabilities through adapters and produce observations. Policies decide whether an intent is permissible; tasks coordinate multi-step work; audit records preserve the reason, actor, decision, and outcome.

## Invariants

- Stable OSIP identifiers are never derived solely from vendor identifiers.
- A device can be unknown or unhealthy without invalidating its containing space.
- An observation is evidence, not a command and not an authorization decision.
- A policy decision is attributable to a versioned policy and an identity or system actor.
- A task's requested outcome is distinct from its execution attempts and observed results.

Protocol-specific addresses, protocol payloads, and vendor entity IDs remain inside adapter models. Their mapping to a capability and OSIP identity is explicit and testable.
