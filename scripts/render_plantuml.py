"""Render stale PlantUML sources for the OSIP documentation site.

This script deliberately runs outside the MkDocs plugin lifecycle. Rendering SVG files
inside a watched ``docs/`` directory from a MkDocs hook creates an infinite rebuild loop
with ``mkdocs serve`` and the static-i18n plugin.
"""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = PROJECT_ROOT / "diagrams"
OUTPUT_DIR = PROJECT_ROOT / "docs" / "assets" / "plantuml"


def renderer() -> list[str]:
    """Return a locally configured PlantUML command."""
    plantuml_jar = os.environ.get("PLANTUML_JAR")
    plantuml_bin = os.environ.get("PLANTUML_BIN") or shutil.which("plantuml")
    if plantuml_jar:
        java = os.environ.get("JAVA_BIN") or shutil.which("java")
        if not java:
            raise RuntimeError("PLANTUML_JAR is set but no Java executable was found.")
        return [java, "-jar", plantuml_jar]
    if plantuml_bin:
        return [plantuml_bin]
    raise RuntimeError(
        "PlantUML is required. Install the 'plantuml' executable, set "
        "PLANTUML_BIN, or set PLANTUML_JAR to the official plantuml.jar file."
    )


def main() -> None:
    sources = sorted(SOURCE_DIR.glob("*.puml"))
    stale_sources = [
        source
        for source in sources
        if not (OUTPUT_DIR / f"{source.stem}.svg").exists()
        or (OUTPUT_DIR / f"{source.stem}.svg").stat().st_mtime_ns
        < source.stat().st_mtime_ns
    ]
    if not stale_sources:
        print("PlantUML SVG files are current; skipping render.")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            *renderer(),
            "-tsvg",
            "-charset",
            "UTF-8",
            "-o",
            str(OUTPUT_DIR),
            *(str(source) for source in stale_sources),
        ],
        check=True,
        cwd=PROJECT_ROOT,
    )
    print(f"Rendered {len(stale_sources)} PlantUML diagram(s).")


if __name__ == "__main__":
    main()
