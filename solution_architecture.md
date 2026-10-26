# Tata Elxsi — TELIPORT Season 4
## End-to-End Solution Architecture & System Specification

**Project:** Autonomous Self-Healing Fleet: Closed-Loop Predictive Maintenance Platform  
**Target Benchmark:** NASA C-MAPSS Turbofan Engine Fleet Degradation (FD001–FD004)  
**Execution Paradigm:** Edge-to-Cloud Closed-Loop Autonomics (Deterministic & Non-LLM)  

---

## 1. High-Level System Architecture & End-to-End Pipeline

The system is architected as an automated, closed-loop cyber-physical pipeline consisting of five tightly integrated pipeline stages across the four mandated layers:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                             END-TO-END SYSTEM DATA FLOW                                                │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
                                                         │
                                                         ▼
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 1. DATA INGESTION & SENSOR PREPROCESSING (Layer 1)                                                                     │
│    • Ingest C-MAPSS Telemetry (21 Sensors + 3 Operational Settings across Unit Trajectories)                           │
│    • Flat/Invariant Sensor Elimination (Drop Sensors 1, 5, 10, 16, 18, 19)                                             │
│    • Missing-Value Imputation & Sensor Noise Smoothing (Low-pass Butterworth / Moving Average)                         │
└────────────────────────────────────────────────────────┬───────────────────────────────────────────────────────────────┘
                                                         │
                                                         ▼
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 2. TEMPORAL FEATURE ENGINEERING (Layer 1)                                                                              │
│    • Rolling-Window Statistics (Window size w = 20 or 30 cycles): Rolling Mean (μ), Rolling Std (σ)                    │
│    • Trend & Dynamics: Exponentially Weighted Moving Average (EWMA), Rate-of-Change (Slope Δs/Δt)                      │
│    • Operating Regime Normalization (K-Means Clustering on Settings 1-3 for FD002/FD004; MinMax for FD001)             │
└────────────────────────────────────────────────────────┬───────────────────────────────────────────────────────────────┘
                                                         │
                                                         ▼
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 3. ML INFERENCE ENGINE: ANOMALY DETECTION & RUL PROGNOSIS (Layer 2)                                                    │
│    • Anomaly Scoring: Multi-Sensor Reconstruction Residuals / Isolation Forest Health Index                            │
│    • RUL Predictor: Piecewise Linear Formulation ($RUL_{max} = 125$) via Tuned XGBoost / Random Forest Regressor       │
│    • Metric Optimization: Penalizes Late Predictions via NASA Asymmetric Scoring Function                              │
└────────────────────────────────────────────────────────┬───────────────────────────────────────────────────────────────┘
                                                         │
                             ┌───────────────────────────┴───────────────────────────┐
                             ▼                                                       ▼
┌──────────────────────────────────────────────────────┐  ┌──────────────────────────────────────────────────────────────┐
│ 4. MLOPS & RETRAINING LIFECYCLE (Layer 3)            │  │ 5. RULE-BASED TRIAGE AGENT & WORK ORDER (Layer 4)             │
│    • MLflow Experiment Tracking & Metric Logging     │  │    • Deterministic Finite State Machine (FSM) Triage          │
│    • Model Registry: Versioned Artifacts (.joblib)   │  │    • Multi-Threshold Risk Classification:                    │
│    • Drift Monitoring: KS-Test on Sensor Residuals   │  │       - CRITICAL ($RUL \le 15$ cycles): Instant Work Order    │
│    • Automated Retraining Trigger Pipeline           │  │       - WARNING ($15 < RUL \le 35$): Soft In-Situ Derating   │
│                                                      │  │       - HEALTHY ($RUL > 35$): Nominal Operation               │
│                                                      │  │    • Automated Work Order (AWO) Generator (ISO 55000 Schema) │
│                                                      │  │    • Human Exception Handler (Sensor Dropout / Conflict)     │
└──────────────────────────────────────────────────────┘  └──────────────────────────────┬───────────────────────────────┘
                                                                                         │
                                                                                         ▼
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 6. CLOSED-LOOP SELF-HEALING EXECUTION & FLEET DASHBOARD                                                                │
│    • Tier 1: Soft-Healing Telematics Command (Throttle Derate / Load Shedding to extend remaining life)                │
│    • Tier 2: Automated Dispatch to Depot CMMS with Prescriptive Parts & Servicing Blueprint                            │
│    • Fleet Monitoring View: Interactive Fleet Health Grid & Asset Trajectory Visualizer                                │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Layer 1: Data Engineering Specification

