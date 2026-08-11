# Scripts

Store reproducible maintenance, validation, and publishing helpers here. Scripts should document inputs, outputs, required tooling, and whether they modify repository state.

## Documentation helpers

`render_plantuml.py` renders only missing or stale `diagrams/*.puml` sources to shared SVG files in `docs/assets/plantuml/`. It requires a local `plantuml` executable, or `PLANTUML_BIN`, or `PLANTUML_JAR` together with Java. Run it before a local MkDocs preview and in CI before `mkdocs build`; it intentionally does not run as an MkDocs hook, because writing into `docs/` from a hook causes a `mkdocs serve` rebuild loop.
