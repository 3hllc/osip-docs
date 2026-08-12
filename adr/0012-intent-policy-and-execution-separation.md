---
title: ADR-0012 - Separate Intent, Policy, and Execution
status: accepted
date: 2026-08-12
deciders: [OSIP Project]
tags: [intent, policy, constrained-spatial-reasoning, execution, safety, applications]
---

# ADR-0012 - Separate Intent, Policy, and Execution

## Context

Applications and users should be able to request a desired outcome for a physical space without orchestrating provider-specific device commands. At the same time, a high-level request must not become an implicit authorization bypass. Mixing desired state, safety policy, spatial reasoning, provider selection, and execution inside one automation makes the system difficult to audit, explain, migrate, and operate.

## Decision

OSIP separates digital twin, policy, the Constrained Spatial Reasoning Layer, deterministic execution, and provider execution. An intent describes a scoped outcome. Policy evaluates permission, constraints, approval, and safety. The Constrained Spatial Reasoning Layer creates an attributable execution plan that selects eligible assets, capabilities, bindings, verification evidence, and safe fallbacks. Deterministic execution carries out the accepted plan through providers or the edge runtime. AI may propose an intent or plan but never gains direct actuator authority.

## Alternatives considered

| Alternative | Reason not selected |
| --- | --- |
| Applications send direct provider commands | Couples applications to integrations and bypasses reusable policy, audit, and fallback logic. |
| Encode all behaviour in automation rules | Mixes outcome, policy, state, and execution; cannot provide a stable application/control-plane model. |
| Let AI choose and issue commands directly | Is incompatible with deterministic safety, authorization, explainability, and local continuity requirements. |

## Consequences

OSIP must define intent schemas, policy decision records, execution-plan lifecycle, correlation, approval, and verification semantics. The initial MVP implements one narrow, evidence-backed intent rather than a general natural-language controller. This introduces modelling work but creates a durable application boundary and makes multiple provider bindings safely usable.

## Links

- [Intent, Policy, and Execution](../docs/en/architecture/intent-policy-and-execution.md)
- [Constrained Spatial Reasoning Layer](../docs/en/architecture/constrained-spatial-reasoning-layer.md)
- [AI Architecture](../docs/en/ai/ai-architecture.md)
- [Edge Runtime](../docs/en/architecture/edge-runtime.md)
