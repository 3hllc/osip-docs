# Reference Apartment Engineering Design

## Purpose

The approximately 165 m² reference apartment is OSIP’s first physical validation environment. It tests a repeatable system design rather than collecting attractive devices. The apartment is simultaneously an engineering laboratory, demonstration environment, commissioning rehearsal, and source of Installer Edition evidence.

## Engineering scope

The design records requirements and interfaces for suspended-ceiling engineering space, network and power, lighting and shading, access and security, leak protection, HVAC (including VRF and/or heat-pump equipment, ceiling fan coils, radiant floor heating), humidification and dehumidification, sensors, cameras, voice, and approved robotics. A listed system is a design scope, not an approved device purchase.

## Design work packages

| Work package | Required evidence |
| --- | --- |
| Spatial baseline | Named rooms, zones, coordinate convention, furniture/object model, privacy classification, and change-control rule. |
| Building systems | Interface inventory, safe states, manual overrides, electrical and water dependencies, actuator ownership, and commissioning sequence. |
| Network and radio | Trust zones, wired/wireless coverage, coordinator placement, Zigbee router rationale, failure behaviour, and acceptance walk-through. |
| Device/capability matrix | Required capability, location, adapter, stable identity, power/network dependency, health signal, supported lifecycle, and fallback. |
| Local runtime | Service placement, power-loss behaviour, backup/restore objective, authorized access path, monitoring, and upgrade/rollback plan. |
| User experience | Explicit user/installer jobs, manual controls, explainability for consequential automation, consent boundaries, and accessibility considerations. |

## Commissioning gates

Commissioning proceeds in ordered layers: infrastructure and power; network/time; local runtime; powered radio routers; end devices and building-system adapters; normalized contracts; automation; then optional AI experiences. Each gate has recorded tests. WAN loss, adapter restart, router loss, device replacement, restore from backup, and safe-manual override are mandatory demonstrations for the capabilities they affect.

## Repeatability rule

An apartment-specific workaround is not a product pattern. Every accepted pattern must state installation time, dependencies, tools, skills, evidence, maintenance burden, replacement procedure, and conditions under which it should not be used. Unresolved variations create an open question or risk, not undocumented installer judgement.

## Related documents

- [Reference Apartment](reference-apartment.md)
- [Zigbee Mesh and MQTT Bridge](../architecture/zigbee-mesh-and-mqtt-bridge.md)
- [Deployment Architecture](../architecture/deployment-architecture.md)
- [Installer Playbook](../operations/installer-playbook.md)
