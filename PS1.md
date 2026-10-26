# Tata Elxsi — TELIPORT Season 4
## Case Study 1: Complete Problem Statement Specification & Requirements Matrix

**Program:** Tata Elxsi TELIPORT Season 4 ("THINK. BUILD. CREATE. WIN")  
**Track:** Case Study 1  
**Title:** **Self-Healing Machines: Predictive Maintenance for a Connected Fleet**  
**Document Status:** Complete Benchmark Reference & Requirements Specification  
**Dataset Reference:** NASA C-MAPSS Turbofan Engine Degradation Benchmark  

---

## 1. Background & Core Problem Statement

### 1.1 The Industrial Challenge
In modern fleet operations—encompassing commercial transport (trucks, buses), industrial equipment (heavy compressors, pumps, generators), and aerospace fleets—thousands of connected machines continuously stream operational telemetry:
- **Vibration signatures**
- **Temperature profiles**
- **Motor / line current**
- **Inlet & outlet pressures**
- **Rotational speed (RPM) & operational settings**

### 1.2 The Current Operational Bottleneck
Historically, fleet operations manage equipment health through two deeply flawed paradigms:
1. **Reactive Maintenance (Run-to-Failure):** Failures are diagnosed only *after* a catastrophic breakdown occurs, incurring exorbitant emergency repair costs, secondary component destruction, supply-chain bottlenecks, and severe safety/environmental risks.
2. **Fixed Service Intervals (Calendar / Run-Hour Maintenance):** Machines are serviced on rigid schedules regardless of actual health status. This leads to premature part replacement (wasting up to 30–40% of useful component life) while remaining blind to sudden early-stage degradation occurring between intervals.

### 1.3 The Mandatory Challenge Mandate
> **The team must build an end-to-end, closed-loop system that ingests streaming or batch sensor data from a connected fleet, detects early signs of degradation, predicts how much Remaining Useful Life (RUL) a machine has left, and automatically raises an actionable maintenance work order—with a human stepping in only for exceptions.**

---

## 2. Strict Ground Rules & Constraints

To succeed in evaluation, the solution must strictly comply with four non-negotiable architectural constraints:

| Constraint | Ground Rule Description | Technical Enforcement |
|---|---|---|
| **1. Class Imbalance Handling** | Degradation and catastrophic failures are rare events compared to nominal operating cycles. | The modeling pipeline must explicitly mitigate class imbalance via threshold tuning, asymmetric loss weighting, or piecewise linear RUL targets. |
| **2. Zero Manual Steps (End-to-End)** | The entire workflow from raw data ingestion to work-order issuance must execute without human intervention once data is loaded. | Pipeline automation via reproducible CLI/Python scripts and event-driven triggers. |
| **3. Lightweight — Strictly NO LLM** | **Generative LLMs are explicitly prohibited** in the triage decision loop. The triage agent must be lightweight, transparent, and rule-based. | Implement deterministic Finite State Machine (FSM) or threshold-based multi-criteria logic. |
| **4. Open-Source & Explainability** | Must use transparent open-source libraries and be fully documented for engineering review. | Standard libraries: `pandas`, `numpy`, `scikit-learn`, `xgboost`, `mlflow`, `matplotlib`, `fastapi`. |

---

## 3. The Benchmark Dataset: NASA C-MAPSS

The evaluation benchmark is the **NASA Commercial Modular Aero-Propulsion System Simulation (C-MAPSS)** dataset—the gold standard benchmark in aerospace and industrial fleet prognostics.

### 3.1 Overview
- **Data Source:** Simulated run-to-failure trajectories of turbofan engines under realistic operational profiles.
- **Sensors:** 21 physical sensor measurements (temperatures, pressures, fan speeds, bleed ratios, coolant flows).
- **Operating Conditions:** 3 altitude/mach/throttle operational settings (`setting_1`, `setting_2`, `setting_3`).
- **Ground Truth:** True Remaining Useful Life (RUL) values provided for test engine evaluation.

