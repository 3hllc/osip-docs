# End-to-End Operating Model

## Purpose

This view explains how OSIP operates a physical space end to end. It complements the C4 diagrams: C4 identifies systems and containers, while this diagram shows the canonical information and control path. The central distinction is that integration technology connects OSIP to the physical environment, but the **Constrained Spatial Reasoning Layer** decides what may happen in a space under explicit constraints.

```mermaid
flowchart TB
  subgraph PHYSICAL[Physical environment]
    DEV[Devices, engineering systems and manual controls]
    PROTO[Zigbee, BACnet, KNX, Modbus, vendor APIs and other protocols]
    DEV <--> PROTO
  end

  subgraph INTEGRATION[Replaceable integration boundary]
    Z2M[Zigbee2MQTT or another protocol bridge]
    HA[Home Assistant]
    PROVIDERS[Integration providers\nHomeAssistantProvider and direct providers]
    RAW[Raw telemetry and diagnostics\nprovenance-controlled]
    Z2M --> PROVIDERS
    HA --> PROVIDERS
    PROVIDERS --> RAW
  end

  subgraph EDGE[OSIP Edge Runtime — local-first critical path]
    BUS[Canonical OSIP Bus\nversioned events and routed commands]
    TWIN[Digital Twin\nsite, spaces, assets, capabilities, bindings and context]
    POLICY[Policy Engine\nauthorization, safety, privacy, energy and approval]
    CSRL[Constrained Spatial Reasoning Layer\ninterprets spatial context and creates an explainable decision]
    PLAN[Attributable Execution Plan\nselected bindings, constraints, verification and fallback]
    EXEC[Deterministic Execution\nlocal rules, approved plans, verification and safe degradation]
    STATE[(Local state, configuration and audit)]

    BUS --> TWIN
    TWIN --> CSRL
    POLICY --> CSRL
    CSRL -->|recommend / reject / request approval| EXPLAIN[Explanation for a person or application]
    CSRL -->|permitted| PLAN --> EXEC --> BUS
    TWIN <--> STATE
    POLICY <--> STATE
    CSRL <--> STATE
    EXEC --> STATE
  end

  subgraph EXPERIENCE[Applications and people]
    APP[Operator, tenant, installer and vertical applications]
    HUMAN[Human decision and manual override]
    APP -->|typed intent, query or approved configuration request| CSRL
    EXPLAIN --> APP
    HUMAN --> APP
  end

  subgraph OPTIONAL[Optional, non-critical services]
    CONTROL[OSIP Fleet / Control Plane\ncommissioning, configuration, rollout, health and audit]
    AI[AI capabilities\nintent interpretation, recommendation and anomaly detection]
    CONTROL -. versioned configuration and evidence sync .-> STATE
    AI -. proposed intent or interpretation only .-> CSRL
  end

  PROTO --> Z2M
  PROTO --> HA
  PROTO --> PROVIDERS
  PROVIDERS -->|canonical observations, state, health| BUS
  BUS -->|authorized canonical commands| PROVIDERS
  PROVIDERS --> PROTO
```

## Reading the diagram

1. Devices and engineering systems communicate through their native protocols. Zigbee2MQTT and Home Assistant are useful integration paths, not OSIP domain dependencies.
2. Providers validate the asset binding and convert external data into canonical OSIP events. Raw telemetry remains separately retained for diagnosis and reprocessing.
3. The local OSIP bus distributes canonical facts. The digital twin attaches spatial meaning, relationships, freshness, provenance, and health.
4. CSRL evaluates the requested outcome or observed situation against the twin, policy, actor authority, and evidence quality. Its result is an explanation, recommendation, denial, approval request, or execution plan.
5. Deterministic execution carries out only the permitted plan through an eligible provider, verifies the observed result, and records audit evidence.
6. Fleet/control plane and AI may improve operation, but neither is synchronously required for a declared local critical path. AI proposes an interpretation or intent; it never commands an actuator directly.

## Local continuity rule

The solid route through OSIP Edge is the declared local-first path. For an `edge-required` capability it must remain operational during WAN loss and without an AI service, control plane, or Home Assistant dependency. Dashed links are optional enhancement, configuration synchronisation, or recommendation paths.

## Related documents

- [Architecture Overview](architecture-overview.md)
- [Integration Providers](integration-providers.md)
- [Constrained Spatial Reasoning Layer](constrained-spatial-reasoning-layer.md)
- [Edge Runtime](edge-runtime.md)
- [Fleet and Control Plane](fleet-control-plane.md)
