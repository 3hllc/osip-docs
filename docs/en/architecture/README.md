# Architecture

This section describes the platform before implementation. OSIP is an operational control plane for physical spaces, not a smart-home dashboard or a Home Assistant distribution. It owns the spatial, asset, capability, policy, intent, and operational model; providers such as Home Assistant, MQTT bridges, BACnet, KNX, and vendor APIs remain replaceable infrastructure beneath its canonical boundary.

Read the [Physical Asset Model](physical-asset-model.md) for the site/space/asset hierarchy, [Integration Providers](integration-providers.md) for the canonical boundary, and [Intent, Policy, and Execution](intent-policy-and-execution.md) for how a requested outcome becomes a controlled action. [Edge Runtime](edge-runtime.md) defines local continuity; [Fleet and Control Plane](fleet-control-plane.md) defines multi-site operation without becoming part of the critical path.

The [End-to-End Operating Model](end-to-end-operating-model.md) shows the complete high-level path from physical devices through integration providers, canonical OSIP contracts, constrained spatial reasoning, deterministic execution, and observed outcome.

The [Zigbee Mesh and MQTT Bridge](zigbee-mesh-and-mqtt-bridge.md) specification separates the physical Zigbee device mesh from MQTT transport. It does not make Zigbee2MQTT or MQTT the OSIP domain model.