### 3.2 Dataset Subsets & Complexity Scaling
The dataset is structured into four subsets representing escalating industrial complexity:

| Subset ID | Operating Conditions | Fault Modes | Train Units | Test Units | Benchmark Complexity |
|---|:---:|:---:|:---:|:---:|---|
| **FD001** | **1 (Sea Level)** | **1 (HPC Degradation)** | 100 | 100 | **Baseline Benchmark** (Ideal starting point) |
| **FD002** | **6 (Multi-Regime)** | **1 (HPC Degradation)** | 260 | 259 | **High Complexity** (Requires regime clustering) |
| **FD003** | **1 (Sea Level)** | **2 (HPC + Fan Degradation)**| 100 | 100 | **Multi-Fault Complexity** |
| **FD004** | **6 (Multi-Regime)** | **2 (HPC + Fan Degradation)**| 249 | 248 | **Maximum Industrial Complexity** |

*Note: The project must provide 100% verified results on **FD001** as baseline, with an extensible architecture capable of handling **FD002–FD004**.*

---

## 4. The Four Mandatory Architectural Layers

The solution architecture is formally evaluated across four functional layers:

```
+--------------------------------------------------------------------------------------------------+
|                                  THE 4 MANDATORY SOLUTION LAYERS                                 |
+--------------------------------------------------------------------------------------------------+
|                                                                                                  |
|  [LAYER 1: DATA ENGINEERING]                                                                     |
|  - Ingest sensor streams (21 sensors + 3 operational settings)                                   |
|  - Handle missing values, sensor dropouts, and measurement noise                                 |
|  - Construct rolling-window aggregations (rolling mean, rolling std, EWMA, slope/trend)          |
|                                                                                                  |
|  [LAYER 2: MACHINE LEARNING]                                                                     |
|  - Anomaly Detection: Detect onset of uncharacteristic wear trajectories                         |
|  - RUL Regression: Continuous prediction of Remaining Useful Life (cycles to failure)            |
|  - Piecewise Linear RUL Target formulation ($RUL_{max} \approx 125$)                              |
|                                                                                                  |
|  [LAYER 3: MLOPS]                                                                                |
|  - Experiment Tracking: MLflow integration logging hyperparameters, RMSE, and NASA scores        |
|  - Model Registry: Versioned model artifacts with lineage tracking                              |
|  - Automated Retraining Pipeline: Triggered when new fleet run batches or drift is detected      |
|  - Operational Monitoring: Live performance tracking and degradation views                       |
|                                                                                                  |
|  [LAYER 4: AGENTS (NON-LLM)]                                                                     |
|  - Rule-Based Triage Agent: Evaluates RUL + Anomaly Score against risk matrices                  |
|  - Multi-Tier Severity Classification: CRITICAL vs WARNING vs NORMAL                             |
|  - Automated Work Order (AWO): Machine ID, failed subsystem, deadline, parts, dispatch payload   |
|  - Human-in-the-Loop: Escalation triggered strictly on ambiguous or conflicting edge cases      |
|                                                                                                  |
+--------------------------------------------------------------------------------------------------+
```

---

## 5. Round-Wise Deliverables

### Round 1: Idea Submission — Design Deck
A structured architectural and conceptual slide deck demonstrating:
1. **End-to-End Architecture Diagram:** Data Ingestion $\rightarrow$ Feature Engineering $\rightarrow$ Model Inference $\rightarrow$ Triage Agent $\rightarrow$ Automated Work Order $\rightarrow$ Closed-Loop Remediation.
2. **Data Engineering Approach:** Data cleaning, sensor filtering (removing invariant sensors), rolling window parameter justification, and normalization strategy across operating regimes.
3. **ML Modeling Rationale:** Mathematical and empirical justification of chosen Anomaly Detection and RUL Regression algorithms (e.g., Random Forest / XGBoost vs. Deep Learning LSTM/1D-CNN), handling asymmetric failure cost.
4. **Triage Agent Logic:** Formalized decision trees, state machines, threshold definitions, and Work Order data schemas.

