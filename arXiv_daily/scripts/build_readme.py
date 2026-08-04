#!/usr/bin/env python3
"""Build human-readable topic views from the deduplicated paper store."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

import yaml


ARCHIVE_ROOT = Path(__file__).resolve().parents[1]


def _clean(value: str) -> str:
    return " ".join(value.replace("|", "\\|").split())


def _authors(authors: list[str], limit: int = 3) -> str:
    if len(authors) <= limit:
        return ", ".join(authors)
    return f"{', '.join(authors[:limit])}, et al."


def _paper_row(paper: dict[str, Any], topic: str) -> str:
    labels = paper.get("matches", {}).get(topic, [])
    categories = ", ".join(paper.get("categories", [])[:3])
    return (
        f"| {paper['published']} | "
        f"[{_clean(paper['title'])}]({paper['url']}) | "
        f"{_clean(_authors(paper.get('authors', [])))} | "
        f"{_clean(categories)} | "
        f"{_clean(', '.join(labels))} | "
        f"[abs]({paper['url']}) / [pdf]({paper['pdf_url']}) |"
    )


def _topic_papers(papers: list[dict[str, Any]], topic: str) -> list[dict[str, Any]]:
    selected = [paper for paper in papers if topic in paper.get("topics", [])]
    return sorted(selected, key=lambda p: (p["published"], p["arxiv_id"]), reverse=True)


def _topic_markdown(
    topic: str,
    topic_config: dict[str, Any],
    papers: list[dict[str, Any]],
    coverage: str,
) -> str:
    title = topic_config["title"]
    selected = _topic_papers(papers, topic)
    lines = [
        f"# {title} — arXiv Daily",
        "",
        "[← Archive overview](../README.md)",
        "",
        "> Automatically generated high-recall candidate feed. Inclusion here is not an endorsement or promotion to the curated root README.",
        "",
        f"**Coverage:** 2025-01-01 to {coverage} · **Papers:** {len(selected)} · **Unique arXiv IDs:** {len({p['arxiv_id'] for p in selected})}",
        "",
        f"**Scope:** {topic_config['scope']}",
        "",
    ]
    current_month = None
    for paper in selected:
        month = paper["published"][:7]
        if month != current_month:
            if current_month is not None:
                lines.append("")
            lines.extend(
                [
                    f"## {month}",
                    "",
                    "| Date | Paper | Authors | Categories | Matched signals | Links |",
                    "| :--: | :---- | :------ | :--------: | :-------------- | :----: |",
                ]
            )
            current_month = month
        lines.append(_paper_row(paper, topic))
    if not selected:
        lines.append("No matching papers yet.")
    lines.append("")
    return "\n".join(lines)


def build_archive(config_path: Path, data_path: Path, archive_root: Path = ARCHIVE_ROOT) -> None:
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    payload = json.loads(data_path.read_text(encoding="utf-8"))
    papers = list(payload.get("papers", {}).values())
    coverage = payload.get("coverage_end", config["archive"]["start_date"])

    for topic, topic_config in config["topics"].items():
        output = archive_root / topic_config["file"]
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            _topic_markdown(topic, topic_config, papers, coverage), encoding="utf-8"
        )

    counts = Counter()
    for paper in papers:
        counts.update(paper.get("topics", []))

    lines = [
        "# Awesome-Embodied-3DV — arXiv Daily",
        "",
        "> A high-recall candidate archive for manual curation into [Awesome-Embodied-3DV](../README.md). It is intentionally broader than the curated list.",
        "",
        f"**Coverage:** {payload.get('coverage_start', config['archive']['start_date'])} to {coverage} · **Unique papers:** {len(papers)}",
        "",
        "## Sections",
        "",
        "| Section | Papers | Scope |",
        "| :------ | -----: | :---- |",
    ]
    for topic, topic_config in config["topics"].items():
        lines.append(
            f"| [{topic_config['title']}]({topic_config['file']}) | {counts[topic]} | {topic_config['scope']} |"
        )
    lines.extend(
        [
            "",
            "A paper is stored once in [`data/papers.json`](data/papers.json) but may appear in multiple generated views. The archive uses arXiv `v1` dates and is updated twice daily by GitHub Actions. Promotion to the root README is always manual.",
            "",
            "## Latest candidates",
            "",
        ]
    )
    for topic, topic_config in config["topics"].items():
        selected = _topic_papers(papers, topic)[:10]
        lines.extend([f"### {topic_config['title']}", ""])
        for paper in selected:
            lines.append(
                f"- {paper['published']} — [{_clean(paper['title'])}]({paper['url']})"
            )
        if not selected:
            lines.append("- No matching papers yet.")
        lines.append("")

    lines.extend(
        [
            "## Method",
            "",
            "The fetcher combines depth/sensing, 3D/4D representation, reconstruction, generation, embodied-world-model, and infrastructure queries. Local regex rules assign one or more topic tags; arXiv ID is the deduplication key.",
            "",
            "## Manual maintenance",
            "",
            "```bash",
            "python -m pip install -r arXiv_daily/requirements.txt",
            "python arXiv_daily/scripts/fetch_arxiv.py",
            "python arXiv_daily/scripts/validate_archive.py",
            "```",
            "",
            "Edit [`config.yaml`](config.yaml) to expand queries or classification signals. The scheduled job uses a 14-day lookback to catch delayed indexing.",
            "",
            "Inspired by [robotics_arXiv_daily](https://github.com/jiangranlv/robotics_arXiv_daily).",
            "",
        ]
    )
    (archive_root / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=ARCHIVE_ROOT / "config.yaml")
    parser.add_argument("--data", type=Path, default=ARCHIVE_ROOT / "data/papers.json")
    args = parser.parse_args()
    build_archive(args.config, args.data)


if __name__ == "__main__":
    main()
