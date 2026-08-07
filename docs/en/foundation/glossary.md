# Glossary

## Purpose

This glossary establishes the preferred meanings of terms used across OSIP specifications, ADRs, reference designs, and installer material. A term defined here should not be redefined locally without an explicit, documented reason. Product names and vendor-specific vocabulary belong in an integration document unless the term is required to interpret an OSIP contract.

## Platform terms

| Term | Meaning in OSIP |
| --- | --- |
| **OSIP** | Open Spatial Intelligence Platform: a local-first platform and set of repeatable practices for spatially aware environments. It is not a single vendor product or a synonym for Home Assistant. |
| **Local First** | Required functions continue on the trusted local environment during WAN loss. Cloud services may enhance a function, but cannot be its only control path unless explicitly classified as cloud-dependent. |
| **Cloud Enhanced** | A cloud capability that is optional for normal local operation, such as remote access, opt-in backup, fleet insights, or heavyweight inference. |
| **Reference apartment** | The 165 m² real-world validation environment used to prove designs, commissioning procedures, failure recovery, and evidence before a pattern is productized. |
| **Reference deployment** | A real environment used to validate an OSIP capability profile. The Reference Apartment is the first such deployment; it does not define the platform's scope or future supported space types. |
| **Installer Edition** | A future repeatable delivery package derived from validated reference designs, including installation, commissioning, support, and acceptance material. |
| **Adapter** | A bounded component that translates a vendor, protocol, or product-specific interface into OSIP contracts. It prevents implementation details from becoming domain-model dependencies. |
| **Integration boundary** | The interface at which external payloads, identities, credentials, availability, and errors are normalized before general OSIP services consume them. |

## Model and interaction terms

| Term | Meaning in OSIP |
| --- | --- |
| **Spatial model** | The durable representation of spaces, zones, objects, relationships, and contextual meaning in an environment. |
| **Digital twin** | A time-aware, attributable projection of relevant physical and contextual state. It is not a complete copy of every vendor payload or a substitute for source-of-truth systems. |
| **Device** | A physical or logical endpoint represented by a stable OSIP `device_id`. Its radio, vendor, and integration identifiers are attributes, not the durable domain identity. |
| **Capability** | A normalized function that a device or service can expose, such as occupancy sensing, dimming, contact state, or temperature measurement. |
| **Observation** | A fact reported by a source at a time, for example a measured temperature or button press. Observations can be late, duplicated, invalid, or stale. |
| **State projection** | The current interpretation derived from observations and commands. It carries source, timestamp, and quality; it must not claim freshness that the platform cannot establish. |
| **Command** | A requested, attributable action. Broker acceptance is not command completion; completion is evidenced by an observed result or documented acknowledgement. |
| **Event** | An immutable record that something happened or changed. Events use versioned contracts and have an owner, time, source, and classification. |
| **Context** | Meaning derived from spatial, temporal, behavioural, and system facts, such as “activity in the kitchen zone after sunset.” |

## Connectivity terms

| Term | Meaning in OSIP |
| --- | --- |
| **MQTT broker** | The local client-server publish/subscribe transport used initially for OSIP message distribution. MQTT is not the OSIP domain model and is not a mesh topology. |
| **Topic** | A transport-facing MQTT routing name. A topic is not sufficient semantic documentation; the versioned event or command contract defines meaning. |
| **Zigbee mesh** | The low-power device radio network between Zigbee endpoints, routers, and a coordinator. It is separate from MQTT and enters OSIP through an integration adapter. |
| **Coordinator** | The Zigbee network root connected to an integration host or gateway. It is a commissioning and recovery asset, not an OSIP core service. |
| **Router** | A Zigbee-capable device that relays radio traffic. A device must be validated as a router; mains power alone does not guarantee useful routing behaviour. |
| **End device** | A Zigbee endpoint, commonly battery-powered, that usually does not relay mesh traffic. |

## Governance terms

| Term | Meaning in OSIP |
| --- | --- |
| **ADR** | Architecture Decision Record: a durable record of a significant decision, its context, consequences, and status. An ADR is not a meeting note. |
| **Decision log** | An index of decisions, including small or temporary ones that do not justify an ADR. It links to an ADR when one exists. |
| **Assumption** | A proposition currently treated as true so work can proceed. It must state validation evidence and the consequence if false. |
| **Constraint** | A binding limitation imposed by safety, law, environment, budget, interoperability, infrastructure, or a prior accepted decision. |
| **Risk** | An uncertain future event with a potential adverse effect. A risk has likelihood, impact, owner, mitigation, and trigger. |
| **Open question** | A decision-relevant unknown with a named next step. It is neither an assumption nor a risk register entry. |

## Naming rules

Use the terms above in headings, event contracts, and diagrams. Prefer precise phrases such as “Zigbee integration adapter” over a vague “bridge,” and “observed completion” over “MQTT delivered.” New cross-document vocabulary is proposed through a pull request that updates this glossary and the relevant specification together.
