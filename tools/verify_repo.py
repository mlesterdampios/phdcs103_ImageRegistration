"""Check the published teaching repository without installing dependencies.

Run from any directory: python path/to/tools/verify_repo.py
Use --strict-pack to reject Git metadata, environments, caches, browser profiles
and release archives in a folder prepared for distribution. Default verification
skips those local runtime artifacts so it remains useful after Git checkout and
Python setup. Browser profiles are never traversed or read in either mode.
This reads the saved files only. It never runs a research experiment or writes
Python bytecode. The sole output file is docs/repository_validation.json.
"""
from __future__ import annotations

import ast
import argparse
import hashlib
import json
import os
import posixpath
import re
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET
import zipfile


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "docs/repository_validation.json"
NS = {
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def clean_text(text):
    return " ".join(text.split())


def package_target(part, target):
    return target.lstrip("/") if target.startswith("/") else posixpath.normpath(posixpath.join(posixpath.dirname(part), target))


def package_relationships(archive, part):
    folder, filename = posixpath.split(part)
    path = posixpath.join(folder, "_rels", filename + ".rels")
    return {row.attrib["Id"]: row.attrib for row in ET.fromstring(archive.read(path))}


def local_target(document, raw):
    """Resolve a Markdown link without accepting paths outside the repo."""
    value = raw.strip()
    if value.startswith("<"):
        value = value[1:value.index(">")]
    else:
        value = re.split(r'\s+["\']', value, maxsplit=1)[0]
    parsed = urlsplit(value)
    if parsed.scheme or value.startswith(("#", "//")):
        return None
    value = unquote(parsed.path)
    if not value:
        return None
    return (document.parent / value).resolve()


def repository_files(strict_pack):
    """Prune runtime/private directories before reading any file contents."""
    forbidden = {".git", ".build", ".venv", "venv", "__pycache__", ".ipynb_checkpoints",
                 ".pytest_cache", ".mypy_cache", ".ruff_cache", "node_modules", "qa",
                 "chrome-profile", "slide_previews", "original_previews", "beginner_previews",
                 "tmp", "temp"}
    archive_extensions = {".zip", ".7z", ".tar", ".gz", ".rar", ".pyc", ".pyo"}
    files, issues, skipped = [], [], []

    def ignored(path):
        rel = path.relative_to(ROOT)
        return (any(part.lower() in forbidden or part.lower().startswith(("chrome-", "isolated-"))
                    for part in rel.parts) or rel.parts[:2] == ("notebooks", "reruns") or
                path.suffix.lower() in archive_extensions)

    for folder, directories, filenames in os.walk(ROOT):
        parent = Path(folder)
        retained = []
        for name in directories:
            path = parent / name
            if ignored(path) or path.is_symlink():
                rel = path.relative_to(ROOT).as_posix()
                skipped.append(rel)
                if strict_pack:
                    issues.append(rel)
            else:
                retained.append(name)
        directories[:] = retained
        for name in filenames:
            path = parent / name
            if ignored(path) or path.is_symlink():
                rel = path.relative_to(ROOT).as_posix()
                skipped.append(rel)
                if strict_pack:
                    issues.append(rel)
            else:
                files.append(path)
    return sorted(files), sorted(issues), sorted(skipped)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--strict-pack", action="store_true",
                        help="Reject all Git metadata, virtual environments, caches, browser profiles and release archives in a distribution pack; never enter private profile directories.")
    args = parser.parse_args()
    checks, findings = [], []
    files, bad_paths, skipped = repository_files(args.strict_pack)

    def check(name, condition, **details):
        result = {"name": name, "passed": bool(condition), **details}
        checks.append(result)
        if not condition:
            findings.append(result)

    paths = read_json(ROOT / "content/repository_paths.json")
    plan = read_json(ROOT / "content/lesson_plan.json")
    final_content = read_json(ROOT / "content/final_slide_content.json")
    manifest = read_json(ROOT / "content/source_copy_manifest.json")
    slides, steps = plan["slides"], plan["steps"]
    mapping = paths["mapping"]
    check("canonical deck path has an explicit repository mapping",
          mapping.get(plan["deck"]["path"]) == paths["presentation"])
    check("presentation and demo retain their relative relationship",
          (ROOT / "demo" / plan["deck"]["relative_from_demo"]).resolve() == (ROOT / paths["presentation"]).resolve())
    mapping_issues = []
    for source, target in mapping.items():
        if PurePosixPath(source).is_absolute() or PurePosixPath(target).is_absolute() or ".." in PurePosixPath(target).parts:
            mapping_issues.append({"source": source, "target": target, "issue": "non-portable mapping"})
        elif not (ROOT / target).exists():
            mapping_issues.append({"source": source, "target": target, "issue": "missing mapped destination"})
    check("all repository path mappings resolve", not mapping_issues, issues=mapping_issues,
          provenance_boundary="Canonical historical source-deck identifiers are preserved provenance, not runtime dependencies.")

    copy_issues = []
    for entry in manifest["files"]:
        path = ROOT / entry["repository"]
        if not path.is_file():
            copy_issues.append({"path": entry["repository"], "issue": "missing"})
        elif digest(path) != entry["sha256"]:
            copy_issues.append({"path": entry["repository"], "issue": "checksum mismatch"})
    check("copied source files retain their exact published bytes", not copy_issues,
          files_checked=len(manifest["files"]), issues=copy_issues)
    copied = {entry["repository"]: entry["sha256"] for entry in manifest["files"]}
    ppt_path, demo_path = ROOT / paths["presentation"], ROOT / paths["demo"]
    check("latest presentation checksum matches source copy manifest",
          digest(ppt_path) == copied.get(paths["presentation"]), sha256=digest(ppt_path))
    check("latest standalone demo checksum matches source copy manifest",
          digest(demo_path) == copied.get(paths["demo"]), sha256=digest(demo_path))

    title_issues, visibility_issues, note_issues, demo_issues = [], [], [], []
    expected_links = sum(bool(s.get("demo_step")) for s in slides)
    actual_links, visible = 0, 0
    with zipfile.ZipFile(ppt_path) as archive:
        check("PowerPoint archive integrity", archive.testzip() is None)
        presentation_part = "ppt/presentation.xml"
        relationships = package_relationships(archive, presentation_part)
        ids = ET.fromstring(archive.read(presentation_part)).find("p:sldIdLst", NS)
        check("actual PowerPoint slide count matches canonical lesson", len(ids) == len(slides) == 86, slides=len(ids))
        # Use sldIdLst relationships. XML filenames can differ from slide order.
        for number, (identifier, expected) in enumerate(zip(ids, slides), 1):
            relationship_id = identifier.attrib["{" + NS["r"] + "}id"]
            part = package_target(presentation_part, relationships[relationship_id]["Target"])
            slide = ET.fromstring(archive.read(part))
            texts = [t.text or "" for t in slide.findall(".//a:t", NS)]
            title = clean_text(texts[0]) if texts else ""
            if title != clean_text(expected["title"]):
                title_issues.append({"slide": number, "expected": expected["title"], "actual": title})
            hidden = slide.attrib.get("show", "1") == "0"
            visible += not hidden
            if hidden != bool(expected["hidden"]):
                visibility_issues.append(number)
            rels = package_relationships(archive, part)
            notes_rel = next((r for r in rels.values() if r["Type"].endswith("/notesSlide")), None)
            note_text = ""
            if notes_rel:
                note_part = package_target(part, notes_rel["Target"])
                note_text = "\n".join(t.text or "" for t in ET.fromstring(archive.read(note_part)).findall(".//a:t", NS))
            # Final notes remove obsolete source-edition slide boilerplate.
            # Native note masters can also append a separate slide-number field.
            final_notes = final_content[number-1]["final_notes"]
            if (f"Chronological slide {number} of 86." not in note_text or
                    clean_text(final_notes) not in clean_text(note_text)):
                note_issues.append(number)
            links = [r["Target"] for r in rels.values() if r["Type"].endswith("/hyperlink") and "demo/index.html" in r.get("Target", "")]
            actual_links += len(links)
            wanted = ["../demo/index.html#" + expected["demo_step"]] if expected.get("demo_step") else []
            if links != wanted:
                demo_issues.append({"slide": number, "expected": wanted, "actual": links})
            for link in links:
                fragment = urlsplit(link).fragment
                if fragment not in {s["id"] for s in steps}:
                    demo_issues.append({"slide": number, "unknown_step": fragment})
    check("all actual slide titles follow canonical order", not title_issues, issues=title_issues)
    check("44 visible and 42 hidden slides match canonical route", visible == 44 and not visibility_issues, visible=visible, hidden=len(slides)-visible, issues=visibility_issues)
    check("all slides contain their full canonical discussion notes", not note_issues, slides_checked=len(slides), issues=note_issues)
    check("all declared PowerPoint demo targets are correct", not demo_issues and actual_links == expected_links == 71,
          links_checked=actual_links, issues=demo_issues)

    html = demo_path.read_text(encoding="utf-8")
    embedded = re.search(r'<script\s+id="chronologicalBundle"\s+type="application/json">([\s\S]*?)</script>', html)
    bundle = json.loads(embedded.group(1)) if embedded else {}
    bundle_plan = bundle.get("plan", {})
    embedded_steps = bundle_plan.get("steps", [])
    # The builder adds browser-only display labels to each canonical step.
    # It renames a native calculator's mode to native_mode, because mode is
    # also the human-readable evidence label above every browser lesson.
    # All canonical values and order must remain identical after that rename.
    steps_match = len(embedded_steps) == len(steps) and all(
        all(actual.get("native_mode" if key == "mode" and expected.get("native_type") else key) == value
            for key, value in expected.items())
        for expected, actual in zip(steps, embedded_steps))
    check("demo embeds the exact current slide and step sequences",
          bundle_plan.get("slides") == slides and steps_match,
          slides=len(bundle_plan.get("slides", [])), steps=len(bundle_plan.get("steps", [])))
    check("demo embeds the current measurement records",
          bundle.get("measurements") == read_json(ROOT / "content/measurement_lessons.json"))
    check("demo retains three embedded source laboratories and measurement images",
          len(bundle.get("frames", {})) == 3 and bool(bundle.get("measurement_assets")),
          embedded_laboratories=len(bundle.get("frames", {})))

    notebook = read_json(ROOT / paths["notebook"])
    code = [cell for cell in notebook["cells"] if cell["cell_type"] == "code"]
    errors = [cell.get("id", str(i)) for i, cell in enumerate(code) for output in cell.get("outputs", []) if output.get("output_type") == "error"]
    check("notebook has 22 executed code cells and no saved errors",
          len(code) == 22 and all(cell.get("execution_count") is not None for cell in code) and not errors,
          code_cells=len(code), errors=errors)

    broken, link_count = [], 0
    # Inline Markdown links and image links; include reference-style definitions.
    link_pattern = re.compile(r'!?\[[^\]\n]*\]\(([^\n]+?)\)')
    definition_pattern = re.compile(r'^\s*\[[^\]]+\]:\s*(\S+)', re.M)
    for document in (path for path in files if path.suffix.lower() == ".md"):
        content = document.read_text(encoding="utf-8")
        targets = link_pattern.findall(content) + definition_pattern.findall(content)
        for raw in targets:
            try:
                destination = local_target(document, raw)
                if destination is None:
                    continue
                link_count += 1
                contained = destination.is_relative_to(ROOT)
                if not contained or not destination.exists():
                    broken.append({"document": document.relative_to(ROOT).as_posix(), "target": raw,
                                   "issue": "outside repository" if not contained else "missing"})
            except (ValueError, IndexError) as exc:
                broken.append({"document": document.relative_to(ROOT).as_posix(), "target": raw, "issue": type(exc).__name__})
    check("all local Markdown and image links resolve inside the repository", not broken,
          local_links_checked=link_count, issues=broken)

    check("distribution contains no runtime or private artifacts" if args.strict_pack else
          "runtime and private artifacts are excluded from verification", not bad_paths,
          strict_pack=args.strict_pack, issues=bad_paths, skipped_runtime_paths=len(skipped))
    json_issues, json_count, python_issues, python_count = [], 0, [], 0
    for path in files:
        if path.suffix.lower() in {".json", ".ipynb"}:
            json_count += 1
            try:
                read_json(path)
            except (ValueError, UnicodeError) as exc:
                json_issues.append({"path": path.relative_to(ROOT).as_posix(), "issue": str(exc)})
        if path.suffix.lower() == ".py":
            python_count += 1
            try:
                ast.parse(path.read_text(encoding="utf-8"), filename=path.relative_to(ROOT).as_posix())
            except (SyntaxError, UnicodeError) as exc:
                python_issues.append({"path": path.relative_to(ROOT).as_posix(), "issue": str(exc)})
    check("all JSON data and notebook JSON parse", not json_issues, files_checked=json_count, issues=json_issues)
    check("all Python sources compile as syntax trees without bytecode", not python_issues, files_checked=python_count, issues=python_issues)
    largest = max(files, key=lambda p: p.stat().st_size)
    check("every file is below GitHub's 100 MiB regular-file limit", largest.stat().st_size < 100*1024*1024,
          largest_file=largest.relative_to(ROOT).as_posix(), largest_bytes=largest.stat().st_size)

    report = {"status": "passed" if not findings else "failed", "checks": checks,
              "checks_passed": sum(c["passed"] for c in checks), "checks_total": len(checks),
              "findings": findings, "repository_files_scanned": len(files),
              "source_copy_files": len(manifest["files"]), "experiment_pipelines_rerun": False,
              "strict_pack": args.strict_pack,
              "verification_scope": "Portable saved-artifact checks; browser behavior is tested separately with tools/check_demo.cjs.",
              "privacy": "Report uses repository-relative paths only. No source workspace is required."}
    REPORT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "checks_passed": report["checks_passed"],
                      "checks_total": len(checks), "report": "docs/repository_validation.json",
                      "findings": findings}, ensure_ascii=False))
    return 0 if not findings else 1


if __name__ == "__main__":
    sys.exit(main())
