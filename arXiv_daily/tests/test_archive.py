import sys
import unittest
from datetime import date
from pathlib import Path
from unittest import mock

import yaml


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import fetch_arxiv  # noqa: E402
from fetch_arxiv import classify_paper, fetch  # noqa: E402


class ClassifierTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = yaml.safe_load((ROOT / "config.yaml").read_text())

    def classify(self, title, abstract):
        return classify_paper({"title": title, "abstract": abstract, "comment": None}, self.config)[0]

    def test_seeclear_is_data_perception_candidate(self):
        topics = self.classify(
            "SeeClear: Reliable Transparent Object Depth Estimation via Generative Opacification",
            "We turn transparent object regions into geometric opaque images to improve monocular depth estimation.",
        )
        self.assertIn("data_perception", topics)

    def test_gaussian_representation_candidate(self):
        topics = self.classify(
            "Dynamic Gaussian Splatting for 4D Scene Representation",
            "We use deformation fields and Gaussian splatting to represent dynamic scenes.",
        )
        self.assertIn("representation", topics)

    def test_embodied_scene_graph_candidate(self):
        topics = self.classify(
            "A Persistent 3D Scene Graph for Embodied Agents",
            "Our world model provides 3D grounding and persistent scene memory for robot interaction.",
        )
        self.assertIn("embodiment_world_models", topics)

    def test_3d_dataset_candidate(self):
        topics = self.classify(
            "A Large-Scale 3D Reconstruction Benchmark",
            "We release a 3D dataset and metric suite for scene reconstruction evaluation.",
        )
        self.assertIn("datasets_infrastructure", topics)

    def test_non_3d_medical_paper_is_rejected(self):
        topics = self.classify(
            "Clinical Risk Prediction from Medical Records",
            "A hospital benchmark for risk classification and patient outcome evaluation.",
        )
        self.assertEqual([], topics)

    def test_quantum_world_model_is_rejected(self):
        topics = self.classify(
            "A Decision-Useful World Model for Quantum Architecture Search",
            "We use a world model to optimize VQE circuits for quantum systems.",
        )
        self.assertNotIn("embodiment_world_models", topics)


class FetchTest(unittest.TestCase):
    def test_transient_api_failure_does_not_abort_later_queries(self):
        config = {
            "archive": {
                "page_size": 100,
                "delay_seconds": 10,
                "num_retries": 10,
                "max_results_per_window": 100,
            },
            "queries": [
                {"name": "rate-limited", "query": "cat:cs.RO"},
                {"name": "healthy", "query": "cat:cs.CV"},
            ],
        }
        client = mock.Mock()
        client.results.side_effect = [
            fetch_arxiv.arxiv.HTTPError("https://export.arxiv.org", 10, 429),
            iter(()),
        ]

        with mock.patch("fetch_arxiv.arxiv.Client", return_value=client):
            failures = fetch(
                config,
                date(2026, 8, 1),
                date(2026, 8, 5),
                {"papers": {}},
            )

        self.assertEqual(["rate-limited (2026-08-01..2026-08-05)"], failures)
        self.assertEqual(2, client.results.call_count)


if __name__ == "__main__":
    unittest.main()
