# AI Capability Roadmap

## Principle

AI is architecturally native and runtime-optional. It is designed into OSIP’s contextual data, policy, privacy, evaluation, and explanation model, while critical and safety-relevant local functions retain deterministic operation without AI.

## Capability progression

| Capability | First useful role | Guardrail |
| --- | --- | --- |
| Context Engine | Derive approved spatial, temporal, occupancy, and system context from normalized facts. | Preserve source, confidence, freshness, and privacy classification. |
| Spatial Reasoning | Relate zones, objects, devices, and tasks to a coordinate/semantic model. | Never invent physical certainty or override explicit safety constraints. |
| Voice | Translate authorized user requests into typed intents and explanations. | Require identity, confirmation for consequential actions, and non-voice fallback. |
| Computer Vision | Produce privacy-governed observations such as object or spill detection. | Consent, retention, local/cloud boundary, accuracy evaluation, and human review path are explicit. |
| Robotics | Propose and coordinate bounded tasks such as inspection or cleaning. | Robot actions remain within mapped zones, policy, safety, and manual-stop constraints. |
| Behaviour Learning | Recommend comfort, energy, or routine changes from approved history. | Explainability, opt-in, retention limit, uncertainty, and easy rejection are required. |

## Delivery rule

Every capability begins with a concrete user or installer job, defined data inputs, deterministic fallback, harmful-action analysis, test corpus or scenario, success/error metrics, cost/latency limit, and rollback/disable control. AI outputs are recommendations or typed intents; policy and authorization own the final command decision.

## Related documents

- [AI Architecture](ai-architecture.md)
- [Digital Twin](../architecture/digital-twin.md)
- [ADR-0007 - AI-Native, Runtime-Optional Operation](https://github.com/3hllc/osip-docs/blob/main/adr/0007-ai-native-optional.md)