### 2.1 NASA C-MAPSS Sensor Topology & Feature Elimination
The raw C-MAPSS dataset consists of 26 columns per run:
- Column 1: `unit_number` (Engine identifier)
- Column 2: `time_cycle` (Operating time in flight cycles)
- Columns 3–5: `setting_1`, `setting_2`, `setting_3` (Altitude, Mach number, Throttle resolver angle)
- Columns 6–26: `sensor_1` through `sensor_21` (Physical thermodynamic & aerodynamic measurements)

#### Invariant Sensor Elimination
Through empirical variance analysis across all units, six sensors exhibit near-zero variance ($\sigma^2 \approx 0$) regardless of health state because they are regulated by closed-loop control or represent static ambient conditions:
- `sensor_1`: Fan inlet temperature ($T_2$)
- `sensor_5`: Low-Pressure Compressor inlet pressure ($P_2$)
- `sensor_10`: High-Pressure Compressor inlet pressure ($P_{15}$)
- `sensor_16`: Bypass duct static pressure ($P_{30}$)
- `sensor_18`: Demanded fan speed ($N_{f\_dmd}$)
- `sensor_19`: Demanded corrected core speed ($N_{c\_dmd}$)

**Action:** These 6 invariant sensors are systematically dropped during ingestion, reducing dimensionality from 21 to **15 highly discriminative prognostic sensors**.

### 2.2 Temporal Rolling-Window Feature Engineering
Because turbofan degradation is a dynamic process characterized by cumulative wear, instantaneous sensor readings are insufficient. We compute rolling temporal features over a sliding window of length $w = 20$ or $30$ cycles:

1. **Rolling Mean ($\mu_{i,t}$):**
   $$\mu_{i,t}^{(w)} = \frac{1}{w} \sum_{k=0}^{w-1} s_{i,t-k}$$
   Captures the baseline thermodynamic drift and structural shifts in pressure and temperature.

2. **Rolling Standard Deviation ($\sigma_{i,t}$):**
   $$\sigma_{i,t}^{(w)} = \sqrt{\frac{1}{w-1} \sum_{k=0}^{w-1} \left(s_{i,t-k} - \mu_{i,t}^{(w)}\right)^2}$$
   Captures increasing mechanical turbulence, combustion instability, and blade vibration flutter.

3. **Rate of Degradation (Rolling Trend / Slope $\beta_{i,t}$):**
   $$\beta_{i,t}^{(w)} = \frac{\sum_{k=0}^{w-1} (k - \bar{k})(s_{i,t-w+1+k} - \bar{s})}{\sum_{k=0}^{w-1} (k - \bar{k})^2}$$
   Measures the acceleration of degradation (first derivative).

4. **Exponentially Weighted Moving Average (EWMA):**
   $$\text{EWMA}_t = \alpha \cdot s_t + (1 - \alpha) \cdot \text{EWMA}_{t-1} \quad (\alpha = 0.2)$$
   Smooths high-frequency sensor noise while preserving rapid degradation inflections.

### 2.3 Regime-Aware Normalization (Scalability to FD002/FD004)
- **For FD001 (Single Regime):** Features are normalized using `MinMaxScaler` fitted strictly on the training set:
  $$\tilde{x} = \frac{x - x_{min}}{x_{max} - x_{min}}$$
- **For FD002 & FD004 (6 Operating Regimes):** Operating conditions (`setting_1`, `setting_2`, `setting_3`) define distinct flight envelopes. We apply K-Means clustering ($K=6$) to identify operating regimes, followed by cluster-specific standard normalization:
  $$\tilde{x}_{t} = \frac{x_t - \mu_{\text{regime}(t)}}{\sigma_{\text{regime}(t)}}$$
  This strips away operational shifts, isolating pure hardware degradation.

---

## 3. Layer 2: Machine Learning Modeling (RUL Prognosis & Anomaly Detection)

