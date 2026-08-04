import sys
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from fetch_arxiv import classify_paper  # noqa: E402


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


if __name__ == "__main__":
    unittest.main()
