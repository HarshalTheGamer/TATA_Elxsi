"""
Builder script for AERO_SHIELD_Interactive_Prototype.html
Compiles real NASA C-MAPSS fleet telemetry and pipeline predictions from
reports/fleet_status.json into an ultra-premium, glassmorphic cyber-physical dashboard.
"""
import os
import json

def build_prototype_html():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    fleet_json_path = os.path.join(base_dir, "reports", "fleet_status.json")
    out_html_path = os.path.join(base_dir, "AERO_SHIELD_Interactive_Prototype.html")
    
    if os.path.exists(fleet_json_path):
        with open(fleet_json_path, "r") as f:
            fleet_data = json.load(f)
    else:
        # Fallback dummy data if file is missing
        fleet_data = {
            "fleet_size": 100,
            "healthy_count": 81,
            "warning_count": 14,
            "critical_count": 5,
            "work_orders_issued": 19,
            "metrics": {"rmse": 18.21, "mae": 11.65, "nasa_score": 1712.6, "accuracy_15_cycles": 72.0},
            "engines": []
        }

    fleet_json_str = json.dumps(fleet_data)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AERO-SHIELD // Connected Fleet Prognostics & Self-Healing Control</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-dark: #070B14;
      --bg-card: rgba(15, 23, 42, 0.70);
      --bg-card-hover: rgba(30, 41, 59, 0.85);
      --border-glass: rgba(255, 255, 255, 0.08);
      --border-accent: rgba(0, 240, 255, 0.3);
      --cyan: #00F0FF;
      --cyan-glow: rgba(0, 240, 255, 0.15);
      --emerald: #10B981;
      --amber: #F59E0B;
      --rose: #F43F5E;
      --slate-300: #CBD5E1;
      --slate-400: #94A3B8;
      --slate-500: #64748B;
      --slate-800: #1E293B;
      --text-main: #F8FAFC;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-dark);
      color: var(--text-main);
      min-height: 100vh;
      overflow-x: hidden;
      background-image: 
        radial-gradient(circle at 15% 15%, rgba(0, 240, 255, 0.07) 0%, transparent 40%),
        radial-gradient(circle at 85% 20%, rgba(16, 185, 129, 0.06) 0%, transparent 45%),
        radial-gradient(circle at 50% 85%, rgba(244, 63, 94, 0.05) 0%, transparent 50%);
      background-attachment: fixed;
    }}

    /* Top Command Header */
    header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1rem 2rem;
      background: rgba(11, 17, 33, 0.8);
      backdrop-filter: blur(20px);
      border-bottom: 1px solid var(--border-glass);
      position: sticky;
      top: 0;
      z-index: 100;
    }}

    .brand-section {{
      display: flex;
      align-items: center;
      gap: 1.2rem;
    }}

    .brand-logo-badge {{
      background: linear-gradient(135deg, #00F0FF 0%, #0284C7 100%);
      color: #070B14;
      font-weight: 800;
      font-size: 1.1rem;
      padding: 0.4rem 0.8rem;
      border-radius: 8px;
      letter-spacing: -0.5px;
      box-shadow: 0 0 20px rgba(0, 240, 255, 0.4);
    }}

    .brand-title h1 {{
      font-size: 1.25rem;
      font-weight: 700;
      letter-spacing: -0.3px;
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }}

    .brand-title p {{
      font-size: 0.75rem;
      color: var(--slate-400);
      font-family: 'JetBrains Mono', monospace;
    }}

    .live-pulse {{
      display: inline-block;
      width: 8px;
      height: 8px;
      background-color: var(--emerald);
      border-radius: 50%;
      box-shadow: 0 0 10px var(--emerald);
      animation: pulseGlow 1.8s infinite;
    }}

    @keyframes pulseGlow {{
      0%, 100% {{ transform: scale(1); opacity: 1; }}
      50% {{ transform: scale(1.4); opacity: 0.6; }}
    }}

    .header-metrics {{
      display: flex;
      gap: 1.5rem;
      align-items: center;
    }}

    .metric-pill {{
      background: rgba(30, 41, 59, 0.6);
      border: 1px solid var(--border-glass);
      padding: 0.4rem 0.9rem;
      border-radius: 20px;
      display: flex;
      align-items: center;
      gap: 0.6rem;
      font-size: 0.8rem;
      font-family: 'JetBrains Mono', monospace;
    }}

    .metric-pill strong {{
      font-weight: 700;
      color: var(--cyan);
    }}

    .btn-action {{
      background: linear-gradient(135deg, #0284C7, #0369A1);
      border: 1px solid rgba(0, 240, 255, 0.3);
      color: #fff;
      font-weight: 600;
      font-size: 0.8rem;
      padding: 0.55rem 1.1rem;
      border-radius: 8px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.2s ease;
      box-shadow: 0 4px 15px rgba(2, 132, 199, 0.3);
    }}

    .btn-action:hover {{
      transform: translateY(-1px);
      box-shadow: 0 6px 20px rgba(0, 240, 255, 0.5);
      border-color: var(--cyan);
    }}

    /* Main Grid Layout */
    .dashboard-container {{
      display: grid;
      grid-template-columns: 340px 1fr 380px;
      gap: 1.2rem;
      padding: 1.2rem;
      height: calc(100vh - 72px);
    }}

    /* Glass Cards */
    .glass-card {{
      background: var(--bg-card);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid var(--border-glass);
      border-radius: 14px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    }}

    .card-header {{
      padding: 0.85rem 1.1rem;
      background: rgba(30, 41, 59, 0.4);
      border-bottom: 1px solid var(--border-glass);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .card-header h2 {{
      font-size: 0.85rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: var(--slate-300);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .card-body {{
      padding: 1rem;
      overflow-y: auto;
      flex: 1;
    }}

    /* Left Panel: Fleet Matrix */
    .filter-bar {{
      display: flex;
      gap: 0.4rem;
      margin-bottom: 0.8rem;
    }}

    .filter-btn {{
      background: rgba(30, 41, 59, 0.6);
      border: 1px solid var(--border-glass);
      color: var(--slate-400);
      font-size: 0.72rem;
      font-weight: 600;
      padding: 0.35rem 0.65rem;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.2s;
    }}

    .filter-btn.active, .filter-btn:hover {{
      background: rgba(0, 240, 255, 0.15);
      border-color: var(--cyan);
      color: var(--cyan);
    }}

    .engine-list {{
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }}

    .engine-card {{
      background: rgba(30, 41, 59, 0.35);
      border: 1px solid var(--border-glass);
      border-radius: 8px;
      padding: 0.75rem 0.9rem;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      transition: all 0.2s ease;
    }}

    .engine-card:hover {{
      background: rgba(30, 41, 59, 0.7);
      border-color: var(--cyan);
      transform: translateX(4px);
    }}

    .engine-card.active {{
      background: rgba(0, 240, 255, 0.12);
      border-color: var(--cyan);
      box-shadow: 0 0 15px rgba(0, 240, 255, 0.2);
    }}

    .eng-title {{
      font-weight: 700;
      font-size: 0.85rem;
      font-family: 'JetBrains Mono', monospace;
    }}

    .eng-sub {{
      font-size: 0.7rem;
      color: var(--slate-400);
      margin-top: 0.15rem;
    }}

    .status-badge {{
      font-size: 0.68rem;
      font-weight: 700;
      padding: 0.25rem 0.55rem;
      border-radius: 4px;
      font-family: 'JetBrains Mono', monospace;
    }}

    .status-healthy {{
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.4);
      color: var(--emerald);
    }}

    .status-warning {{
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.4);
      color: var(--amber);
    }}

    .status-critical {{
      background: rgba(244, 63, 94, 0.15);
      border: 1px solid rgba(244, 63, 94, 0.4);
      color: var(--rose);
      animation: flashBorder 2s infinite;
    }}

    @keyframes flashBorder {{
      0%, 100% {{ border-color: rgba(244, 63, 94, 0.4); }}
      50% {{ border-color: rgba(244, 63, 94, 1); box-shadow: 0 0 10px rgba(244, 63, 94, 0.5); }}
    }}

    /* Center Panel: Diagnostic Inspector */
    .hero-stat-row {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 0.8rem;
      margin-bottom: 1.2rem;
    }}

    .stat-box {{
      background: rgba(30, 41, 59, 0.4);
      border: 1px solid var(--border-glass);
      border-radius: 10px;
      padding: 0.8rem;
      text-align: center;
    }}

    .stat-label {{
      font-size: 0.7rem;
      color: var(--slate-400);
      text-transform: uppercase;
      font-weight: 600;
    }}

    .stat-val {{
      font-size: 1.4rem;
      font-weight: 800;
      color: var(--cyan);
      margin-top: 0.2rem;
      font-family: 'JetBrains Mono', monospace;
    }}

    .chart-container {{
      background: rgba(30, 41, 59, 0.3);
      border: 1px solid var(--border-glass);
      border-radius: 10px;
      padding: 1rem;
      margin-bottom: 1.2rem;
      position: relative;
    }}

    .chart-header {{
      display: flex;
      justify-content: space-between;
      margin-bottom: 0.8rem;
      font-size: 0.78rem;
      color: var(--slate-400);
    }}

    .telemetry-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 0.8rem;
    }}

    .gauge-card {{
      background: rgba(30, 41, 59, 0.45);
      border: 1px solid var(--border-glass);
      border-radius: 8px;
      padding: 0.75rem;
    }}

    .gauge-title {{
      font-size: 0.7rem;
      color: var(--slate-400);
      font-weight: 600;
      display: flex;
      justify-content: space-between;
    }}

    .gauge-num {{
      font-size: 1.15rem;
      font-weight: 700;
      color: #fff;
      margin-top: 0.3rem;
      font-family: 'JetBrains Mono', monospace;
    }}

    /* Right Panel: Self-Healing Controller */
    .tier-box {{
      background: rgba(30, 41, 59, 0.45);
      border: 1px solid var(--border-glass);
      border-radius: 10px;
      padding: 1rem;
      margin-bottom: 1rem;
    }}

    .tier-box.highlight {{
      border-color: rgba(16, 185, 129, 0.4);
      background: rgba(16, 185, 129, 0.05);
    }}

    .tier-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.75rem;
    }}

    .tier-tag {{
      font-size: 0.7rem;
      font-weight: 800;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      text-transform: uppercase;
      font-family: 'JetBrains Mono', monospace;
    }}

    .tag-soft {{
      background: rgba(16, 185, 129, 0.2);
      color: var(--emerald);
      border: 1px solid rgba(16, 185, 129, 0.4);
    }}

    .tag-hard {{
      background: rgba(244, 63, 94, 0.2);
      color: var(--rose);
      border: 1px solid rgba(244, 63, 94, 0.4);
    }}

    .tier-desc {{
      font-size: 0.75rem;
      color: var(--slate-300);
      line-height: 1.4;
      margin-bottom: 0.8rem;
    }}

    .btn-heal {{
      width: 100%;
      background: linear-gradient(135deg, #10B981, #059669);
      border: 1px solid rgba(16, 185, 129, 0.5);
      color: #fff;
      font-weight: 700;
      font-size: 0.8rem;
      padding: 0.7rem;
      border-radius: 8px;
      cursor: pointer;
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.25s ease;
      box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
    }}

    .btn-heal:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 25px rgba(16, 185, 129, 0.6);
    }}

    .btn-heal.active {{
      background: linear-gradient(135deg, #059669, #047857);
      border-color: #34D399;
    }}

    .btn-inspect-wo {{
      width: 100%;
      background: rgba(30, 41, 59, 0.8);
      border: 1px solid var(--border-glass);
      color: var(--slate-300);
      font-weight: 600;
      font-size: 0.78rem;
      padding: 0.65rem;
      border-radius: 8px;
      cursor: pointer;
      transition: all 0.2s;
      margin-top: 0.5rem;
    }}

    .btn-inspect-wo:hover {{
      background: rgba(51, 65, 85, 0.8);
      color: #fff;
      border-color: var(--cyan);
    }}

    /* Modal for Work Order */
    .modal-overlay {{
      display: none;
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(12px);
      z-index: 200;
      justify-content: center;
      align-items: center;
    }}

    .modal-overlay.open {{
      display: flex;
    }}

    .modal-content {{
      background: #0D1424;
      border: 1px solid var(--cyan);
      box-shadow: 0 0 40px rgba(0, 240, 255, 0.3);
      border-radius: 14px;
      width: 620px;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }}

    .modal-header {{
      padding: 1rem 1.4rem;
      background: rgba(15, 23, 42, 0.8);
      border-bottom: 1px solid var(--border-glass);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .modal-header h3 {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--cyan);
      font-family: 'JetBrains Mono', monospace;
    }}

    .modal-close {{
      background: none;
      border: none;
      color: var(--slate-400);
      font-size: 1.4rem;
      cursor: pointer;
    }}

    .modal-body {{
      padding: 1.2rem;
      overflow-y: auto;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.78rem;
      color: var(--slate-300);
      background: #090E1A;
    }}

    pre {{
      background: rgba(15, 23, 42, 0.6);
      padding: 1rem;
      border-radius: 8px;
      border: 1px solid var(--border-glass);
      overflow-x: auto;
      line-height: 1.4;
    }}

    /* Scrollbars */
    ::-webkit-scrollbar {{
      width: 5px;
      height: 5px;
    }}
    ::-webkit-scrollbar-track {{
      background: rgba(15, 23, 42, 0.5);
    }}
    ::-webkit-scrollbar-thumb {{
      background: rgba(51, 65, 85, 0.6);
      border-radius: 4px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: var(--cyan);
    }}
  </style>
</head>
<body>

  <!-- Top Command Header -->
  <header>
    <div class="brand-section">
      <div class="brand-logo-badge">AERO-SHIELD</div>
      <div class="brand-title">
        <h1>
          <span>Autonomous Connected Fleet Operations</span>
          <span class="live-pulse"></span>
        </h1>
        <p>NASA C-MAPSS FD001 PROGNOSTICS • ZERO-LLM DETERMINISTIC RESILIENCE</p>
      </div>
    </div>

    <div class="header-metrics">
      <div class="metric-pill">FLEET MONITORED: <strong>100 UNITS</strong></div>
      <div class="metric-pill">HEALTHY: <span style="color:var(--emerald); font-weight:700;">81</span></div>
      <div class="metric-pill">WARNING: <span style="color:var(--amber); font-weight:700;">14</span></div>
      <div class="metric-pill">CRITICAL: <span style="color:var(--rose); font-weight:700;">5</span></div>
      <button class="btn-action" onclick="simulateRetraining()">
        <span>⚡</span>
        <span>Run MLOps Drift Check & Retrain</span>
      </button>
    </div>
  </header>

  <!-- 3-Column Master Layout -->
  <main class="dashboard-container">

    <!-- LEFT: Fleet Matrix -->
    <section class="glass-card">
      <div class="card-header">
        <h2><span>🌐</span> Connected Fleet Grid</h2>
        <span id="active-filter-label" style="font-size:0.7rem; color:var(--cyan); font-family:'JetBrains Mono';">ALL (100)</span>
      </div>
      <div class="card-body">
        <div class="filter-bar">
          <button class="filter-btn active" onclick="filterFleet('ALL', this)">ALL (100)</button>
          <button class="filter-btn" onclick="filterFleet('CRITICAL', this)">CRITICAL (5)</button>
          <button class="filter-btn" onclick="filterFleet('WARNING', this)">WARNING (14)</button>
          <button class="filter-btn" onclick="filterFleet('HEALTHY', this)">HEALTHY (81)</button>
        </div>
        <div class="engine-list" id="engine-list-container">
          <!-- Dynamically populated -->
        </div>
      </div>
    </section>

    <!-- CENTER: Selected Unit Deep-Dive Diagnostic Twin -->
    <section class="glass-card">
      <div class="card-header">
        <h2 id="selected-unit-header"><span>✈️</span> Turbofan Unit #002 Prognostics</h2>
        <span id="selected-unit-status-badge" class="status-badge status-warning">WARNING STATE</span>
      </div>
      <div class="card-body">
        
        <!-- KPI Row -->
        <div class="hero-stat-row">
          <div class="stat-box">
            <div class="stat-label">Operating Cycles</div>
            <div class="stat-val" id="stat-cycles">158</div>
          </div>
          <div class="stat-box">
            <div class="stat-label">Predicted RUL</div>
            <div class="stat-val" id="stat-rul" style="color:var(--amber);">33.5 <span style="font-size:0.8rem;">CYC</span></div>
          </div>
          <div class="stat-box">
            <div class="stat-label">True Benchmark</div>
            <div class="stat-val" id="stat-benchmark">30.0 <span style="font-size:0.8rem;">CYC</span></div>
          </div>
          <div class="stat-box">
            <div class="stat-label">Model Residual</div>
            <div class="stat-val" id="stat-residual" style="color:var(--emerald);">+3.5 <span style="font-size:0.8rem;">CYC</span></div>
          </div>
        </div>

        <!-- Dynamic Degradation Trajectory Chart -->
        <div class="chart-container">
          <div class="chart-header">
            <strong>RUL DEGRADATION TRAJECTORY & MITIGATION CURVE</strong>
            <span id="chart-legend-mitigation" style="color:var(--emerald); display:none;">• In-Situ Mitigation: +25 Cycles Gained</span>
          </div>
          <svg id="degradation-svg" viewBox="0 0 600 180" style="width:100%; height:180px; overflow:visible;">
            <!-- Grid Lines -->
            <line x1="50" y1="20" x2="570" y2="20" stroke="rgba(255,255,255,0.06)" stroke-dasharray="4"/>
            <line x1="50" y1="60" x2="570" y2="60" stroke="rgba(255,255,255,0.06)" stroke-dasharray="4"/>
            <line x1="50" y1="100" x2="570" y2="100" stroke="rgba(255,255,255,0.06)" stroke-dasharray="4"/>
            <line x1="50" y1="140" x2="570" y2="140" stroke="rgba(255,255,255,0.06)" stroke-dasharray="4"/>
            
            <!-- Axes Labels -->
            <text x="15" y="24" fill="#64748B" font-size="10" font-family="JetBrains Mono">125</text>
            <text x="25" y="84" fill="#64748B" font-size="10" font-family="JetBrains Mono">60</text>
            <text x="30" y="144" fill="#64748B" font-size="10" font-family="JetBrains Mono">0</text>
            
            <text x="50" y="165" fill="#64748B" font-size="10" font-family="JetBrains Mono">Cycle 0</text>
            <text x="300" y="165" fill="#64748B" font-size="10" font-family="JetBrains Mono">Current Cycle (158)</text>
            <text x="500" y="165" fill="#64748B" font-size="10" font-family="JetBrains Mono">Failure (191)</text>

            <!-- Trajectory Path -->
            <path id="path-history" d="M 50 20 L 220 20 Q 320 60, 360 105" fill="none" stroke="#00F0FF" stroke-width="3"/>
            <!-- Projected Failure Path -->
            <path id="path-projected" d="M 360 105 L 480 140" fill="none" stroke="#F59E0B" stroke-width="2.5" stroke-dasharray="5"/>
            <!-- Counterfactual Soft-Healed Path (Hidden by default) -->
            <path id="path-healed" d="M 360 105 Q 450 115, 550 140" fill="none" stroke="#10B981" stroke-width="3" stroke-dasharray="4" style="display:none;"/>
            
            <!-- Inspection Point Circle -->
            <circle cx="360" cy="105" r="5" fill="#F59E0B" stroke="#fff" stroke-width="2"/>
          </svg>
        </div>

        <!-- Telemetry Gauges -->
        <div class="telemetry-grid">
          <div class="gauge-card">
            <div class="gauge-title"><span>HPC PRESS (s11)</span><span style="color:var(--amber);">+3.8σ</span></div>
            <div class="gauge-num" id="gauge-s11">50.02 <span style="font-size:0.75rem; color:var(--slate-400);">psia</span></div>
          </div>
          <div class="gauge-card">
            <div class="gauge-title"><span>CORE SPEED (s12)</span><span style="color:var(--emerald);">-0.7σ</span></div>
            <div class="gauge-num" id="gauge-s12">518.34 <span style="font-size:0.75rem; color:var(--slate-400);">rpm</span></div>
          </div>
          <div class="gauge-card">
            <div class="gauge-title"><span>EGT TEMP (s4)</span><span id="gauge-s4-stat" style="color:var(--amber);">642°C</span></div>
            <div class="gauge-num" id="gauge-s4">1406.5 <span style="font-size:0.75rem; color:var(--slate-400);">°R</span></div>
          </div>
        </div>

      </div>
    </section>

    <!-- RIGHT: Cyber-Physical Self-Healing Controller -->
    <section class="glass-card">
      <div class="card-header">
        <h2><span>⚡</span> Closed-Loop Controller</h2>
        <span class="status-badge" style="background:rgba(0,240,255,0.15); color:var(--cyan); border:1px solid var(--cyan);">AUTONOMIC FSM</span>
      </div>
      <div class="card-body">
        
        <!-- Tier 1 Soft Healing -->
        <div class="tier-box highlight">
          <div class="tier-header">
            <span class="tier-tag tag-soft">Tier 1: In-Situ Soft Healing</span>
            <span id="tier1-status-pill" style="font-size:0.68rem; color:var(--emerald); font-weight:700;">STANDBY</span>
          </div>
          <div class="tier-desc">
            Autonomous supervisory command issued to engine ECU (FADEC). Modulates throttle limit to reduce thermodynamic stress.
          </div>
          <div style="background:rgba(15,23,42,0.6); padding:0.6rem; border-radius:6px; margin-bottom:0.8rem; font-family:'JetBrains Mono'; font-size:0.75rem;">
            <div>COMMAND: <span id="tier1-cmd-text" style="color:var(--cyan); font-weight:700;">APPLY_OPERATIONAL_DERATE_15PCT</span></div>
            <div style="margin-top:0.2rem; color:var(--slate-400);">EXPECTED GAIN: <strong style="color:var(--emerald);">+25 OPERATING CYCLES</strong></div>
          </div>
          <button class="btn-heal" id="btn-soft-heal" onclick="toggleSoftHealing()">
            <span>⚡</span>
            <span id="heal-btn-label">Apply In-Situ Throttle Derate (-15%)</span>
          </button>
        </div>

        <!-- Tier 2 Prescriptive Hard Healing -->
        <div class="tier-box">
          <div class="tier-header">
            <span class="tier-tag tag-hard">Tier 2: Prescriptive Maintenance</span>
            <span style="font-size:0.68rem; color:var(--slate-400); font-family:'JetBrains Mono';">ISO 55000</span>
          </div>
          <div class="tier-desc">
            Direct orchestration with Computerized Maintenance Management Systems (SAP PM / IBM Maximo). Dispatches parts and bay slots.
          </div>
          <div style="font-size:0.75rem; font-family:'JetBrains Mono'; color:var(--slate-300); line-height:1.6;">
            <div>• WORK ORDER: <span id="wo-id-display" style="color:var(--cyan);">AWO-ELXSI-U002-C0158</span></div>
            <div>• ASSIGNED HUB: <span style="color:#fff;">DEPOT-NORTH-HUB-BAY-3</span></div>
            <div>• SPARE KIT: <span style="color:var(--emerald);">PART-BLADE-HPC-KIT-A</span></div>
            <div>• OBSERVABILITY (DPR): <span style="color:var(--cyan);">0.88 &ge; 0.75 (PASS)</span></div>
          </div>
          <button class="btn-inspect-wo" onclick="openWorkOrderModal()">
            📄 Inspect Automated Work Order Payload
          </button>
        </div>

        <!-- MLOps Summary Box -->
        <div style="background:rgba(30,41,59,0.3); border:1px solid var(--border-glass); border-radius:8px; padding:0.75rem;">
          <div style="font-size:0.7rem; font-weight:700; color:var(--slate-400); text-transform:uppercase; margin-bottom:0.4rem;">
            MLOps Governance State
          </div>
          <div style="display:flex; justify-content:space-between; font-size:0.72rem; font-family:'JetBrains Mono'; color:var(--slate-300);">
            <span>Model: XGBoost-v1.4</span>
            <span style="color:var(--emerald);">RMSE: 18.21 cyc</span>
          </div>
          <div style="display:flex; justify-content:space-between; font-size:0.72rem; font-family:'JetBrains Mono'; color:var(--slate-300); margin-top:0.2rem;">
            <span>NASA Score: 1712.6</span>
            <span style="color:var(--cyan);">KS-Drift: Monitored</span>
          </div>
        </div>

      </div>
    </section>

  </main>

  <!-- Work Order Inspection Modal -->
  <div class="modal-overlay" id="wo-modal">
    <div class="modal-content">
      <div class="modal-header">
        <h3 id="modal-wo-title">AUTOMATED WORK ORDER: AWO-ELXSI-U002-C0158</h3>
        <button class="modal-close" onclick="closeWorkOrderModal()">&times;</button>
      </div>
      <div class="modal-body">
        <pre id="modal-json-content"></pre>
      </div>
    </div>
  </div>

  <script>
    // Embedded Fleet Pipeline Telemetry
    const FLEET_DATA = {fleet_json_str};
    let currentEngine = FLEET_DATA.engines[1] || FLEET_DATA.engines[0];
    let isHealed = false;

    // Initialize UI
    window.addEventListener('DOMContentLoaded', () => {{
      renderEngineList('ALL');
      selectEngine(currentEngine.unit_id);
    }});

    function renderEngineList(filter) {{
      const container = document.getElementById('engine-list-container');
      container.innerHTML = '';
      
      const filtered = FLEET_DATA.engines.filter(e => {{
        if (filter === 'ALL') return true;
        return e.state === filter;
      }});

      filtered.forEach(eng => {{
        const card = document.createElement('div');
        card.className = `engine-card ${{eng.unit_id === currentEngine.unit_id ? 'active' : ''}}`;
        card.onclick = () => selectEngine(eng.unit_id);
        
        let badgeClass = 'status-healthy';
        if (eng.state === 'WARNING') badgeClass = 'status-warning';
        if (eng.state === 'CRITICAL') badgeClass = 'status-critical';

        card.innerHTML = `
          <div>
            <div class="eng-title">ENGINE U-${{String(eng.unit_id).padStart(3, '0')}}</div>
            <div class="eng-sub">Cycle: ${{eng.current_cycle}} • True RUL: ${{eng.true_rul}}</div>
          </div>
          <div style="text-align:right;">
            <div class="status-badge ${{badgeClass}}">${{eng.state}}</div>
            <div style="font-size:0.75rem; font-family:'JetBrains Mono'; margin-top:0.2rem; color:var(--cyan);">
              ${{eng.predicted_rul}} <span style="font-size:0.65rem; color:var(--slate-400);">cyc</span>
            </div>
          </div>
        `;
        container.appendChild(card);
      }});
    }}

    function filterFleet(filter, btn) {{
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      document.getElementById('active-filter-label').innerText = `${{filter}} (${{
        filter === 'ALL' ? FLEET_DATA.engines.length : FLEET_DATA.engines.filter(e => e.state === filter).length
      }})`;
      renderEngineList(filter);
    }}

    function selectEngine(unitId) {{
      currentEngine = FLEET_DATA.engines.find(e => e.unit_id === unitId) || FLEET_DATA.engines[0];
      isHealed = false;
      
      // Update Active Card Highlights
      document.querySelectorAll('.engine-card').forEach(c => c.classList.remove('active'));
      // Find card
      const cards = document.querySelectorAll('.engine-card');
      cards.forEach(c => {{
        if (c.innerHTML.includes(`ENGINE U-${{String(unitId).padStart(3, '0')}}`)) {{
          c.classList.add('active');
        }}
      }});

      // Update Center Deep-Dive
      document.getElementById('selected-unit-header').innerHTML = `<span>✈️</span> Turbofan Unit #${{String(unitId).padStart(3, '0')}} Prognostics`;
      
      const badge = document.getElementById('selected-unit-status-badge');
      badge.className = 'status-badge';
      if (currentEngine.state === 'HEALTHY') {{
        badge.classList.add('status-healthy');
        badge.innerText = 'HEALTHY NOMINAL';
      }} else if (currentEngine.state === 'WARNING') {{
        badge.classList.add('status-warning');
        badge.innerText = 'WARNING: DEGRADING';
      }} else {{
        badge.classList.add('status-critical');
        badge.innerText = 'CRITICAL: DISPATCH REQUIRED';
      }}

      // Stat row
      document.getElementById('stat-cycles').innerText = currentEngine.current_cycle;
      document.getElementById('stat-rul').innerText = currentEngine.predicted_rul + ' CYC';
      document.getElementById('stat-benchmark').innerText = currentEngine.true_rul + ' CYC';
      
      const res = (currentEngine.predicted_rul - currentEngine.true_rul).toFixed(1);
      const resEl = document.getElementById('stat-residual');
      resEl.innerText = (res > 0 ? '+' : '') + res + ' CYC';
      resEl.style.color = Math.abs(res) <= 15 ? 'var(--emerald)' : 'var(--amber)';

      // Telemetry
      if (currentEngine.sensors) {{
        document.getElementById('gauge-s11').innerHTML = (currentEngine.sensors.sensor_11 || 47.45) + ' <span style="font-size:0.75rem; color:var(--slate-400);">psia</span>';
        document.getElementById('gauge-s12').innerHTML = (currentEngine.sensors.sensor_12 || 521.8) + ' <span style="font-size:0.75rem; color:var(--slate-400);">rpm</span>';
        document.getElementById('gauge-s4').innerHTML = (currentEngine.sensors.sensor_4 || 1405.2) + ' <span style="font-size:0.75rem; color:var(--slate-400);">°R</span>';
      }}

      // Controller
      document.getElementById('tier1-cmd-text').innerText = currentEngine.tier1_command;
      document.getElementById('wo-id-display').innerText = currentEngine.work_order_id || 'NO_DISPATCH_REQUIRED';

      // Reset soft heal button
      const healBtn = document.getElementById('btn-soft-heal');
      const healPill = document.getElementById('tier1-status-pill');
      const healedPath = document.getElementById('path-healed');
      const legend = document.getElementById('chart-legend-mitigation');

      healBtn.classList.remove('active');
      healBtn.innerHTML = `<span>⚡</span><span>Apply In-Situ Throttle Derate (-15%)</span>`;
      healPill.innerText = currentEngine.state === 'HEALTHY' ? 'NOMINAL' : 'READY TO TRIGGER';
      healedPath.style.display = 'none';
      legend.style.display = 'none';
      document.getElementById('gauge-s4-stat').innerText = '642°C';
      document.getElementById('gauge-s4-stat').style.color = currentEngine.state === 'CRITICAL' ? 'var(--rose)' : 'var(--amber)';
    }}

    function toggleSoftHealing() {{
      isHealed = !isHealed;
      const healBtn = document.getElementById('btn-soft-heal');
      const healPill = document.getElementById('tier1-status-pill');
      const healedPath = document.getElementById('path-healed');
      const legend = document.getElementById('chart-legend-mitigation');
      const rulStat = document.getElementById('stat-rul');
      const tempStat = document.getElementById('gauge-s4-stat');

      if (isHealed) {{
        healBtn.classList.add('active');
        healBtn.innerHTML = `<span>✔</span><span>In-Situ Throttle Derate Active (85%)</span>`;
        healPill.innerText = 'MITIGATING IN FLIGHT';
        healedPath.style.display = 'block';
        legend.style.display = 'inline';
        
        // Show life extension effect
        const extendedRul = (currentEngine.predicted_rul + 25.0).toFixed(1);
        rulStat.innerHTML = `${{extendedRul}} <span style="font-size:0.8rem; color:var(--emerald);">(+25 Gained)</span>`;
        tempStat.innerText = '602°C (-40°C)';
        tempStat.style.color = 'var(--emerald)';
      }} else {{
        selectEngine(currentEngine.unit_id);
      }}
    }}

    function openWorkOrderModal() {{
      const modal = document.getElementById('wo-modal');
      const pre = document.getElementById('modal-json-content');
      document.getElementById('modal-wo-title').innerText = `AUTOMATED WORK ORDER: ${{currentEngine.work_order_id || 'AWO-PREVIEW'}}`;

      const samplePayload = {{
        "work_order_id": currentEngine.work_order_id || `AWO-ELXSI-U${{String(currentEngine.unit_id).padStart(3, '0')}}-C${{currentEngine.current_cycle}}`,
        "standard_compliance": "ISO 55000 / MIMOSA-OSA-EAI",
        "asset_metadata": {{
          "unit_id": currentEngine.unit_id,
          "asset_class": "Turbofan Engine (C-MAPSS Class)",
          "current_flight_cycle": currentEngine.current_cycle,
          "predicted_remaining_useful_life": currentEngine.predicted_rul,
          "severity_rank": currentEngine.state === "CRITICAL" ? 1 : 2
        }},
        "tier_1_in_situ_remediation": {{
          "command": currentEngine.tier1_command,
          "throttle_resolver_limit": "85.0%",
          "core_temperature_reduction_c": 40.0,
          "projected_cycle_extension": 25.0
        }},
        "tier_2_prescriptive_maintenance": {{
          "recommended_action": currentEngine.state === "CRITICAL" ? "BORESCOPE_INSPECT_AND_OVERHAUL_HPC" : "SCHEDULE_DEPOT_LUBRICATION",
          "target_depot": "DEPOT-NORTH-HUB-BAY-3",
          "reserved_spare_kits": ["PART-BLADE-HPC-KIT-A", "PART-SEAL-CORE-04"],
          "diagnostic_preservation_ratio_dpr": 0.88,
          "estimated_bay_hours": currentEngine.state === "CRITICAL" ? 14.5 : 4.0
        }},
        "automation_metadata": {{
          "agent_type": "Deterministic Rule-Based FSM (Non-LLM)",
          "turnaround_latency_ms": 412,
          "human_exception_required": false
        }}
      }};

      pre.innerText = JSON.stringify(samplePayload, null, 2);
      modal.classList.add('open');
    }}

    function closeWorkOrderModal() {{
      document.getElementById('wo-modal').classList.remove('open');
    }}

    function simulateRetraining() {{
      alert("[MLOps Retraining Flow Dispatched]\\n\\nKolmogorov-Smirnov feature drift check: PSI = 0.31 > 0.25.\\nInitiated automated challenger model training on incoming 15-cycle batch.\\nChallenger backtest RMSE: 17.8 cycles (Beats Champion: 18.21 cycles).\\nPromoted to Production Registry with zero human manual intervention.");
    }}
  </script>
</body>
</html>
"""

    with open(out_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"[SUCCESS] Standalone Glassmorphic Prototype compiled at: {out_html_path}")

if __name__ == "__main__":
    build_prototype_html()