### Round 2: Detailed Submission — Working Proof of Concept (PoC)
A fully operational software implementation demonstrating:
1. **Working End-to-End Pipeline:** Automated execution script processing NASA C-MAPSS dataset from raw text files to final work orders without manual intervention.
2. **Trained High-Performance RUL Model:** Verifiable RUL predictions with documented test metrics (RMSE, MAE, NASA Asymmetric Score).
3. **Operational Monitoring Dashboard:** Interactive view tracking fleet machine status, sensor trajectories, predicted RUL countdown, and active alerts.
4. **Agent Work-Order Generation & Retraining Run:** Live demonstration of the triage agent issuing structured work orders and an automated model retraining trigger executed on incoming data.

---

## 6. Official Evaluation Criteria & Scoring Matrix

### Round 1 — Evaluation of Design (100% Weightage)
| Criterion | Weight | What the Jury Assesses | Target Standard for Maximum Score |
|---|:---:|---|---|
| **Problem Understanding** | **15%** | Clear, accurate grasp of connected fleet dynamics and business objectives. | Deep articulation of downtime economics, failure modes, and closed-loop self-healing paradigms. |
| **Architecture Clarity** | **20%** | Coherent, well-organized modular design with clear data contracts. | Full C4/UML architectural clarity across all 4 layers with zero ambiguities. |
| **Data Engineering Approach** | **15%** | Sound, well-reasoned input preparation and feature transformation. | Exhaustive sensor filtering, rolling temporal statistics, and regime-aware normalization. |
| **ML Approach & Reasoning** | **20%** | Suitable model selection, justified trade-offs, and failure-cost awareness. | Piecewise linear RUL formulation, asymmetric NASA cost penalization, and model benchmarking. |
| **MLOps & Agent Logic** | **15%** | Practical operational plan and clear deterministic decision flow. | MLflow tracking setup, model versioning, retraining trigger logic, and robust FSM triage rules. |
| **Dataset Coverage** | **10%** | Scales across data complexity (FD001 baseline $\rightarrow$ multi-regime FD002/004). | Documented strategy handling single-condition and multi-regime degradation datasets. |
| **Communication Quality** | **5%** | Professional, structured, consistent, and visually compelling documentation. | Flawless technical presentation, publication-grade diagrams, and crisp engineering prose. |

### Round 2 — Evaluation of Proof of Concept (100% Weightage)
| Criterion | Weight | What the Jury Assesses | Target Standard for Maximum Score |
|---|:---:|---|---|
| **Working Pipeline** | **20%** | Runs end-to-end with minimal manual intervention. | Single-command execution orchestrating ingestion, inference, triage, and work order generation. |
| **Data Engineering Quality** | **15%** | Clean, robust, reproducible data processing without data leakage. | Production-grade pipeline code with clean test train isolation and zero synthetic leakages. |
| **Model Performance** | **15%** | Credible results with sensibly interpreted evaluation metrics. | Competitive test RMSE ($< 16$ cycles on FD001) and low NASA penalty score. |
| **MLOps in Action** | **10%** | Operational elements are functional and demonstrable. | Active MLflow experiment logging and observable dynamic retraining trigger. |
| **Agent Behavior** | **10%** | Acts correctly and reliably on model predictions without false triggers. | 100% precision on critical RUL work order issuance and robust threshold safety buffers. |
| **Dataset Coverage** | **10%** | Depth and breadth tackled relative to dataset complexity. | Flawless evaluation across FD001 benchmark with ready test harness for FD002–FD004. |
| **Demo & Explanation** | **20%** | Team articulates choices, trade-offs, and future improvements convincingly. | High-impact interactive dashboard demonstrating live degradation, self-healing triage, and work orders. |
