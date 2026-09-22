import unittest
from src.ml_pipeline.core import (
    FeatureScaler,
    ModelEvaluator,
    MLPipelineRunner,
)


class TestFeatureScaler(unittest.TestCase):
    def setUp(self):
        self.scaler = FeatureScaler()

    def test_standard_scale_success(self):
        data = [10.0, 20.0, 30.0, 40.0, 50.0]
        scaled = self.scaler.standard_scale(data)
        self.assertEqual(len(scaled), 5)
        self.assertAlmostEqual(sum(scaled), 0.0, places=2)

    def test_standard_scale_constant_values(self):
        data = [5.0, 5.0, 5.0]
        scaled = self.scaler.standard_scale(data)
        self.assertEqual(scaled, [0.0, 0.0, 0.0])

    def test_standard_scale_empty_list(self):
        self.assertEqual(self.scaler.standard_scale([]), [])

    def test_standard_scale_invalid_type(self):
        with self.assertRaises(TypeError):
            self.scaler.standard_scale("not a list")

    def test_standard_scale_invalid_element(self):
        with self.assertRaises(TypeError):
            self.scaler.standard_scale([1.0, "invalid", 3.0])


class TestModelEvaluator(unittest.TestCase):
    def setUp(self):
        self.evaluator = ModelEvaluator()

    def test_evaluate_binary_classification_success(self):
        y_true = [1, 0, 1, 1, 0, 1, 0, 0]
        y_pred = [1, 0, 1, 0, 0, 1, 0, 1]
        metrics = self.evaluator.evaluate_binary_classification(
            y_true, y_pred
        )

        self.assertEqual(metrics["accuracy"], 0.75)
        self.assertEqual(metrics["precision"], 0.75)
        self.assertEqual(metrics["recall"], 0.75)
        self.assertEqual(metrics["f1_score"], 0.75)
        self.assertEqual(metrics["total_samples"], 8)

    def test_evaluate_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            self.evaluator.evaluate_binary_classification([1, 0], [1])

    def test_evaluate_empty_dataset(self):
        with self.assertRaises(ValueError):
            self.evaluator.evaluate_binary_classification([], [])

    def test_evaluate_invalid_label_values(self):
        with self.assertRaises(ValueError):
            self.evaluator.evaluate_binary_classification([1, 2], [1, 0])


class TestMLPipelineIntegration(unittest.TestCase):
    def setUp(self):
        self.pipeline = MLPipelineRunner()

    def test_pipeline_end_to_end_success(self):
        features = [10.0, 20.0, 30.0, 40.0]
        y_true = [1, 0, 1, 0]
        y_pred = [1, 0, 1, 0]

        result = self.pipeline.run_pipeline(features, y_true, y_pred)

        self.assertEqual(result["status"], "SUCCESS")
        self.assertEqual(result["model_metrics"]["accuracy"], 1.0)
        self.assertEqual(len(result["scaled_features"]), 4)


if __name__ == "__main__":
    unittest.main()
