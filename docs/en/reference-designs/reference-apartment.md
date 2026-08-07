# Reference Apartment

## Role

The approximately 165 m² reference apartment is OSIP's first engineering laboratory, test bed, demonstration environment, and source of deployment requirements. It validates product assumptions under real daily operation. It is not a bespoke exception: every decision records whether it can become a repeatable installer pattern.

## Engineering scope

The design anticipates suspended-ceiling engineering space, radiant floor heating, VRF and/or heat-pump equipment, ceiling fan coils, humidity control and dehumidification, leak protection, electrical safety, lighting, curtains, access control, security, robotics, voice interaction, and AI-assisted experiences. These are candidate scopes, not an unapproved hardware list.

## Required design records

- A named space and zone model with the coordinate/reference convention.
- Network and trust-zone topology, service placement, and local-control failure behaviour.
- Device/capability register with placement, integration adapter, health requirements, and lifecycle status.
- BOM entries linked to the supported capability and ADR/research evidence.
- Commissioning sequence, acceptance tests, backup/recovery procedure, and installer handover record.
- Operational lessons that update the Installer Edition rather than remaining local knowledge.

## Acceptance evidence

The installation is accepted incrementally: critical functions must work through a simulated WAN loss; a device or adapter outage must be visible and degrade safely; a consequential automation must be traceable from evidence to outcome; and a trained operator must be able to execute the documented recovery path.