### 3.1 Piecewise Linear RUL Target Formulation
In physical turbofan operation, components experience initial zero-degradation "run-in" wear where no measurable degradation occurs. Degradation becomes observable only after micro-cracks or blade erosion begin accumulating.

To prevent models from attempting to predict infinite or misleadingly linear decay from day one, we adopt the standard industrial **Piecewise Linear RUL Function**:
$$\text{RUL}_{\text{target}}(t) = \min\left(RUL_{\max}, \, T_{\text{failure}} - t\right)$$
where $RUL_{\max} = 125$ cycles (empirically derived as the threshold where thermodynamic sensor deviations become statistically significant).

```
RUL
 ^
125 ┌──────────────────────────────────────┐
    │          Normal Operation            │ \
    │         (Zero Degradation)           │   \  Degradation Phase
    │                                      │     \ (Observable Wear)
    │                                      │       \
  0 └──────────────────────────────────────┴─────────\──────> Time (Cycles)
    0                                     t_inflection  T_failure
```

### 3.2 Predictive Model Architecture: XGBoost / Random Forest Regressor
We implement an ensemble of gradient-boosted decision trees (`XGBRegressor`) benchmarked against `RandomForestRegressor`:
- **Hyperparameter Configuration:**
  - `n_estimators`: 250
  - `max_depth`: 6
  - `learning_rate`: 0.04
  - `subsample`: 0.85
  - `colsample_bytree`: 0.85
- **Advantages over Heavy Deep Learning:**
  - **Zero Training Latency:** Trains in seconds rather than hours.
  - **Inherent Interpretability:** Direct extraction of feature importances (e.g., Sensor 11: HP Turbine exit temperature and Sensor 12: Core speed as primary degradation drivers).
  - **Lightweight Edge Deployment:** Model footprint $< 15 \text{ MB}$, easily executable on edge telematics units.

### 3.3 Loss Function & NASA Asymmetric Scoring
In fleet maintenance, **a late prediction is catastrophically worse than an early prediction:**
- If the model predicts an engine has 30 cycles left when it actually has 10 (Late prediction: $\Delta > 0$), the engine suffers an in-flight shutdown or catastrophic rotor failure.
- If the model predicts 10 cycles when it actually has 30 (Early prediction: $\Delta < 0$), the engine is serviced slightly prematurely, costing minimal maintenance hours.

We evaluate both Root Mean Squared Error (RMSE) and the **Official NASA Asymmetric Scoring Metric**:
$$S = \sum_{i=1}^{N} s_i$$
$$\text{where } s_i = \begin{cases} 
\exp\left(-\frac{d_i}{13}\right) - 1 & \text{for } d_i < 0 \quad (\text{Early prediction, gentle penalty}) \\
\exp\left(\frac{d_i}{10}\right) - 1 & \text{for } d_i \ge 0 \quad (\text{Late prediction, exponential penalty}) 
\end{cases}$$
where $d_i = \hat{y}_i - y_i$ is the prediction residual.

---

## 4. Layer 3: MLOps & Retraining Pipeline

### 4.1 MLflow Tracking & Governance
All training runs, feature parameterizations, and evaluations are governed via **MLflow**:
- **Run Tracking:** Logs dataset version (e.g., `FD001_v1`), window size ($w$), tree depth, subsample ratios.
- **Metric Tracking:** Continuous logging of Train RMSE, Validation RMSE, Test RMSE, NASA Score, and Inference Latency (ms).
- **Artifact Registry:** Stores serialised pipelines (`pipeline.joblib`), scaler objects (`scaler.joblib`), feature lists, and residual diagnostic plots.

### 4.2 Automated Retraining Trigger Pipeline
To fulfill the requirement of an automated retraining flow when new fleet data arrives:
1. **Streaming Batch Arrival:** When a batch of completed engine cycles arrives from the fleet, the system calculates the **Population Stability Index (PSI)** and **Kolmogorov-Smirnov (KS) test** across sensor feature distributions.
2. **Drift Detection:** If feature drift exceeds threshold ($\text{PSI} > 0.25$) or if prediction residuals on verified depot inspections increase by $> 20\%$, the system automatically issues a trigger.
3. **Automated Pipeline Execution:**
   - Triggers `/api/ml/retrain` endpoint.
   - Refits scalers and trains candidate model $M_{\text{new}}$.
   - Runs automated backtesting against holdout benchmark.
   - If $M_{\text{new}}$ outperforms current champion model $M_{\text{champ}}$ on NASA Score, $M_{\text{new}}$ is automatically promoted to production in the model registry.

