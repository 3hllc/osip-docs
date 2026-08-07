"""Build hooks for OSIP documentation.

PlantUML source remains versioned in the repository-level ``diagrams/`` folder.
Before MkDocs collects documentation files, this hook creates local SVG derivatives under
``docs/en/assets/plantuml/``. Generated files are deliberately ignored by Git.
"""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path


def on_config(config, **kwargs):
    """Render PlantUML early enough for MkDocs to register the SVG files."""
    project_root = Path(config.config_file_path).parent
    source_dir = project_root / "diagrams"
    output_dir = project_root / "docs" / "en" / "assets" / "plantuml"
    sources = sorted(source_dir.glob("*.puml"))

    if not sources:
        return config

    plantuml_jar = os.environ.get("PLANTUML_JAR")
    plantuml_bin = os.environ.get("PLANTUML_BIN") or shutil.which("plantuml")
    if plantuml_jar:
        java = os.environ.get("JAVA_BIN") or shutil.which("java")
        if not java:
            raise RuntimeError("PLANTUML_JAR is set but no Java executable was found.")
        renderer = [java, "-jar", plantuml_jar]
    elif plantuml_bin:
        renderer = [plantuml_bin]
    else:
        raise RuntimeError(
            "PlantUML is required to build OSIP documentation. Install the "
            "'plantuml' executable, set PLANTUML_BIN, or set PLANTUML_JAR "
            "to the official plantuml.jar file."
        )

    output_dir.mkdir(parents=True, exist_ok=True)
    for source in sources:
        subprocess.run(
            [*renderer, "-tsvg", "-charset", "UTF-8", "-o", str(output_dir), str(source)],
            check=True,
            cwd=project_root,
        )

    return config
