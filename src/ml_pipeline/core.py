import math
from typing import List, Dict, Union


class FeatureScaler:
    """Standardizes numerical feature datasets for ML model ingestion."""

    def standard_scale(self, data: List[float]) -> List[float]:
        """Scales numerical features to zero mean and unit variance."""
        if not isinstance(data, list):
            raise TypeError("Input feature data must be a list of numbers.")
        if not data:
            return []

        for item in data:
            if not isinstance(item, (int, float)) or isinstance(item, bool):
                raise TypeError(
                    f"All dataset values must be int or float, "
                    f"got {type(item).__name__}."
                )

        n = len(data)
        mean = sum(data) / n
        variance = sum((x - mean) ** 2 for x in data) / n
        std = math.sqrt(variance)

        if std == 0:
            return [0.0 for _ in data]

        return [round((x - mean) / std, 4) for x in data]


class ModelEvaluator:
    """Computes binary classification metrics for model validation."""

    def evaluate_binary_classification(
        self, y_true: List[int], y_pred: List[int]
    ) -> Dict[str, float]:
        """Calculates accuracy, precision, recall, and F1-score."""
        if not isinstance(y_true, list) or not isinstance(y_pred, list):
            raise TypeError("y_true and y_pred must both be Python lists.")

        if len(y_true) != len(y_pred):
            raise ValueError(
                "y_true and y_pred must contain equal number of labels."
            )

        if not y_true:
            raise ValueError("Dataset cannot be empty.")

        tp = fp = tn = fn = 0
        for yt, yp in zip(y_true, y_pred):
            is_invalid_yt = yt not in (0, 1) or isinstance(yt, bool)
            is_invalid_yp = yp not in (0, 1) or isinstance(yp, bool)
            if is_invalid_yt or is_invalid_yp:
                raise ValueError(
                    "Binary classification labels must be 0 or 1."
                )

            if yt == 1 and yp == 1:
                tp += 1
            elif yt == 0 and yp == 1:
                fp += 1
            elif yt == 0 and yp == 0:
                tn += 1
            elif yt == 1 and yp == 0:
                fn += 1

        total = len(y_true)
        accuracy = round((tp + tn) / total, 4)
        precision = round(tp / (tp + fp), 4) if (tp + fp) > 0 else 0.0
        recall = round(tp / (tp + fn), 4) if (tp + fn) > 0 else 0.0
        f1_score = (
            round(2 * (precision * recall) / (precision + recall), 4)
            if (precision + recall) > 0
            else 0.0
        )

        return {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1_score": f1_score,
            "total_samples": total,
        }


class MLPipelineRunner:
    """Combines feature processing and evaluation into a pipeline."""

    def __init__(self):
        self.scaler = FeatureScaler()
        self.evaluator = ModelEvaluator()

    def run_pipeline(
        self,
        raw_features: List[float],
        y_true: List[int],
        y_pred: List[int],
    ) -> Dict[str, Union[List[float], Dict[str, float]]]:
        """Executes full preprocessing and evaluation workflow."""
        scaled_features = self.scaler.standard_scale(raw_features)
        metrics = self.evaluator.evaluate_binary_classification(
            y_true=y_true,
            y_pred=y_pred,
        )

        return {
            "scaled_features": scaled_features,
            "model_metrics": metrics,
            "status": "SUCCESS",
        }
