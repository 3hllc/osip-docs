# OSIP

OSIP is the **Open Spatial Intelligence Platform**: an open, modular platform for intelligent physical environments. It is not a smart-home distribution and it is not a wrapper around any one integration product. It models spaces, people, devices, events, context, and tasks so that automation, AI, robotics, and engineering systems can work as one coherent environment. The first reference deployment is residential; it validates the platform but does not limit its scope to residential use.

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

## Local documentation preview

Create the project-local Python environment once, ensure that local PlantUML is available, then run the development server:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements-docs.lock
.\.venv\Scripts\python scripts/render_plantuml.py
.\.venv\Scripts\python -m mkdocs serve
```

Use `.\.venv\Scripts\python` for every local documentation command; do not install documentation dependencies into the global Python environment. Run `scripts/render_plantuml.py` after changing a `.puml` source, then start or refresh MkDocs. Mermaid uses the versioned local bundle in `docs/assets/javascripts/`, so builds and rendered pages do not depend on a CDN. The renderer writes only stale SVG files and runs outside MkDocs, preventing a `mkdocs serve` rebuild loop. Select either rendered diagram to open the zoomable viewer. For a strict production-equivalent check, run `$env:NO_MKDOCS_2_WARNING='true'; .\.venv\Scripts\python -m mkdocs build --strict`.

## Contributing

Use GitHub issues to propose work, document significant technical choices in `adr/`, and keep English and Russian project documents aligned where both versions exist.

## License

License selection is pending.
