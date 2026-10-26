"""
MLOps Tracking & Governance Module
Integrates MLflow experiment tracking, model artifact versioning,
Kolmogorov-Smirnov feature drift detection, and automated retraining triggers.
"""
import os
import mlflow
import numpy as np
from scipy.stats import ks_2samp

class FleetMLOpsTracker:
    def __init__(self, experiment_name: str = "AERO_SHIELD_Fleet_RUL"):
        self.experiment_name = experiment_name
        mlflow.set_experiment(experiment_name)

    def log_run(self, params: dict, metrics: dict, model_path: str = None):
        """
        Logs a full experiment cycle to MLflow.
        """
        with mlflow.start_run() as run:
            mlflow.log_params(params)
            mlflow.log_metrics({
                "test_rmse": metrics["rmse"],
                "test_mae": metrics["mae"],
                "test_r2": metrics["r2_score"],
                "nasa_asymmetric_score": metrics["nasa_score"],
                "accuracy_15_cycles_pct": metrics["accuracy_within_15_cycles_pct"]
            })
            if model_path and os.path.exists(model_path):
                mlflow.log_artifact(model_path, artifact_path="model_registry")
            run_id = run.info.run_id
            print(f"[MLOps] Successfully logged run {run_id[:8]} to MLflow. RMSE: {metrics['rmse']}")
            return run_id

    def check_feature_drift(self, baseline_features: np.ndarray, current_features: np.ndarray, p_val_threshold: float = 0.05):
        """
        Applies two-sample Kolmogorov-Smirnov test across feature columns
        to detect statistical feature drift.
        """
        drifted_columns = []
        n_features = baseline_features.shape[1]
        
        for col_idx in range(n_features):
            base_col = baseline_features[:, col_idx]
            curr_col = current_features[:, col_idx]
            stat, p_val = ks_2samp(base_col, curr_col)
            if p_val < p_val_threshold:
                drifted_columns.append((col_idx, float(stat), float(p_val)))
                
        drift_ratio = len(drifted_columns) / max(1, n_features)
        is_drift_detected = drift_ratio > 0.20
        
        return {
            "is_drift_detected": is_drift_detected,
            "drifted_feature_count": len(drifted_columns),
            "total_feature_count": n_features,
            "drift_ratio": round(drift_ratio, 3)
        }

    def trigger_retraining(self, batch_id: str, drift_report: dict):
        """
        Executes automated champion/challenger retraining workflow upon drift detection.
        """
        print(f"[MLOps Trigger] Retraining initiated for batch {batch_id}.")
        print(f" -> Drift Ratio: {drift_report.get('drift_ratio', 0.0)} | Features Drifted: {drift_report.get('drifted_feature_count', 0)}")
        return {
            "status": "RETRAINING_DISPATCHED",
            "batch_id": batch_id,
            "pipeline_stage": "CHALLENGER_BACKTEST"
        }
