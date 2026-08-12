# Scripts

Store reproducible maintenance, validation, and publishing helpers here. Scripts should document inputs, outputs, required tooling, and whether they modify repository state.

## Documentation helpers

`render_plantuml.py` renders only missing or stale `diagrams/*.puml` sources to shared SVG files in `docs/assets/plantuml/`. It requires a local `plantuml` executable, or `PLANTUML_BIN`, or `PLANTUML_JAR` together with Java. Run it before a local MkDocs preview and in CI before `mkdocs build`; it intentionally does not run as an MkDocs hook, because writing into `docs/` from a hook causes a `mkdocs serve` rebuild loop.

`check_translation_parity.py` verifies that each English documentation page has a Russian page at the same relative path and that the Russian page declares `translation_status: current` and `source_language: en`. It runs in CI before the site is built. It enforces structural currency; reviewer approval remains responsible for the accuracy of the Russian translation.

`check_translation_parity.py` verifies that each English documentation page has a Russian page at the same relative path and that the Russian page declares `translation_status: current` and `source_language: en`. It runs in CI before the site is built. It enforces structural currency; reviewer approval remains responsible for the accuracy of the Russian translation.