---

## 5. Layer 4: Non-LLM Rule-Based Triage Agent

### 5.1 Deterministic Finite State Machine (FSM)
In compliance with the **Strict NO-LLM rule**, the Triage Agent is implemented as a deterministic Finite State Machine (FSM) executing multi-criteria safety evaluation:

```
                  ┌───────────────┐
                  │    HEALTHY    │ (RUL > 35 cycles)
                  └───────┬───────┘
                          │ Anomaly Score > Threshold AND RUL <= 35
                          ▼
                  ┌───────────────┐
                  │    WARNING    │ (15 < RUL <= 35 cycles)
                  │ (Soft Heal)   │ -> Command 15% Throttle Derate to Fleet Telematics
                  └───────┬───────┘
                          │ RUL <= 15 cycles
                          ▼
                  ┌───────────────┐
                  │   CRITICAL    │ (RUL <= 15 cycles)
                  │ (Auto-Dispatch│ -> Generate Automated Work Order (AWO) to CMMS
                  └───────┬───────┘
                          │ Sensor Conflict / Physical Sensor Dropout
                          ▼
                  ┌───────────────┐
                  │   EXCEPTION   │ -> Escalate to Human Reliability Engineer
                  └───────────────┘
```

### 5.2 Automated Work Order (AWO) JSON Schema
When an asset enters `CRITICAL` or `WARNING` state, the agent instantaneously emits an ISO 55000-compliant Work Order payload:

```json
{
  "work_order_id": "AWO-ELXSI-FD001-U042-20261026",
  "generated_at": "2026-10-26T19:30:00Z",
  "status": "DISPATCHED_TO_CMMS",
  "priority": "HIGH_P1",
  "asset_metadata": {
    "fleet_id": "AERO_FLEET_WEST",
    "unit_id": 42,
    "asset_type": "Turbofan Engine (C-MAPSS Class)",
    "current_operating_cycle": 182
  },
  "diagnostic_telemetry": {
    "predicted_rul_cycles": 11.4,
    "confidence_interval_95": [9.8, 13.1],
    "health_index": 0.18,
    "primary_degrading_subsystem": "High-Pressure Compressor (HPC)",
    "critical_sensor_alerts": [
      {"sensor": "s11", "name": "HPC Outlet Static Pressure", "deviation_sigma": 3.8},
      {"sensor": "s12", "name": "Physical Core Speed", "deviation_sigma": 3.2}
    ]
  },
  "autonomous_prescriptions": {
    "tier_1_in_situ_action": {
      "command": "APPLY_OPERATIONAL_DERATE",
      "throttle_cap": "85%",
      "projected_cycles_extended": 18
    },
    "tier_2_maintenance_action": {
      "action_type": "BORESCOPE_INSPECT_AND_OVERHAUL_HPC",
      "required_spares": ["PART-BLADE-HPC-SET-A", "PART-SEAL-CORE-04"],
      "estimated_depot_downtime_hours": 14.5,
      "recommended_depot": "DEPOT-NORTH-HUB"
    }
  },
  "exception_flags": {
    "human_review_required": false,
    "reason": "All prognostic sensors consistent; zero telemetry dropouts."
  }
}
```

### 5.3 Exception Handling Protocol (Human-in-the-Loop)
Human intervention is triggered **strictly on exceptional boundary conditions**:
1. **Telemetry Dropout:** If $> 3$ consecutive cycle records are dropped by IoT communication channels.
2. **Sensor Discrepancy (Analytical Redundancy Violation):** If core temperature sensors indicate critical overheating, but exhaust gas pressure and shaft speeds remain completely nominal (indicating sensor failure rather than engine failure).
3. **Inventory Out-of-Stock:** If the depot inventory database reports zero replacement blade sets for the recommended maintenance window.
