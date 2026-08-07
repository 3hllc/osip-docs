# OSIP

OSIP is the **Open Spatial Intelligence Platform**: an open, modular platform for intelligent physical environments. It is not a smart-home distribution and it is not a wrapper around any one integration product. It models spaces, people, devices, events, context, and tasks so that automation, AI, robotics, and engineering systems can work as one coherent environment.

## Getting started

- English documentation source: [docs/en](docs/en/)
- Russian documentation source: [docs/ru](docs/ru/)
- Foundation and governing documents: [docs/en/foundation](docs/en/foundation/)
- Architecture Decision Records: [adr](adr/)
- Diagram sources: [diagrams](diagrams/)

## Repository layout

```text
docs/             Canonical Markdown documentation published by MkDocs
diagrams/         Versioned PlantUML and Mermaid diagram sources
adr/              Architecture Decision Records
research/         Research notes and experiments
bom/              Bills of materials
installer/        Installation and provisioning tools
deployment/       Deployment definitions and runbooks
cloud/            Cloud configuration and services
ai/               AI components, prompts, and models
api/              API contracts and implementations
reference_apartment/ Reference deployment and apartment-specific materials
```

The documentation repository is the canonical source of knowledge. The MkDocs site, PDFs, presentations, and any external wiki pages are generated or derived views. Do not duplicate a subject: link to its canonical document instead.

## Contributing

Use GitHub issues to propose work, document significant technical choices in `adr/`, and keep English and Russian project documents aligned where both versions exist.

## License

License selection is pending.
