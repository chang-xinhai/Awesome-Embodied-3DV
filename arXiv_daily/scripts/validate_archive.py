#!/usr/bin/env python3
"""Validate archive invariants and generated topic views."""

from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

import yaml


ARCHIVE_ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    config = yaml.safe_load((ARCHIVE_ROOT / "config.yaml").read_text(encoding="utf-8"))
    payload = json.loads(
        (ARCHIVE_ROOT / "data/papers.json").read_text(encoding="utf-8")
    )
    papers = payload["papers"]
    topics = set(config["topics"])
    start = date.fromisoformat(config["archive"]["start_date"])
    end = date.fromisoformat(payload["coverage_end"])

    assert payload["paper_count"] == len(papers), "paper_count does not match store"
    assert papers, "archive is empty"
    assert start <= end, "invalid coverage interval"

    expected_by_topic: dict[str, set[str]] = {topic: set() for topic in topics}
    for paper_id, paper in papers.items():
        assert paper_id == paper["arxiv_id"], f"ID mismatch: {paper_id}"
        assert re.fullmatch(r"\d{4}\.\d{4,5}", paper_id), f"invalid arXiv ID: {paper_id}"
        published = date.fromisoformat(paper["published"])
        assert start <= published <= end, f"date outside coverage: {paper_id}"
        assert paper["url"] == f"https://arxiv.org/abs/{paper_id}"
        assert paper["pdf_url"] == f"https://arxiv.org/pdf/{paper_id}"
        paper_topics = set(paper["topics"])
        assert paper_topics and paper_topics <= topics, f"invalid topics: {paper_id}"
        assert paper_topics == set(paper["matches"]), f"match/topic mismatch: {paper_id}"
        for topic in paper_topics:
            expected_by_topic[topic].add(paper_id)

    for required_id, required_topics in config.get("validation", {}).get(
        "required_topics", {}
    ).items():
        assert required_id in papers, f"required paper missing: {required_id}"
        assert set(required_topics) <= set(papers[required_id]["topics"]), (
            f"required paper misclassified: {required_id}"
        )

    for topic, topic_config in config["topics"].items():
        markdown = (ARCHIVE_ROOT / topic_config["file"]).read_text(encoding="utf-8")
        ids = re.findall(r"https://arxiv\.org/abs/(\d{4}\.\d{4,5})", markdown)
        # Every row repeats the abs URL in the title and Links column.
        counts = {paper_id: ids.count(paper_id) for paper_id in set(ids)}
        assert all(count == 2 for count in counts.values()), f"duplicate/malformed rows in {topic}"
        assert set(ids) == expected_by_topic[topic], f"generated view mismatch: {topic}"
        dates = re.findall(r"^\| (\d{4}-\d{2}-\d{2}) \|", markdown, flags=re.MULTILINE)
        assert dates == sorted(dates, reverse=True), f"date order mismatch: {topic}"

    print(
        f"validated {len(papers)} unique papers across "
        + ", ".join(
            f"{config['topics'][topic]['title']}={len(expected_by_topic[topic])}"
            for topic in config["topics"]
        )
    )


if __name__ == "__main__":
    main()
