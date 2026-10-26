"""
Comprehensive Test Suite for AERO-SHIELD Fleet Pipeline
Validates data ingestion, feature engineering, model training,
MLOps logging, triage agent FSM, and work-order generation.
"""
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import pytest
import numpy as np
import pandas as pd

from src.data_loader import load_cmapss_data, INVARIANT_SENSORS, ACTIVE_SENSORS
from src.feature_engineering import compute_rolling_features, extract_last_cycle_features
from src.model_engine import RULPredictor, compute_nasa_asymmetric_score
from src.mlops_tracker import FleetMLOpsTracker
from src.triage_agent import FleetTriageAgent
DATA_DIR = os.path.join(BASE_DIR, "data", "raw")

def test_data_loader_structure():
    """Verify data loader prunes invariant sensors and loads valid train/test sets."""
    train_df, test_df, rul_df = load_cmapss_data(DATA_DIR, subset="FD001")
    
    assert len(train_df) > 0, "Train dataset should not be empty"
    assert len(test_df) > 0, "Test dataset should not be empty"
    assert len(rul_df) == 100, "FD001 test benchmark must contain exactly 100 true RUL labels"
    
    # Verify invariant sensors were pruned
    for inv_s in INVARIANT_SENSORS:
        assert inv_s not in train_df.columns, f"{inv_s} should have been pruned"
        assert inv_s not in test_df.columns, f"{inv_s} should have been pruned"
        
    for act_s in ACTIVE_SENSORS:
        assert act_s in train_df.columns, f"Active sensor {act_s} must be present"

def test_feature_engineering_rolling_isolation():
    """Verify rolling calculations do not leak across distinct engine units."""
    sample_data = pd.DataFrame({
        "unit_number": [1, 1, 1, 2, 2],
        "time_cycle": [1, 2, 3, 1, 2],
        "sensor_2": [640.0, 642.0, 644.0, 650.0, 652.0]
    })
    
    feat_df = compute_rolling_features(sample_data, sensor_cols=["sensor_2"], window=2, max_rul=125)
    
    assert "sensor_2_roll_mean" in feat_df.columns
    assert "sensor_2_roll_std" in feat_df.columns
    assert "target_rul" in feat_df.columns
    
    # Engine 2 at cycle 1 must have roll_mean == 650.0 (not influenced by Engine 1's 644.0)
    eng2_c1_mean = feat_df[(feat_df["unit_number"] == 2) & (feat_df["time_cycle"] == 1)]["sensor_2_roll_mean"].values[0]
    assert eng2_c1_mean == pytest.approx(650.0, rel=1e-3)

def test_nasa_asymmetric_scoring_penalties():
    """Verify NASA loss penalizes late predictions exponentially harder than early warnings."""
    # At d = +/- 10
    y_true = np.array([50.0])
    score_early_10 = compute_nasa_asymmetric_score(y_true, np.array([40.0]))  # d = -10
    score_late_10  = compute_nasa_asymmetric_score(y_true, np.array([60.0]))  # d = +10
    assert score_late_10 > score_early_10, "Late failure must always be penalized heavier than early warning"

    # Exponential growth at d = +/- 25
    score_early_25 = compute_nasa_asymmetric_score(y_true, np.array([25.0]))  # d = -25
    score_late_25  = compute_nasa_asymmetric_score(y_true, np.array([75.0]))  # d = +25
    assert score_late_25 > score_early_25 * 1.8, f"At d=25, late score ({score_late_25}) must exhibit exponential penalty over early ({score_early_25})"

def test_triage_agent_fsm_transitions():
    """Verify deterministic Non-LLM Triage Agent FSM state classifications."""
    agent = FleetTriageAgent(critical_threshold=15.0, warning_threshold=35.0)
    
    # Case 1: Healthy
    res_healthy = agent.evaluate_unit(unit_id=1, current_cycle=100, predicted_rul=55.0)
    assert res_healthy["state"] == "HEALTHY"
    assert res_healthy["requires_work_order"] is False
    assert res_healthy["projected_extension_cycles"] == 0
    
    # Case 2: Warning (Tier 1 Soft In-Situ Derating)
    res_warn = agent.evaluate_unit(unit_id=2, current_cycle=140, predicted_rul=24.5)
    assert res_warn["state"] == "WARNING"
    assert res_warn["requires_work_order"] is True
    assert res_warn["projected_extension_cycles"] == 25
    assert "APPLY_OPERATIONAL_DERATE" in res_warn["tier1_command"]
    assert res_warn["work_order"]["severity_level"] == "WARNING"
    
    # Case 3: Critical (Tier 2 Prescriptive Dispatch)
    res_crit = agent.evaluate_unit(unit_id=3, current_cycle=190, predicted_rul=9.2)
    assert res_crit["state"] == "CRITICAL"
    assert res_crit["requires_work_order"] is True
    assert res_crit["work_order"]["urgency_rank"] == 1
    assert "BORESCOPE_INSPECT_AND_OVERHAUL_HPC" in res_crit["work_order"]["tier_2_prescriptive_maintenance"]["action_code"]

def test_mlops_drift_detection():
    """Verify Kolmogorov-Smirnov drift detection accurately detects distribution shifts."""
    tracker = FleetMLOpsTracker()
    
    np.random.seed(42)
    baseline = np.random.normal(0, 1, size=(200, 10))
    no_drift = np.random.normal(0, 1, size=(200, 10))
    heavy_drift = np.random.normal(5, 2, size=(200, 10))
    
    clean_check = tracker.check_feature_drift(baseline, no_drift)
    assert clean_check["is_drift_detected"] is False
    
    drift_check = tracker.check_feature_drift(baseline, heavy_drift)
    assert drift_check["is_drift_detected"] is True
    assert drift_check["drift_ratio"] > 0.8
