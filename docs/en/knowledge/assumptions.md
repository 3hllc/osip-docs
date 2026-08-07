# Assumptions

## Purpose

An assumption lets the project proceed while evidence is incomplete. It is not a hidden requirement or a decision. Every assumption must be testable, have a review point, and state what changes if it proves false. Invalidated assumptions are updated in place with their outcome and linked follow-up work.

## Current assumptions

| ID | Assumption | Validation approach | Consequence if false | Review point |
| --- | --- | --- | --- | --- |
| A-001 | The reference apartment can host a reliable local compute, storage, and network environment with planned power and backup arrangements. | Inventory physical locations, power capacity, network segmentation, and recovery tests. | Change the edge deployment design and scope or add infrastructure work before integration. | Reference-design approval |
| A-002 | A Zigbee-based device network can meet the initial low-power sensing and control needs when its router topology is intentionally designed. | Radio survey, commissioning evidence, command latency, and router-loss recovery tests. | Use additional routers, another radio technology, or revise the supported device matrix. | Before reference-apartment acceptance |
| A-003 | MQTT can serve as the initial local event transport without leaking MQTT topics into the OSIP domain model. | Review contracts and adapter code; test a simulated alternate producer. | Strengthen the adapter boundary or reassess the backbone decision. | Before the first production-like integration |
| A-004 | English can remain the canonical technical source while Russian pages preserve the same site structure and are translated incrementally. | Review language switch, navigation parity, and translation workflow with contributors. | Revise documentation strategy and localisation workflow. | Before external installer documentation |
| A-005 | Cloud capabilities can be optional for the first operational use cases. | Execute WAN-loss scenarios for all declared local-first functions. | Reclassify affected functions, add local components, or reduce their scope. | Architecture baseline review |
| A-006 | The platform can begin with a constrained, explicit capability catalog instead of attempting universal device support. | Approve the initial capability matrix and track unsupported integration requests. | Expand the catalog through versioned contracts and reference-design validation. | Each release-planning review |

## Management rules

Assumptions do not silently become facts. A pull request that relies on a new assumption adds it here or references an existing ID. When evidence validates an assumption, its conclusion is captured in the relevant specification or decision log; when it fails, the owner creates or updates the linked risk, ADR, or design work before continuing.

## Related records

- [Open Questions](open-questions.md)
- [Constraints](constraints.md)
- [Risks](risks.md)
- [Project Principles](../foundation/project-principles.md)
