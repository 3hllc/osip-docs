"""Fail documentation checks when the English and Russian trees drift structurally."""

from __future__ import annotations

from pathlib import Path
import re
import sys


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
ENGLISH_ROOT = REPOSITORY_ROOT / "docs" / "en"
RUSSIAN_ROOT = REPOSITORY_ROOT / "docs" / "ru"
REQUIRED_METADATA = {
    "translation_status": "current",
    "source_language": "en",
}


def markdown_files(root: Path) -> set[Path]:
    return {path.relative_to(root) for path in root.rglob("*.md")}


def front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip('"\'')
    return result


def main() -> int:
    english = markdown_files(ENGLISH_ROOT)
    russian = markdown_files(RUSSIAN_ROOT)
    errors: list[str] = []

    for relative_path in sorted(english - russian):
        errors.append(f"Missing Russian translation: docs/ru/{relative_path}")
    for relative_path in sorted(russian - english):
        errors.append(f"Russian page without English source: docs/ru/{relative_path}")

    for relative_path in sorted(english & russian):
        russian_path = RUSSIAN_ROOT / relative_path
        metadata = front_matter(russian_path)
        for key, expected in REQUIRED_METADATA.items():
            if metadata.get(key) != expected:
                errors.append(
                    f"docs/ru/{relative_path}: expected front-matter "
                    f"{key}: {expected}"
                )

    if errors:
        print("Translation parity check failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1

    print(f"Translation parity: {len(english)} EN pages and {len(russian)} RU pages are current.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
