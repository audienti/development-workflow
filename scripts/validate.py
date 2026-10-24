#!/usr/bin/env python3
"""Check this package's manifests, constrained skill metadata and local links."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


def validate(root):
    errors = []
    manifests = []
    for folder in (".codex-plugin", ".claude-plugin"):
        path = root / folder / "plugin.json"
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            errors.append(f"{path.relative_to(root)}: {exc}")
            continue
        manifests.append(value)
        if value.get("name") != "development-workflow":
            errors.append(f"{folder}: wrong plugin name")
        if not re.fullmatch(r"\d+\.\d+\.\d+", str(value.get("version", ""))):
            errors.append(f"{folder}: expected a release version")
        if not value.get("description"):
            errors.append(f"{folder}: missing description")
        if folder == ".codex-plugin" and value.get("skills") != "./skills/":
            errors.append(f"{folder}: skills must point to ./skills/")
    if len(manifests) == 2 and manifests[0].get("version") != manifests[1].get("version"):
        errors.append("plugin versions differ")

    skills = sorted((root / "skills").glob("*/SKILL.md"))
    expected = {"development-workflow"} | {
        f"workflow-{stage}" for stage in
        ("setup", "intake", "blast-radius", "dry", "plan", "build", "verify", "review", "deliver")
    }
    if {path.parent.name for path in skills} != expected:
        errors.append("expected the ten documented skills")
    for path in skills:
        text = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        if not match:
            errors.append(f"{path.relative_to(root)}: missing frontmatter")
            continue
        fields = dict(re.findall(r"^(name|description): (.+)$", match[1], re.M))
        if fields.get("name") != path.parent.name:
            errors.append(f"{path.relative_to(root)}: name differs from directory")
        description = fields.get("description", "")
        if len(description) < 5 or description[0] not in "\"'" or description[-1] != description[0]:
            errors.append(f"{path.relative_to(root)}: expected a quoted description")

    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for link in re.findall(r"\]\(([^)]+)\)", text):
            if urlparse(link).scheme or link.startswith("#"):
                continue
            target = (path.parent / unquote(link.split("#")[0])).resolve()
            if not target.is_relative_to(root) or not target.exists():
                errors.append(f"{path.relative_to(root)}: missing/outside link {link}")
            if path.is_relative_to(root / "skills") and not target.is_relative_to(root / "skills"):
                errors.append(f"{path.relative_to(root)}: runtime link escapes skills bundle: {link}")
    return errors, len(skills)


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    errors, count = validate(root)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        sys.exit(1)
    print(f"Package OK: {count} skills, matching manifests and local links. Behavioral evaluation is separate.")
