"""
AERO-SHIELD: Autonomous Closed-Loop Self-Healing Fleet Pipeline
Single-command automated runner:
Data Ingestion ➔ Temporal Features ➔ XGBoost Model ➔ MLflow Logging ➔ Triage Agent ➔ Work Orders
"""
import os
import sys
import json
import time

# Ensure project root is in Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.data_loader import load_cmapss_data, ACTIVE_SENSORS
from src.feature_engineering import compute_rolling_features, extract_last_cycle_features
from src.model_engine import RULPredictor
from src.mlops_tracker import FleetMLOpsTracker
from src.triage_agent import FleetTriageAgent

def run_end_to_end():
    start_time = time.time()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data", "raw")
    models_dir = os.path.join(base_dir, "models")
    reports_dir = os.path.join(base_dir, "reports")
    work_orders_dir = os.path.join(reports_dir, "generated_work_orders")
    
    os.makedirs(models_dir, exist_ok=True)
    os.makedirs(work_orders_dir, exist_ok=True)

    print("=" * 80)
    print("AERO-SHIELD: AUTONOMOUS CLOSED-LOOP SELF-HEALING FLEET PIPELINE")
    print("Benchmark: NASA C-MAPSS Turbofan Engine Fleet Degradation (FD001)")
    print("=" * 80)

    # -------------------------------------------------------------------------
    # STAGE 1: Data Ingestion & Sensor Pruning
    # -------------------------------------------------------------------------
    print("\n[Stage 1/5] Ingesting NASA C-MAPSS FD001 Telemetry...")
    train_df, test_df, rul_df = load_cmapss_data(data_dir, subset="FD001")
    n_train_units = train_df["unit_number"].nunique()
    n_test_units = test_df["unit_number"].nunique()
    print(f" -> Training Engines: {n_train_units} units ({len(train_df)} total cycle records)")
    print(f" -> Test Engines:     {n_test_units} units ({len(test_df)} total cycle records)")
    print(f" -> Active Prognostic Sensors: {len(ACTIVE_SENSORS)} channels (6 flat sensors pruned)")

    # -------------------------------------------------------------------------
    # STAGE 2: Temporal Rolling-Window Feature Engineering
    # -------------------------------------------------------------------------
    print("\n[Stage 2/5] Computing Dynamic Rolling-Window Features (w = 20 cycles)...")
    train_feat = compute_rolling_features(train_df, ACTIVE_SENSORS, window=20, max_rul=125)
    test_feat = compute_rolling_features(test_df, ACTIVE_SENSORS, window=20, max_rul=125)

    # Feature column selection (rolling mean, std, ewma, dev)
    feature_cols = [c for c in train_feat.columns if any(k in c for k in ["roll_mean", "roll_std", "ewma", "dev_from_mean"])]
    print(f" -> Extracted {len(feature_cols)} temporal dynamic features per engine cycle.")

    X_train = train_feat[feature_cols].values
    y_train = train_feat["target_rul"].values

    last_cycle_test_df, X_test = extract_last_cycle_features(test_feat, feature_cols)
    y_test = rul_df["true_rul"].values

    # -------------------------------------------------------------------------
    # STAGE 3: Machine Learning Model Training (Piecewise Linear XGBoost)
    # -------------------------------------------------------------------------
    print("\n[Stage 3/5] Training Piecewise Linear XGBoost RUL Regressor...")
    model_path = os.path.join(models_dir, "rul_model.joblib")
    predictor = RULPredictor(n_estimators=250, max_depth=6, learning_rate=0.04)
    predictor.fit(X_train, y_train, feature_names=feature_cols)
    predictor.save(model_path)
    print(f" -> Model trained and saved to: {model_path}")

    # Evaluate on holdout test units
    metrics = predictor.evaluate(X_test, y_test)
    print(" ------------------------------------------------------------------------------")
    print(f"  • Test RMSE:                    {metrics['rmse']} cycles")
    print(f"  • Test MAE:                     {metrics['mae']} cycles")
    print(f"  • Test R2 Score:                {metrics['r2_score']}")
    print(f"  • Official NASA Score:          {metrics['nasa_score']}")
    print(f"  • Accuracy within +/-15 cycles: {metrics['accuracy_within_15_cycles_pct']}%")
    print(f"  • Accuracy within +/-25 cycles: {metrics['accuracy_within_25_cycles_pct']}%")
    print(f"  • Mean Asymmetric Bias:         {metrics['mean_residual_bias']} cycles")
    print(" ------------------------------------------------------------------------------")

    # -------------------------------------------------------------------------
    # STAGE 4: MLOps Tracking & Drift Evaluation
    # -------------------------------------------------------------------------
    print("\n[Stage 4/5] Logging Artifacts to MLflow Governance Registry...")
    tracker = FleetMLOpsTracker()
    run_id = tracker.log_run(
        params={
            "model_type": "XGBRegressor",
            "n_estimators": 250,
            "max_depth": 6,
            "learning_rate": 0.04,
            "window_size": 20,
            "piecewise_max_rul": 125,
            "dataset": "NASA_CMAPSS_FD001"
        },
        metrics=metrics,
        model_path=model_path
    )
    
    # Check for feature drift between early training cycles and late test cycles
    drift_report = tracker.check_feature_drift(X_train[:500], X_test)
    print(f" -> Drift Check: Drift Detected = {drift_report['is_drift_detected']} (Ratio: {drift_report['drift_ratio']})")

    # -------------------------------------------------------------------------
    # STAGE 5: Non-LLM Triage Agent & Closed-Loop Work Order Issuance
    # -------------------------------------------------------------------------
    print("\n[Stage 5/5] Activating Deterministic Non-LLM Triage Agent...")
    agent = FleetTriageAgent(critical_threshold=15.0, warning_threshold=35.0)
    
    fleet_summary = []
    generated_work_orders = []

    for idx, row in last_cycle_test_df.iterrows():
        unit_id = int(row["unit_number"])
        current_cycle = int(row["time_cycle"])
        pred_rul = metrics["y_pred"][idx]
        true_rul = metrics["y_true"][idx]
        
        # Sensor snapshot for audit
        sensor_snap = {f"sensor_{s}": round(float(row.get(f"sensor_{s}", 0.0)), 2) for s in [2, 3, 4, 7, 8, 11, 12, 14, 15]}

        triage_res = agent.evaluate_unit(
            unit_id=unit_id,
            current_cycle=current_cycle,
            predicted_rul=pred_rul,
            sensor_summary=sensor_snap
        )
        
        unit_record = {
            "unit_id": unit_id,
            "current_cycle": current_cycle,
            "predicted_rul": triage_res["predicted_rul"],
            "true_rul": round(float(true_rul), 1),
            "state": triage_res["state"],
            "projected_extension_cycles": triage_res["projected_extension_cycles"],
            "tier1_command": triage_res["tier1_command"],
            "has_work_order": triage_res["requires_work_order"],
            "sensors": sensor_snap
        }
        
        if triage_res["work_order"]:
            wo = triage_res["work_order"]
            agent.save_work_order(wo, work_orders_dir)
            generated_work_orders.append(wo)
            unit_record["work_order_id"] = wo["work_order_id"]
            
        fleet_summary.append(unit_record)

    # Save reports
    with open(os.path.join(reports_dir, "test_metrics.json"), "w") as f:
        json.dump(metrics, f, indent=2)
        
    with open(os.path.join(reports_dir, "fleet_status.json"), "w") as f:
        json.dump({
            "fleet_size": len(fleet_summary),
            "healthy_count": sum(1 for u in fleet_summary if u["state"] == "HEALTHY"),
            "warning_count": sum(1 for u in fleet_summary if u["state"] == "WARNING"),
            "critical_count": sum(1 for u in fleet_summary if u["state"] == "CRITICAL"),
            "work_orders_issued": len(generated_work_orders),
            "metrics": {
                "rmse": metrics["rmse"],
                "mae": metrics["mae"],
                "nasa_score": metrics["nasa_score"],
                "accuracy_15_cycles": metrics["accuracy_within_15_cycles_pct"]
            },
            "engines": fleet_summary
        }, f, indent=2)

    elapsed = round(time.time() - start_time, 2)
    print("=" * 80)
    print(f"PIPELINE COMPLETED SUCCESSFULLY in {elapsed}s with ZERO manual steps.")
    print(f" -> Work Orders Dispatched: {len(generated_work_orders)} to {work_orders_dir}")
    print(f" -> Fleet Status Database:  {os.path.join(reports_dir, 'fleet_status.json')}")
    print("=" * 80)

if __name__ == "__main__":
    run_end_to_end()
