#!/usr/bin/env python3
"""Build the structured L0-L4 corpus and reproducible survey summaries.

README.md is the canonical source for paper identity, taxonomy placement,
modality, mechanism, date, and official links. Boolean mechanism tags are
derived from those reviewed annotations using the documented rules below.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path


LEVEL_RE = re.compile(r"^## L([0-4]):")
LINK_RE = re.compile(r"\[([^]]+)\]\(([^)]+)\)")
GITHUB_RE = re.compile(r"\[GitHub(?: \(announced\))?\]\((https://github\.com/[^)]+)\)")
WEBSITE_RE = re.compile(r"\[(?:Website|Dataset|Code)\]\(([^)]+)\)")

MODALITIES = ["Image", "Editing", "Video", "Slide", "UI", "3D", "World"]
MECHANISMS = ["planning", "retrieval", "tool_use", "multi_agent", "verification", "memory", "rl"]


def has_any(text: str, terms: tuple[str, ...]) -> bool:
    return any(term in text for term in terms)


def annotate(row: dict[str, str]) -> dict[str, object]:
    text = f"{row['paper']} {row['primary_mechanism']}".lower()
    path = row["capability_path"]
    level = row["primary_level"]
    tags = {
        "planning": has_any(
            text,
            (
                "plan", "prompt", "condition", "layout", "story", "script",
                "scene graph", "world script", "trajectory", "reasoning",
                "specification", "grounding", "reference",
            ),
        ),
        "retrieval": has_any(text, ("retriev", "search", "rag", "knowledge", "grounded")),
        "tool_use": "L2" in path or has_any(
            text, ("tool", "workflow", "program", "code-driven", "orchestration", "routing", "dispatch"),
        ),
        "multi_agent": has_any(
            text, ("multi-agent", "multi agent", "collaborative", "collaboration", "multi-role", "role orchestration"),
        ),
        "verification": "L3" in path or has_any(
            text, ("verif", "critic", "feedback", "review", "reflection", "repair", "correct", "render", "rollback"),
        ),
        "memory": level == "L4" or has_any(
            text, ("memory", "experience", "skill", "capability profile", "self-evolv", "evolving", "persistent"),
        ),
        "rl": has_any(
            text, ("reinforcement", " rl", "rl ", "grpo", "policy optim", "preference optimization"),
        ),
    }
    return tags


def normalized_fields(row: dict[str, object], tags: dict[str, object]) -> dict[str, str]:
    """Derive conservative normalized descriptors from reviewed catalog fields."""
    text = f"{row['paper']} {row['primary_mechanism']}".lower()
    modalities = list(row["modalities"])
    if bool(tags["multi_agent"]):
        controller_type = "multi-role language or multimodal controller"
    elif has_any(text, ("unified", "native", "interleaved", "latent action", "visual reasoner")):
        controller_type = "unified multimodal policy"
    else:
        controller_type = "language or multimodal controller"

    executor_map = {
        "Image": "image generator",
        "Editing": "visual editor",
        "Video": "video generator or editor",
        "Slide": "slide renderer or object model",
        "UI": "code generator and browser renderer",
        "3D": "3D generator or scene engine",
        "World": "world generator or simulator",
    }
    visual_executor = "; ".join(executor_map[item] for item in modalities)

    level = str(row["primary_level"])
    feedback = {
        "L0": "no deployed controller action demonstrated",
        "L1": "no outcome-conditioned action demonstrated",
        "L2": "execution result does not redirect the open-loop route",
        "L3": "current-outcome feedback changes a later action",
        "L4": "completed experience changes future-task control",
    }[level]
    evaluation_type = {
        "L0": "component, data-pipeline, or terminal-artifact evaluation",
        "L1": "condition and terminal-artifact evaluation",
        "L2": "operation and terminal-artifact evaluation",
        "L3": "trajectory, repair, and terminal-artifact evaluation",
        "L4": "chronological transfer and terminal-artifact evaluation",
    }[level]
    return {
        "controller_type": controller_type,
        "visual_executor": visual_executor,
        "feedback": feedback,
        "evaluation_type": evaluation_type,
    }


def parse_readme(path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    level: str | None = None
    subsection = ""
    for line in path.read_text(encoding="utf-8").splitlines():
        match = LEVEL_RE.match(line)
        if match:
            level = f"L{match.group(1)}"
            subsection = ""
            continue
        if line.startswith("## Evaluation"):
            level = None
        if line.startswith("### "):
            subsection = line[4:].strip()
            continue
        if not level or not line.startswith("| ["):
            continue

        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 7:
            continue
        paper_match = LINK_RE.match(cells[0])
        if not paper_match:
            continue
        github_match = GITHUB_RE.search(cells[1])
        website_match = WEBSITE_RE.search(cells[2])
        date = cells[6]
        year, month = (int(part) for part in date.split("-"))
        modalities = [item.strip() for item in cells[4].split(",")]
        row: dict[str, object] = {
            "paper": paper_match.group(1),
            "paper_url": paper_match.group(2),
            "date": date,
            "year": year,
            "half_year": f"{year}-H{1 if month <= 6 else 2}",
            "primary_level": level,
            "capability_path": cells[3],
            "modalities": modalities,
            "catalog_subsection": subsection,
            "primary_mechanism": cells[5],
            "closed_loop": "L3" in cells[3],
            "cross_task_persistence": level == "L4",
            "github": github_match.group(1) if github_match else "",
            "website": website_match.group(1) if website_match else "",
            "open_source": bool(github_match),
        }
        tags = annotate(row)
        row.update(tags)
        row.update(normalized_fields(row, tags))
        rows.append(row)

    names = [str(row["paper"]) for row in rows]
    duplicates = sorted(name for name, count in Counter(names).items() if count > 1)
    if duplicates:
        raise ValueError(f"Duplicate L0-L4 records: {duplicates}")
    return rows


def build_summary(rows: list[dict[str, object]]) -> dict[str, object]:
    levels = ["L0", "L1", "L2", "L3", "L4"]
    periods = sorted({str(row["half_year"]) for row in rows})
    by_period = {
        period: {
            level: sum(row["half_year"] == period and row["primary_level"] == level for row in rows)
            for level in levels
        }
        for period in periods
    }
    by_modality = {
        modality: {
            level: sum(modality in row["modalities"] and row["primary_level"] == level for row in rows)
            for level in levels
        }
        for modality in MODALITIES
    }
    by_mechanism = {
        mechanism: {
            level: sum(bool(row[mechanism]) and row["primary_level"] == level for row in rows)
            for level in levels
        }
        for mechanism in MECHANISMS
    }
    return {
        "record_count": len(rows),
        "level_counts": {level: sum(row["primary_level"] == level for row in rows) for level in levels},
        "half_year_by_level": by_period,
        "modality_by_level": by_modality,
        "mechanism_by_level": by_mechanism,
        "notes": {
            "modality_counts": "Multi-label counts; one system can contribute to several modality rows.",
            "mechanism_counts": "Boolean tags derived from reviewed README taxonomy paths, section placement, titles, and primary-mechanism annotations.",
            "scope": "Unique reviewed records assigned to L0-L4; stand-alone evaluation resources and additional background components are excluded.",
        },
    }


def write_csv(rows: list[dict[str, object]], path: Path) -> None:
    fields = [
        "paper", "paper_url", "date", "year", "half_year", "primary_level",
        "capability_path", "modalities", "catalog_subsection", "primary_mechanism",
        "controller_type", "visual_executor", "feedback", "evaluation_type",
        *MECHANISMS, "closed_loop", "cross_task_persistence", "github", "website", "open_source",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            output = dict(row)
            output["modalities"] = ";".join(row["modalities"])
            writer.writerow({field: output[field] for field in fields})


def write_json(value: object, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--readme", type=Path, default=Path("README.md"))
    parser.add_argument("--output-dir", type=Path, default=Path("data"))
    args = parser.parse_args()

    rows = parse_readme(args.readme)
    summary = build_summary(rows)
    write_csv(rows, args.output_dir / "agentic_visual_generation_corpus.csv")
    write_json(rows, args.output_dir / "agentic_visual_generation_corpus.json")
    write_json(summary, args.output_dir / "landscape_summary.json")
    print(json.dumps({"records": len(rows), "levels": summary["level_counts"]}))


if __name__ == "__main__":
    main()
