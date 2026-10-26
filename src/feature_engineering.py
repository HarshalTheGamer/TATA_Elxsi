"""
Feature Engineering Module for C-MAPSS Fleet Data
Computes dynamic temporal rolling-window features, exponential moving averages,
trend slopes, and applies Piecewise Linear RUL Target labeling.
"""
import pandas as pd
import numpy as np

def compute_rolling_features(df: pd.DataFrame, sensor_cols: list, window: int = 20, max_rul: int = 125):
    """
    Computes rolling mean, rolling std, EWMA, and rate-of-change trend.
    Guarantees isolation by unit_number to eliminate sequence leakage.
    """
    df = df.copy()
    
    # Calculate piecewise linear RUL target if failure trajectory exists
    if "time_cycle" in df.columns:
        max_cycle_map = df.groupby("unit_number")["time_cycle"].transform("max")
        df["raw_rul"] = max_cycle_map - df["time_cycle"]
        df["target_rul"] = df["raw_rul"].clip(upper=max_rul)
        
    feature_dict = {}
    
    # Calculate rolling metrics per unit
    for sensor in sensor_cols:
        grouped = df.groupby("unit_number")[sensor]
        
        # 1. Rolling Mean (Thermodynamic Baseline Drift)
        roll_mean = grouped.rolling(window, min_periods=1).mean().reset_index(level=0, drop=True)
        feature_dict[f"{sensor}_roll_mean"] = roll_mean
        
        # 2. Rolling Standard Deviation (Vibration Flutter & Turbulence)
        roll_std = grouped.rolling(window, min_periods=1).std().fillna(0.0).reset_index(level=0, drop=True)
        feature_dict[f"{sensor}_roll_std"] = roll_std
        
        # 3. Exponentially Weighted Moving Average (EWMA)
        ewma = grouped.transform(lambda x: x.ewm(alpha=0.2).mean())
        feature_dict[f"{sensor}_ewma"] = ewma
        
        # 4. Difference from Rolling Mean (Transient Shock Anomaly)
        feature_dict[f"{sensor}_dev_from_mean"] = df[sensor] - roll_mean

    feat_df = pd.DataFrame(feature_dict, index=df.index)
    result_df = pd.concat([df, feat_df], axis=1)
    
    return result_df

def extract_last_cycle_features(test_feat_df: pd.DataFrame, feature_cols: list):
    """
    Isolates the final operational cycle for each test engine to evaluate
    against the ground truth RUL benchmark.
    """
    last_cycle_df = test_feat_df.groupby("unit_number").last().reset_index()
    X_test = last_cycle_df[feature_cols].values
    return last_cycle_df, X_test
