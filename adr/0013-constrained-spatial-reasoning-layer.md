# ADR-0013: Constrained Spatial Reasoning Layer

- Status: Accepted
- Date: 2026-08-12
- Deciders: OSIP Architecture
- Tags: spatial-model, reasoning, policy, intent, safety, explainability

## Context

The phrase *automation layer* is too broad for the architectural role that distinguishes OSIP from device-centric smart-home systems. A conventional automation layer commonly maps a trigger, schedule, or device state directly to a predefined command. That remains useful for low-level deterministic execution, but it cannot describe how OSIP interprets a request or observation in relation to a physical space, available assets, user role, policy, safety, privacy, energy constraints, and current evidence.

Using the same term for both activities risks hiding the central product boundary: Home Assistant or another provider may execute simple automations, while OSIP must make attributable, constrained decisions at the level of spaces and desired outcomes.

## Decision

OSIP names its decision-making domain capability the **Constrained Spatial Reasoning Layer** (CSRL).

CSRL receives a canonical event or typed intent and reasons over the versioned digital twin, spatial relationships, asset capabilities and bindings, context freshness/confidence, actor and role, policy, authorization, safety, privacy, energy constraints, and provider health. It produces one of three explainable outcomes: reject/request approval, a recommendation, or an attributable execution plan. It does not translate a protocol payload or directly command an actuator.

Deterministic automation remains a subordinate execution mechanism. It may evaluate narrow local triggers, schedules, hard safety rules, and an accepted execution plan, but it cannot become a hidden second policy engine or an alternate path around CSRL for consequential actions.

AI may contribute interpretation, ranking, recommendation, or a proposed typed intent. AI output enters CSRL as untrusted input and never gains direct actuator authority. The Layer must remain usable without AI for declared local-first functions.

## Consequences

- Architecture, C4 views, and specifications distinguish CSRL from integration providers and deterministic execution.
- OSIP applications address a site, space, outcome, and constraints instead of provider-specific device commands whenever possible.
- Every consequential CSRL decision records input evidence references, twin/configuration and policy versions, actor, selected bindings, constraints, plan or rejection, and observed outcome.
- Home Assistant and similar products remain useful providers and may host non-critical technical automation, but they are not the CSRL.
- The first reference deployment must demonstrate one local, non-AI CSRL workflow with a spatial context, policy evaluation, explainable plan, deterministic execution, and observed completion.

## Alternatives considered

| Alternative | Why not selected |
| --- | --- |
| Keep the name “automation layer” | Conflates device-trigger rules with constrained, spatial, policy-aware reasoning. |
| Call it an “AI layer” | Incorrectly makes an AI model the architectural authority and obscures local deterministic operation. |
| Put all reasoning inside Home Assistant | Couples the OSIP domain to one product and prevents a portable provider boundary. |
| Allow each application to decide directly | Duplicates policy, safety, and audit logic and makes outcomes inconsistent. |

## Related documents

- [Constrained Spatial Reasoning Layer](../docs/en/architecture/constrained-spatial-reasoning-layer.md)
- [Intent, Policy, and Execution](../docs/en/architecture/intent-policy-and-execution.md)
- [Edge Runtime](../docs/en/architecture/edge-runtime.md)
- [AI Architecture](../docs/en/ai/ai-architecture.md)
