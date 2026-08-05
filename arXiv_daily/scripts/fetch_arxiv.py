#!/usr/bin/env python3
"""Fetch, classify, deduplicate, and render the arXiv candidate archive."""

from __future__ import annotations

import argparse
import calendar
import json
import logging
import re
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterator

import arxiv
import requests
import yaml

from build_readme import build_archive


ARCHIVE_ROOT = Path(__file__).resolve().parents[1]
LOG = logging.getLogger("arxiv_daily")


def _month_windows(start: date, end: date) -> Iterator[tuple[date, date]]:
    cursor = start.replace(day=1)
    while cursor <= end:
        last = calendar.monthrange(cursor.year, cursor.month)[1]
        window_start = max(start, cursor)
        window_end = min(end, cursor.replace(day=last))
        yield window_start, window_end
        cursor = (cursor.replace(day=last) + timedelta(days=1)).replace(day=1)


def _versionless_id(short_id: str) -> str:
    return re.sub(r"v\d+$", "", short_id)


def _normalize(value: str | None) -> str | None:
    if value is None:
        return None
    return " ".join(value.split())


def classify_paper(paper: dict[str, Any], config: dict[str, Any]) -> tuple[list[str], dict[str, list[str]]]:
    text = " ".join(
        [paper.get("title", ""), paper.get("abstract", ""), paper.get("comment") or ""]
    ).lower()
    topics: list[str] = []
    matches: dict[str, list[str]] = {}
    for topic, topic_config in config["topics"].items():
        required = topic_config.get("require_any", [])
        excluded = topic_config.get("exclude", [])
        if required and not any(
            re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL)
            for pattern in required
        ):
            continue
        if any(
            re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL)
            for pattern in excluded
        ):
            continue
        labels = [
            rule["label"]
            for rule in topic_config["patterns"]
            if re.search(rule["regex"], text, flags=re.IGNORECASE | re.DOTALL)
        ]
        if labels:
            topics.append(topic)
            matches[topic] = labels
    return topics, matches


def _paper_from_result(result: arxiv.Result, query_name: str) -> dict[str, Any]:
    paper_id = _versionless_id(result.get_short_id())
    return {
        "arxiv_id": paper_id,
        "title": _normalize(result.title),
        "abstract": _normalize(result.summary),
        "authors": [str(author) for author in result.authors],
        "published": result.published.date().isoformat(),
        "updated": result.updated.date().isoformat(),
        "primary_category": result.primary_category,
        "categories": list(result.categories),
        "comment": _normalize(result.comment),
        "journal_ref": _normalize(result.journal_ref),
        "doi": result.doi,
        "url": f"https://arxiv.org/abs/{paper_id}",
        "pdf_url": f"https://arxiv.org/pdf/{paper_id}",
        "query_sources": [query_name],
    }


def _merge_paper(existing: dict[str, Any] | None, incoming: dict[str, Any]) -> dict[str, Any]:
    if not existing:
        return incoming
    merged = dict(existing)
    merged.update({key: value for key, value in incoming.items() if key != "query_sources"})
    merged["query_sources"] = sorted(
        set(existing.get("query_sources", [])) | set(incoming.get("query_sources", []))
    )
    return merged


def _load_store(path: Path, reset: bool) -> dict[str, Any]:
    if reset or not path.exists():
        return {"schema_version": 1, "papers": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def fetch(
    config: dict[str, Any], start: date, end: date, store: dict[str, Any]
) -> list[str]:
    settings = config["archive"]
    client = arxiv.Client(
        page_size=int(settings["page_size"]),
        delay_seconds=float(settings["delay_seconds"]),
        num_retries=int(settings["num_retries"]),
    )
    papers = store.setdefault("papers", {})
    failures: list[str] = []
    for window_start, window_end in _month_windows(start, end):
        date_filter = (
            f"submittedDate:[{window_start:%Y%m%d}0000 TO {window_end:%Y%m%d}2359]"
        )
        for query in config["queries"]:
            full_query = f"({query['query']}) AND {date_filter}"
            LOG.info("query=%s window=%s..%s", query["name"], window_start, window_end)
            search = arxiv.Search(
                query=full_query,
                max_results=int(settings["max_results_per_window"]),
                sort_by=arxiv.SortCriterion.SubmittedDate,
                sort_order=arxiv.SortOrder.Descending,
            )
            count = 0
            try:
                for result in client.results(search):
                    incoming = _paper_from_result(result, query["name"])
                    paper_id = incoming["arxiv_id"]
                    papers[paper_id] = _merge_paper(papers.get(paper_id), incoming)
                    count += 1
            except (
                arxiv.HTTPError,
                arxiv.UnexpectedEmptyPageError,
                requests.exceptions.RequestException,
            ) as exc:
                failure = f"{query['name']} ({window_start}..{window_end})"
                failures.append(failure)
                LOG.warning(
                    "skipping query=%s window=%s..%s after arXiv API retries: %s",
                    query["name"],
                    window_start,
                    window_end,
                    exc,
                )
                continue
            LOG.info("query=%s results=%d", query["name"], count)
    return failures


def reclassify(config: dict[str, Any], store: dict[str, Any]) -> None:
    kept: dict[str, dict[str, Any]] = {}
    for paper_id, paper in store.get("papers", {}).items():
        topics, matches = classify_paper(paper, config)
        if not topics:
            continue
        paper["topics"] = topics
        paper["matches"] = matches
        kept[paper_id] = paper
    store["papers"] = dict(
        sorted(
            kept.items(),
            key=lambda item: (item[1]["published"], item[0]),
            reverse=True,
        )
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=ARCHIVE_ROOT / "config.yaml")
    parser.add_argument("--data", type=Path, default=ARCHIVE_ROOT / "data/papers.json")
    parser.add_argument("--start-date", type=date.fromisoformat)
    parser.add_argument("--end-date", type=date.fromisoformat)
    parser.add_argument("--reset", action="store_true")
    parser.add_argument("--rebuild-only", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    config = yaml.safe_load(args.config.read_text(encoding="utf-8"))
    data_path = args.data.resolve()
    store = _load_store(data_path, args.reset)

    today = datetime.now(timezone.utc).date()
    archive_start = date.fromisoformat(config["archive"]["start_date"])
    end = args.end_date or today
    start = args.start_date or max(
        archive_start, end - timedelta(days=int(config["archive"]["lookback_days"]))
    )
    if start > end:
        parser.error("start date must not be after end date")

    if not args.rebuild_only:
        failures = fetch(config, start, end, store)
        if failures:
            LOG.warning(
                "archive rebuilt from available results; skipped %d transiently failing queries: %s",
                len(failures),
                ", ".join(failures),
            )
    reclassify(config, store)
    store["schema_version"] = 1
    store["coverage_start"] = config["archive"]["start_date"]
    previous_end = store.get("coverage_end", config["archive"]["start_date"])
    store["coverage_end"] = max(previous_end, end.isoformat())
    store["paper_count"] = len(store["papers"])
    store["generated_at"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    data_path.parent.mkdir(parents=True, exist_ok=True)
    data_path.write_text(
        json.dumps(store, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    build_archive(args.config.resolve(), data_path, ARCHIVE_ROOT)
    LOG.info("stored %d unique matching papers", len(store["papers"]))


if __name__ == "__main__":
    main()
