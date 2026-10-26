"""
Comprehensive Builder for the Light-Themed Glassmorphic AERO-SHIELD Web Application.
Fully Interactive & Dynamic Architecture:
- Every button, slider, and control triggers authentic DOM/state mutations.
- Live MLOps Autonomous Retraining Runner modal with step-by-step console streaming & metric mutations.
- Interactive Throttle Physics Engine: range slider dynamically recomputes aerothermal temperature drop (-40°C to -80°C), mechanical stress reduction (-25% to -50%), RUL cycle gains (+25 to +50 cycles), and dynamically redraws the SVG curve in real time.
- Fully functional ISO 55000 Work Order modal with authentic file download (Blob), simulated SAP/Maximo CMMS dispatch (HTTP 201), and clipboard copy.
- Live Telemetry Stream simulation with Gaussian sensor jitter and streaming event log.
- Full multi-tab navigation: Fleet Grid, Diagnostic Twin, Control Room, MLOps Registry, Work Orders.
- Glassmorphic White & Clean Light Theme (Emerald Green, Amber Yellow, Rose Red, Sky Blue).
"""
import os
import json

def generate_light_prototype():
    prototype_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(prototype_dir)
    fleet_json_path = os.path.join(project_root, "reports", "fleet_status.json")
    
    if os.path.exists(fleet_json_path):
        with open(fleet_json_path, "r", encoding="utf-8") as f:
            fleet_data = json.load(f)
    else:
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

    html_code = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AERO-SHIELD // Connected Fleet Prognostics & Self-Healing Operations</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-body: #F8FAFC;
      --bg-surface: #FFFFFF;
      --bg-glass: rgba(255, 255, 255, 0.88);
      --bg-glass-card: rgba(255, 255, 255, 0.94);
      --border-light: #E2E8F0;
      --border-card: rgba(226, 232, 240, 0.90);
      --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.05);
      --shadow-md: 0 4px 15px rgba(0, 0, 0, 0.05);
      --shadow-lg: 0 10px 30px rgba(0, 0, 0, 0.07);
      --shadow-glass: 0 16px 40px rgba(15, 23, 42, 0.12);

      /* Semantic Light Accents */
      --green-main: #059669;
      --green-bg: #ECFDF5;
      --green-border: #A7F3D0;
      --green-text: #065F46;

      --yellow-main: #D97706;
      --yellow-bg: #FFFBEB;
      --yellow-border: #FDE68A;
      --yellow-text: #92400E;

      --red-main: #DC2626;
      --red-bg: #FEF2F2;
      --red-border: #FECACA;
      --red-text: #991B1B;

      --blue-main: #0284C7;
      --blue-bg: #F0F9FF;
      --blue-border: #BAE6FD;
      --blue-text: #075985;

      --text-dark: #0F172A;
      --text-muted: #64748B;
      --text-sub: #94A3B8;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-body);
      color: var(--text-dark);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
      background-image: 
        radial-gradient(circle at 12% 10%, rgba(2, 132, 199, 0.05) 0%, transparent 35%),
        radial-gradient(circle at 88% 15%, rgba(16, 185, 129, 0.05) 0%, transparent 40%),
        radial-gradient(circle at 50% 90%, rgba(217, 119, 6, 0.04) 0%, transparent 50%);
      background-attachment: fixed;
    }}

    /* Global Navigation Bar */
    header {{
      background: var(--bg-glass);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border-bottom: 1px solid var(--border-light);
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: var(--shadow-sm);
    }}

    .top-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0.85rem 2rem;
      border-bottom: 1px solid rgba(226, 232, 240, 0.6);
    }}

    .brand-group {{
      display: flex;
      align-items: center;
      gap: 1.2rem;
    }}

    .brand-badge {{
      background: linear-gradient(135deg, #0284C7, #0369A1);
      color: #fff;
      font-weight: 800;
      font-size: 1.15rem;
      padding: 0.4rem 0.85rem;
      border-radius: 8px;
      letter-spacing: -0.5px;
      box-shadow: 0 4px 12px rgba(2, 132, 199, 0.25);
    }}

    .brand-meta h1 {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text-dark);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .brand-meta p {{
      font-size: 0.72rem;
      color: var(--text-muted);
      font-family: 'JetBrains Mono', monospace;
    }}

    .pulse-dot {{
      display: inline-block;
      width: 8px;
      height: 8px;
      background-color: var(--green-main);
      border-radius: 50%;
      box-shadow: 0 0 8px var(--green-main);
      animation: pulse 1.8s infinite;
    }}

    @keyframes pulse {{
      0%, 100% {{ transform: scale(1); opacity: 1; }}
      50% {{ transform: scale(1.3); opacity: 0.6; }}
    }}

    .top-controls {{
      display: flex;
      align-items: center;
      gap: 1rem;
    }}

    .stream-toggle {{
      background: var(--blue-bg);
      border: 1px solid var(--blue-border);
      color: var(--blue-text);
      font-size: 0.78rem;
      font-weight: 600;
      padding: 0.5rem 1rem;
      border-radius: 20px;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      cursor: pointer;
      transition: all 0.2s;
    }}

    .stream-toggle:hover {{
      background: #E0F2FE;
      transform: translateY(-1px);
    }}

    .stream-toggle.active {{
      background: var(--green-bg);
      border-color: var(--green-border);
      color: var(--green-text);
      box-shadow: 0 0 10px rgba(16, 185, 129, 0.3);
    }}

    /* Main Tab Navigation */
    nav.tab-nav {{
      display: flex;
      gap: 2rem;
      padding: 0 2rem;
      background: rgba(255, 255, 255, 0.7);
    }}

    .nav-tab {{
      padding: 0.85rem 0.2rem;
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--text-muted);
      border-bottom: 2px solid transparent;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.2s;
    }}

    .nav-tab:hover {{
      color: var(--blue-main);
    }}

    .nav-tab.active {{
      color: var(--blue-main);
      border-bottom-color: var(--blue-main);
      font-weight: 700;
    }}

    .nav-count {{
      background: var(--border-light);
      padding: 0.15rem 0.45rem;
      border-radius: 10px;
      font-size: 0.7rem;
      font-family: 'JetBrains Mono', monospace;
    }}

    /* Content Area */
    main.view-container {{
      flex: 1;
      padding: 1.5rem 2rem;
      max-width: 1600px;
      margin: 0 auto;
      width: 100%;
    }}

    .tab-content {{
      display: none;
    }}

    .tab-content.active {{
      display: block;
      animation: fadeIn 0.25s ease-out;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Glassmorphic White Cards */
    .glass-card {{
      background: var(--bg-glass-card);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid var(--border-card);
      border-radius: 14px;
      box-shadow: var(--shadow-md);
      overflow: hidden;
      margin-bottom: 1.5rem;
    }}

    .card-header {{
      padding: 1rem 1.4rem;
      background: rgba(248, 250, 252, 0.85);
      border-bottom: 1px solid var(--border-light);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .card-header h2 {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text-dark);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .card-body {{
      padding: 1.4rem;
    }}

    /* Fleet KPI Banner */
    .kpi-grid {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 1.2rem;
      margin-bottom: 1.5rem;
    }}

    .kpi-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-light);
      border-radius: 12px;
      padding: 1.1rem 1.2rem;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      position: relative;
      overflow: hidden;
      transition: all 0.2s;
    }}

    .kpi-card:hover {{
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
    }}

    .kpi-card::before {{
      content: '';
      position: absolute;
      top: 0; left: 0; bottom: 0;
      width: 4px;
      background: var(--border-light);
    }}

    .kpi-card.green::before {{ background: var(--green-main); }}
    .kpi-card.amber::before {{ background: var(--yellow-main); }}
    .kpi-card.red::before {{ background: var(--red-main); }}
    .kpi-card.blue::before {{ background: var(--blue-main); }}

    .kpi-label {{
      font-size: 0.75rem;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .kpi-val {{
      font-size: 1.75rem;
      font-weight: 800;
      color: var(--text-dark);
      margin-top: 0.35rem;
      font-family: 'JetBrains Mono', monospace;
    }}

    .kpi-sub {{
      font-size: 0.72rem;
      color: var(--text-muted);
      margin-top: 0.2rem;
    }}

    /* Fleet Grid & Search */
    .filter-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1.2rem;
      gap: 1rem;
      flex-wrap: wrap;
    }}

    .filter-pills {{
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
    }}

    .pill-btn {{
      background: var(--bg-surface);
      border: 1px solid var(--border-light);
      color: var(--text-muted);
      font-size: 0.8rem;
      font-weight: 600;
      padding: 0.45rem 0.9rem;
      border-radius: 8px;
      cursor: pointer;
      transition: all 0.2s;
    }}

    .pill-btn:hover, .pill-btn.active {{
      background: #F1F5F9;
      color: var(--text-dark);
      border-color: #CBD5E1;
    }}

    .pill-btn.active.green {{ background: var(--green-bg); color: var(--green-text); border-color: var(--green-border); }}
    .pill-btn.active.amber {{ background: var(--yellow-bg); color: var(--yellow-text); border-color: var(--yellow-border); }}
    .pill-btn.active.red {{ background: var(--red-bg); color: var(--red-text); border-color: var(--red-border); }}

    .search-sort-group {{
      display: flex;
      align-items: center;
      gap: 0.8rem;
    }}

    .search-box {{
      background: var(--bg-surface);
      border: 1px solid var(--border-light);
      padding: 0.45rem 0.9rem;
      border-radius: 8px;
      font-size: 0.8rem;
      font-family: inherit;
      width: 220px;
      outline: none;
    }}

    .search-box:focus {{
      border-color: var(--blue-main);
      box-shadow: 0 0 0 2px var(--blue-border);
    }}

    .sort-select {{
      background: var(--bg-surface);
      border: 1px solid var(--border-light);
      padding: 0.45rem 0.8rem;
      border-radius: 8px;
      font-size: 0.8rem;
      font-family: inherit;
      color: var(--text-dark);
      outline: none;
      cursor: pointer;
    }}

    .engine-cards-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 1rem;
      max-height: 580px;
      overflow-y: auto;
      padding-right: 0.5rem;
    }}

    .engine-tile {{
      background: var(--bg-surface);
      border: 1px solid var(--border-light);
      border-radius: 10px;
      padding: 1rem;
      cursor: pointer;
      transition: all 0.2s ease;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
    }}

    .engine-tile:hover {{
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
      border-color: var(--blue-main);
    }}

    .engine-tile.active {{
      border-color: var(--blue-main);
      box-shadow: 0 0 0 2px var(--blue-border);
      background: #F8FAFC;
    }}

    .tile-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .tile-id {{
      font-weight: 700;
      font-size: 0.9rem;
      font-family: 'JetBrains Mono', monospace;
    }}

    .badge {{
      font-size: 0.68rem;
      font-weight: 700;
      padding: 0.2rem 0.5rem;
      border-radius: 6px;
      font-family: 'JetBrains Mono', monospace;
    }}

    .badge.HEALTHY {{ background: var(--green-bg); color: var(--green-text); border: 1px solid var(--green-border); }}
    .badge.WARNING {{ background: var(--yellow-bg); color: var(--yellow-text); border: 1px solid var(--yellow-border); }}
    .badge.CRITICAL {{ background: var(--red-bg); color: var(--red-text); border: 1px solid var(--red-border); }}

    .tile-stats {{
      display: flex;
      justify-content: space-between;
      font-size: 0.75rem;
      color: var(--text-muted);
      font-family: 'JetBrains Mono', monospace;
    }}

    .progress-bar-wrap {{
      background: #F1F5F9;
      height: 6px;
      border-radius: 3px;
      overflow: hidden;
    }}

    .progress-bar {{
      height: 100%;
      border-radius: 3px;
      transition: width 0.3s;
    }}

    .progress-bar.HEALTHY {{ background: var(--green-main); }}
    .progress-bar.WARNING {{ background: var(--yellow-main); }}
    .progress-bar.CRITICAL {{ background: var(--red-main); }}

    /* Layout: 2-Column Inspector (Tab 2) */
    .inspector-layout {{
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 1.5rem;
    }}

    .telemetry-row {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1rem;
      margin-bottom: 1.2rem;
    }}

    .dial-card {{
      background: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: 10px;
      padding: 0.9rem;
      box-shadow: var(--shadow-sm);
      transition: all 0.2s;
    }}

    .dial-label {{
      font-size: 0.72rem;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      display: flex;
      justify-content: space-between;
    }}

    .dial-val {{
      font-size: 1.3rem;
      font-weight: 800;
      margin-top: 0.3rem;
      font-family: 'JetBrains Mono', monospace;
    }}

    /* Self-Healing Lab Controls (Tab 3) */
    .healing-split {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.5rem;
    }}

    .tier-box {{
      background: var(--bg-surface);
      border: 1px solid var(--border-light);
      border-radius: 12px;
      padding: 1.4rem;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }}

    .tier-box.active-tier {{
      border-color: var(--green-border);
      background: #FAFDFB;
      box-shadow: 0 4px 20px rgba(16, 185, 129, 0.08);
    }}

    .tier-tag {{
      display: inline-block;
      font-size: 0.72rem;
      font-weight: 800;
      padding: 0.25rem 0.6rem;
      border-radius: 6px;
      text-transform: uppercase;
      font-family: 'JetBrains Mono', monospace;
      width: fit-content;
    }}

    .tag-soft {{ background: var(--green-bg); color: var(--green-text); border: 1px solid var(--green-border); }}
    .tag-hard {{ background: var(--red-bg); color: var(--red-text); border: 1px solid var(--red-border); }}

    .tier-title {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-dark);
    }}

    .tier-desc {{
      font-size: 0.8rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    .slider-row {{
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
    }}

    .slider-header {{
      display: flex;
      justify-content: space-between;
      font-size: 0.75rem;
      font-weight: 600;
      font-family: 'JetBrains Mono', monospace;
    }}

    input[type="range"] {{
      width: 100%;
      height: 8px;
      background: #E2E8F0;
      border-radius: 4px;
      outline: none;
      accent-color: var(--green-main);
      cursor: pointer;
    }}

    .btn-primary {{
      background: linear-gradient(135deg, #059669, #047857);
      color: #fff;
      font-weight: 700;
      font-size: 0.85rem;
      padding: 0.75rem 1.2rem;
      border-radius: 8px;
      border: none;
      cursor: pointer;
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.2s;
      box-shadow: 0 4px 12px rgba(5, 150, 105, 0.2);
    }}

    .btn-primary:hover {{
      transform: translateY(-1px);
      box-shadow: 0 6px 16px rgba(5, 150, 105, 0.35);
    }}

    .btn-primary.derate-inactive {{
      background: linear-gradient(135deg, #64748B, #475569);
      box-shadow: 0 4px 12px rgba(100, 116, 139, 0.2);
    }}

    .btn-secondary {{
      background: var(--bg-surface);
      border: 1px solid var(--border-light);
      color: var(--text-dark);
      font-weight: 600;
      font-size: 0.8rem;
      padding: 0.65rem 1.1rem;
      border-radius: 8px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      transition: all 0.2s;
    }}

    .btn-secondary:hover {{
      background: #F1F5F9;
      border-color: #CBD5E1;
      transform: translateY(-1px);
    }}

    /* Table Styles */
    table.data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.8rem;
    }}

    table.data-table th {{
      text-align: left;
      padding: 0.75rem 1rem;
      background: #F8FAFC;
      color: var(--text-muted);
      font-weight: 600;
      border-bottom: 1px solid var(--border-light);
    }}

    table.data-table td {{
      padding: 0.75rem 1rem;
      border-bottom: 1px solid var(--border-light);
      color: var(--text-dark);
      font-family: 'JetBrains Mono', monospace;
    }}

    table.data-table tr:hover td {{
      background: #F8FAFC;
    }}

    /* Modals */
    .modal-backdrop {{
      display: none;
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(15, 23, 42, 0.5);
      backdrop-filter: blur(8px);
      z-index: 200;
      justify-content: center;
      align-items: center;
      padding: 1rem;
    }}

    .modal-backdrop.open {{
      display: flex;
      animation: modalFadeIn 0.2s ease-out;
    }}

    @keyframes modalFadeIn {{
      from {{ opacity: 0; transform: scale(0.96); }}
      to {{ opacity: 1; transform: scale(1); }}
    }}

    .modal-window {{
      background: #FFFFFF;
      border-radius: 14px;
      box-shadow: var(--shadow-glass);
      width: 720px;
      max-width: 95vw;
      max-height: 88vh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      border: 1px solid var(--border-light);
    }}

    .modal-head {{
      padding: 1.1rem 1.5rem;
      background: #F8FAFC;
      border-bottom: 1px solid var(--border-light);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .modal-head h3 {{
      font-size: 1rem;
      font-weight: 700;
      color: var(--text-dark);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .modal-body-content {{
      padding: 1.4rem;
      overflow-y: auto;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.78rem;
      background: #FAFAFA;
      color: #1E293B;
      line-height: 1.5;
    }}

    .modal-footer {{
      padding: 1rem 1.5rem;
      background: #F8FAFC;
      border-top: 1px solid var(--border-light);
      display: flex;
      justify-content: flex-end;
      gap: 0.8rem;
      align-items: center;
    }}

    pre {{
      background: #F1F5F9;
      padding: 1rem;
      border-radius: 8px;
      border: 1px solid var(--border-light);
      overflow-x: auto;
      white-space: pre-wrap;
    }}

    /* Toast Notification System */
    #toast-container {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 999;
      display: flex;
      flex-direction: column;
      gap: 10px;
      pointer-events: none;
    }}

    .toast {{
      background: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: 10px;
      padding: 1rem 1.2rem;
      box-shadow: 0 10px 25px rgba(15, 23, 42, 0.12);
      display: flex;
      align-items: flex-start;
      gap: 0.8rem;
      min-width: 320px;
      max-width: 440px;
      pointer-events: auto;
      animation: slideInRight 0.3s ease-out;
      border-left: 4px solid var(--blue-main);
    }}

    .toast.success {{ border-left-color: var(--green-main); }}
    .toast.warning {{ border-left-color: var(--yellow-main); }}
    .toast.danger {{ border-left-color: var(--red-main); }}

    .toast-icon {{ font-size: 1.2rem; }}
    .toast-content {{ flex: 1; }}
    .toast-title {{ font-weight: 700; font-size: 0.85rem; color: var(--text-dark); margin-bottom: 0.2rem; }}
    .toast-msg {{ font-size: 0.75rem; color: var(--text-muted); line-height: 1.4; }}

    @keyframes slideInRight {{
      from {{ transform: translateX(100%); opacity: 0; }}
      to {{ transform: translateX(0); opacity: 1; }}
    }}

    /* Retraining Console Styling */
    .console-box {{
      background: #0F172A;
      color: #38BDF8;
      border-radius: 8px;
      padding: 1rem;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      height: 240px;
      overflow-y: auto;
      line-height: 1.6;
      box-shadow: inset 0 2px 6px rgba(0, 0, 0, 0.5);
    }}

    .console-line {{ margin-bottom: 4px; }}
    .console-line.success {{ color: #4ADE80; font-weight: bold; }}
    .console-line.warn {{ color: #FBBF24; }}
    .console-line.head {{ color: #F472B6; font-weight: bold; }}

    /* Custom Scrollbars */
    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: #F1F5F9;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #CBD5E1;
      border-radius: 3px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #94A3B8;
    }}
  </style>
</head>
<body>

  <!-- Top Glass Header -->
  <header>
    <div class="top-bar">
      <div class="brand-group">
        <div class="brand-badge">AERO-SHIELD</div>
        <div class="brand-meta">
          <h1>
            <span>Connected Fleet Cyber-Physical Operations</span>
            <span class="pulse-dot"></span>
          </h1>
          <p>TATA ELXSI TELIPORT S4 • NASA C-MAPSS PROGNOSTICS • ZERO-LLM CLOSED-LOOP AUTONOMICS</p>
        </div>
      </div>

      <div class="top-controls">
        <button class="stream-toggle" id="btn-stream-toggle" onclick="toggleStreamSimulation()">
          <span id="stream-icon">▶</span>
          <span id="stream-label">Simulate Real-Time Telemetry</span>
        </button>
        <button class="btn-primary" style="padding:0.5rem 1.1rem; font-size:0.78rem;" onclick="triggerMLOpsRetrain()">
          <span>⚡</span>
          <span>Trigger MLOps Retrain Run</span>
        </button>
      </div>
    </div>

    <!-- Multi-View Navigation Bar -->
    <nav class="tab-nav">
      <div class="nav-tab active" onclick="switchTab('tab-fleet', this)">
        <span>🌐</span>
        <span>Fleet Command Grid</span>
        <span class="nav-count">100 Units</span>
      </div>
      <div class="nav-tab" onclick="switchTab('tab-inspector', this)">
        <span>✈️</span>
        <span id="tab-inspector-title">Engine Diagnostic Twin (#002)</span>
      </div>
      <div class="nav-tab" onclick="switchTab('tab-healing', this)">
        <span>⚡</span>
        <span>Self-Healing Control Room</span>
        <span class="nav-count" id="nav-healing-count" style="background:#ECFDF5; color:#065F46;">Tier 1 Active</span>
      </div>
      <div class="nav-tab" onclick="switchTab('tab-mlops', this)">
        <span>📊</span>
        <span>MLOps & Governance Registry</span>
        <span class="nav-count" id="nav-mlops-count" style="background:#F0F9FF; color:#075985;">RMSE 18.21</span>
      </div>
      <div class="nav-tab" onclick="switchTab('tab-audit', this)">
        <span>📋</span>
        <span>Work Orders & Audit Trail</span>
        <span class="nav-count" style="background:#FEF2F2; color:#991B1B;">19 Dispatched</span>
      </div>
    </nav>
  </header>

  <!-- Main View Container -->
  <main class="view-container">

    <!-- ================================================================= -->
    <!-- TAB 1: FLEET COMMAND GRID                                         -->
    <!-- ================================================================= -->
    <div id="tab-fleet" class="tab-content active">
      
      <!-- Top 5 Executive Metric Cards -->
      <div class="kpi-grid">
        <div class="kpi-card blue">
          <div class="kpi-label">Total Connected Fleet</div>
          <div class="kpi-val">100 <span style="font-size:0.9rem; color:var(--text-muted);">Units</span></div>
          <div class="kpi-sub">NASA C-MAPSS Turbofan Fleet</div>
        </div>
        <div class="kpi-card green">
          <div class="kpi-label">Nominal (Healthy)</div>
          <div class="kpi-val" style="color:var(--green-main);">81 <span style="font-size:0.9rem;">Units</span></div>
          <div class="kpi-sub">RUL &gt; 35 Flight Cycles</div>
        </div>
        <div class="kpi-card amber">
          <div class="kpi-label">Degraded (Warning)</div>
          <div class="kpi-val" style="color:var(--yellow-main);">14 <span style="font-size:0.9rem;">Units</span></div>
          <div class="kpi-sub">Soft Derate Active (+25 Cyc)</div>
        </div>
        <div class="kpi-card red">
          <div class="kpi-label">Critical (Imminent)</div>
          <div class="kpi-val" style="color:var(--red-main);">5 <span style="font-size:0.9rem;">Units</span></div>
          <div class="kpi-sub">RUL &le; 15 Cycles (Grounding)</div>
        </div>
        <div class="kpi-card blue">
          <div class="kpi-label">Work Orders Raised</div>
          <div class="kpi-val" style="color:var(--blue-main);">19 <span style="font-size:0.9rem;">Orders</span></div>
          <div class="kpi-sub">100% Autonomous Zero-LLM</div>
        </div>
      </div>

      <!-- Fleet Grid Section -->
      <div class="glass-card">
        <div class="card-header">
          <h2><span>🌐</span> Connected Machine Grid (100 Active Aircraft Engines)</h2>
          <span style="font-size:0.8rem; color:var(--text-muted); font-family:'JetBrains Mono';">Click any engine tile to inspect diagnostic twin</span>
        </div>
        <div class="card-body">
          <div class="filter-row">
            <div class="filter-pills">
              <button class="pill-btn active" onclick="filterFleet('ALL', this)">ALL FLEET (100)</button>
              <button class="pill-btn green" onclick="filterFleet('HEALTHY', this)">🟢 HEALTHY (81)</button>
              <button class="pill-btn amber" onclick="filterFleet('WARNING', this)">🟡 WARNING (14)</button>
              <button class="pill-btn red" onclick="filterFleet('CRITICAL', this)">🔴 CRITICAL (5)</button>
            </div>
            
            <div class="search-sort-group">
              <input type="text" class="search-box" id="engine-search" placeholder="🔍 Search Engine ID..." oninput="onSearchInput(this.value)">
              <select class="sort-select" id="fleet-sort-select" onchange="onSortChange(this.value)">
                <option value="RUL_ASC">Sort: RUL (Lowest First)</option>
                <option value="RUL_DESC">Sort: RUL (Highest First)</option>
                <option value="UNIT_ASC">Sort: Engine ID (1 &rarr; 100)</option>
                <option value="CYCLE_DESC">Sort: Cycle (Highest First)</option>
              </select>
            </div>
          </div>

          <!-- Cards Grid -->
          <div class="engine-cards-grid" id="engine-tiles-container">
            <!-- Populated via JavaScript -->
          </div>
        </div>
      </div>

    </div>

    <!-- ================================================================= -->
    <!-- TAB 2: ENGINE DIAGNOSTIC TWIN & SENSORS                           -->
    <!-- ================================================================= -->
    <div id="tab-inspector" class="tab-content">
      <div class="inspector-layout">
        
        <!-- Left: Diagnostic Charts & Sensors -->
        <div>
          <!-- 4 Telemetry Dials -->
          <div class="telemetry-row">
            <div class="dial-card" id="card-dial-s11">
              <div class="dial-label"><span>HPC PRESSURE (s11)</span> <span style="color:var(--yellow-main);" id="badge-s11">DEVIATION</span></div>
              <div class="dial-val" id="dial-s11" style="color:var(--yellow-main);">50.02 <span style="font-size:0.75rem; color:var(--text-muted);">psia</span></div>
            </div>
            <div class="dial-card" id="card-dial-s12">
              <div class="dial-label"><span>CORE SPEED (s12)</span> <span style="color:var(--green-main);" id="badge-s12">STABLE</span></div>
              <div class="dial-val" id="dial-s12" style="color:var(--green-main);">518.34 <span style="font-size:0.75rem; color:var(--text-muted);">rpm</span></div>
            </div>
            <div class="dial-card" id="card-dial-s4">
              <div class="dial-label"><span>EGT TEMP (s4)</span> <span id="dial-s4-badge" style="color:var(--green-main); font-weight:700;">602°C (-40°C)</span></div>
              <div class="dial-val" id="dial-s4" style="color:var(--text-dark);">1406.47 <span style="font-size:0.75rem; color:var(--text-muted);">°R</span></div>
            </div>
            <div class="dial-card" id="card-dial-s2">
              <div class="dial-label"><span>LP SPOOL (s2)</span> <span style="color:var(--blue-main);" id="badge-s2">NOMINAL</span></div>
              <div class="dial-val" id="dial-s2" style="color:var(--blue-main);">646.85 <span style="font-size:0.75rem; color:var(--text-muted);">°R</span></div>
            </div>
          </div>

          <!-- Live SVG Degradation Curve -->
          <div class="glass-card">
            <div class="card-header">
              <h2><span>📈</span> Remaining Useful Life (RUL) Prognosis Trajectory</h2>
              <div style="font-size:0.75rem; font-family:'JetBrains Mono'; display:flex; gap:1.2rem;">
                <span style="color:var(--blue-main);">● Historical Trajectory</span>
                <span style="color:var(--yellow-main);">● Unmitigated Decay</span>
                <span style="color:var(--green-main); font-weight:700;" id="svg-legend-mitigated">● Mitigated (+25 Cyc)</span>
              </div>
            </div>
            <div class="card-body">
              <svg id="trajectory-svg" viewBox="0 0 700 220" style="width:100%; height:220px; overflow:visible;">
                <!-- Grid Lines -->
                <line x1="60" y1="30" x2="660" y2="30" stroke="#E2E8F0" stroke-dasharray="3"/>
                <line x1="60" y1="80" x2="660" y2="80" stroke="#E2E8F0" stroke-dasharray="3"/>
                <line x1="60" y1="130" x2="660" y2="130" stroke="#E2E8F0" stroke-dasharray="3"/>
                <line x1="60" y1="180" x2="660" y2="180" stroke="#CBD5E1"/>

                <!-- Axis Labels -->
                <text x="25" y="34" fill="#64748B" font-size="11" font-family="JetBrains Mono">125</text>
                <text x="32" y="105" fill="#64748B" font-size="11" font-family="JetBrains Mono">60</text>
                <text x="40" y="184" fill="#64748B" font-size="11" font-family="JetBrains Mono">0</text>
                
                <text x="60" y="202" fill="#64748B" font-size="11" font-family="JetBrains Mono">Cycle 0</text>
                <text x="360" y="202" fill="#0284C7" font-weight="700" font-size="11" font-family="JetBrains Mono" id="svg-current-cycle-label">Cycle 158 (Current)</text>
                <text x="560" y="202" fill="#64748B" font-size="11" font-family="JetBrains Mono" id="svg-fail-point-label">Failure Point (Base)</text>

                <!-- Paths -->
                <path d="M 60 30 L 250 30 Q 360 80, 420 140" fill="none" stroke="#0284C7" stroke-width="3"/>
                <path d="M 420 140 L 560 180" fill="none" stroke="#F59E0B" stroke-width="2.5" stroke-dasharray="5"/>
                <path id="svg-mitigated-path" d="M 420 140 Q 520 150, 650 180" fill="none" stroke="#059669" stroke-width="3.5" stroke-dasharray="4"/>

                <circle id="svg-current-dot" cx="420" cy="140" r="6" fill="#F59E0B" stroke="#fff" stroke-width="2"/>
              </svg>
            </div>
          </div>

          <!-- Real-Time Telemetry Event Log -->
          <div class="glass-card">
            <div class="card-header">
              <h2><span>📡</span> Live Edge Telemetry Stream & Inference Ticker</h2>
              <span id="stream-status-badge" style="font-size:0.75rem; font-family:'JetBrains Mono'; color:var(--text-muted);">STREAM STANDBY</span>
            </div>
            <div class="card-body">
              <div class="console-box" id="telemetry-stream-console">
                <div class="console-line head">// AERO-SHIELD Edge Ingestion Socket: listening on UDP port 5055...</div>
                <div class="console-line">[14:22:01.402] PKT-IN: U-002 | Cycle 158 | S11=50.02 psia, S12=518.34 rpm, S4=1406.47 °R | Status: STREAM_READY</div>
                <div class="console-line warn">[14:22:01.405] INFERENCE: Predicted RUL = 33.5 cycles | Ground Truth Benchmark = 30.0 cycles (Delta: +3.5)</div>
                <div class="console-line success">[14:22:01.408] FSM STATE: WARNING | Tier 1 In-Situ Throttle Derate Engaged (-15% Throttle, -40°C Core Temp)</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Right: Unit Metadata & Subsystem Health -->
        <div class="glass-card">
          <div class="card-header">
            <h2 id="inspector-unit-name">Engine U-002 Health Profile</h2>
            <span id="inspector-badge" class="badge WARNING">WARNING</span>
          </div>
          <div class="card-body">
            <div style="display:flex; flex-direction:column; gap:1.2rem;">
              
              <div style="background:#F8FAFC; border:1px solid var(--border-light); border-radius:8px; padding:1rem;">
                <div style="font-size:0.75rem; color:var(--text-muted); font-weight:600;">PREDICTED REMAINING USEFUL LIFE</div>
                <div style="font-size:1.8rem; font-weight:800; color:var(--text-dark); font-family:'JetBrains Mono'; margin-top:0.2rem;" id="inspector-rul-val">
                  33.5 <span style="font-size:0.9rem; color:var(--text-muted);">Cycles</span>
                </div>
                <div style="font-size:0.72rem; color:var(--text-muted); margin-top:0.2rem;" id="inspector-bench-val">
                  Ground Truth Benchmark: 30.0 Cycles (Residual: +3.5)
                </div>
              </div>

              <!-- Subsystem Breakdown -->
              <div>
                <div style="font-size:0.78rem; font-weight:700; color:var(--text-dark); margin-bottom:0.6rem; text-transform:uppercase;">
                  Subsystem Health Decomposition
                </div>
                
                <div style="display:flex; flex-direction:column; gap:0.6rem; font-size:0.75rem; font-family:'JetBrains Mono';">
                  <div>
                    <div style="display:flex; justify-content:space-between; margin-bottom:0.2rem;">
                      <span>High-Pressure Compressor (HPC)</span>
                      <span style="color:var(--yellow-main); font-weight:700;" id="hpc-deg-val">68% Degradation</span>
                    </div>
                    <div class="progress-bar-wrap"><div class="progress-bar WARNING" id="hpc-deg-bar" style="width:68%;"></div></div>
                  </div>
                  <div>
                    <div style="display:flex; justify-content:space-between; margin-bottom:0.2rem;">
                      <span>High-Pressure Turbine (HPT)</span>
                      <span style="color:var(--green-main); font-weight:700;">14% Degradation</span>
                    </div>
                    <div class="progress-bar-wrap"><div class="progress-bar HEALTHY" style="width:14%;"></div></div>
                  </div>
                  <div>
                    <div style="display:flex; justify-content:space-between; margin-bottom:0.2rem;">
                      <span>Combustor Chamber</span>
                      <span style="color:var(--green-main); font-weight:700;">8% Degradation</span>
                    </div>
                    <div class="progress-bar-wrap"><div class="progress-bar HEALTHY" style="width:8%;"></div></div>
                  </div>
                  <div>
                    <div style="display:flex; justify-content:space-between; margin-bottom:0.2rem;">
                      <span>Fan & Low-Pressure Compressor</span>
                      <span style="color:var(--green-main); font-weight:700;">4% Degradation</span>
                    </div>
                    <div class="progress-bar-wrap"><div class="progress-bar HEALTHY" style="width:4%;"></div></div>
                  </div>
                </div>
              </div>

              <!-- Quick Action Navigation -->
              <div style="display:flex; flex-direction:column; gap:0.6rem;">
                <button class="btn-primary" onclick="switchTab('tab-healing', document.querySelectorAll('.nav-tab')[2])">
                  ⚡ Open in Self-Healing Control Room
                </button>
                <button class="btn-secondary" onclick="openWorkOrderModal()">
                  📄 Inspect ISO 55000 Work Order
                </button>
              </div>

            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- ================================================================= -->
    <!-- TAB 3: CLOSED-LOOP SELF-HEALING CONTROL ROOM                      -->
    <!-- ================================================================= -->
    <div id="tab-healing" class="tab-content">
      <div class="healing-split">
        
        <!-- Tier 1 Soft Healing -->
        <div class="tier-box active-tier" id="tier1-box">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span class="tier-tag tag-soft">TIER 1: IN-SITU AUTONOMIC MITIGATION</span>
            <span id="tier1-status-pill" style="font-size:0.75rem; font-weight:700; color:var(--green-main); font-family:'JetBrains Mono';">MITIGATING IN FLIGHT (-40°C)</span>
          </div>

          <div>
            <h3 class="tier-title">Supervisory Throttle & Aerothermal Stress Derating</h3>
            <p class="tier-desc">
              When progressive HPC degradation is identified ($15 &lt; RUL \le 35$), the agent automatically commands a setpoint modulation back to the aircraft FADEC / engine controller. This cools turbine temperatures and decelerates mechanical wear.
            </p>
          </div>

          <!-- Interactive Physics Range Slider -->
          <div class="slider-row">
            <div class="slider-header">
              <span>OPERATIONAL THROTTLE LIMIT (DRAG SLIDER):</span>
              <span id="throttle-pct-label" style="color:var(--green-main); font-weight:700; font-size:0.85rem;">85% (DERATED)</span>
            </div>
            <input type="range" id="throttle-slider" min="70" max="100" value="85" oninput="onThrottleSliderChange(this.value)">
          </div>

          <!-- Physics Real-Time Readout Panel -->
          <div style="background:#F8FAFC; border:1px solid var(--border-light); border-radius:8px; padding:1rem; font-family:'JetBrains Mono'; font-size:0.78rem; display:flex; flex-direction:column; gap:0.5rem;">
            <div>• TARGET SUBSYSTEM: <span style="font-weight:700; color:var(--blue-main);">FADEC THROTTLE RESOLVER</span></div>
            <div>• TEMPERATURE REDUCTION: <span style="font-weight:700; color:var(--green-main);" id="physics-temp-readout">-40°C (642°C &rarr; 602°C)</span></div>
            <div>• MECHANICAL STRESS REDUCTION: <span style="font-weight:700; color:var(--green-main);" id="physics-stress-readout">-25.4%</span></div>
            <div>• MISSION LIFE EXTENSION: <span style="font-weight:700; color:var(--green-main);" id="physics-gain-readout">+25 OPERATING CYCLES GAINED</span></div>
          </div>

          <button class="btn-primary" id="btn-toggle-heal" onclick="toggleSoftHealing()">
            <span>✔</span>
            <span id="btn-heal-text">In-Situ Throttle Derate Active (85%)</span>
          </button>
        </div>

        <!-- Tier 2 Prescriptive Hard Healing -->
        <div class="tier-box">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span class="tier-tag tag-hard">TIER 2: PRESCRIPTIVE CMMS WORK ORDER</span>
            <span style="font-size:0.75rem; color:var(--text-muted); font-family:'JetBrains Mono';">ISO 55000 / MIMOSA</span>
          </div>

          <div>
            <h3 class="tier-title">Autonomous Maintenance Dispatch & Logistics</h3>
            <p class="tier-desc">
              For assets requiring physical intervention ($RUL \le 15$ cycles), the agent generates structured work orders, pre-reserves replacement components in the depot ERP, and assigns priority bay slots with zero human delay.
            </p>
          </div>

          <div style="background:#F8FAFC; border:1px solid var(--border-light); border-radius:8px; padding:1rem; font-family:'JetBrains Mono'; font-size:0.78rem; display:flex; flex-direction:column; gap:0.5rem;">
            <div>• WORK ORDER ID: <span style="font-weight:700; color:var(--blue-main);" id="wo-id-display">AWO-ELXSI-U002-C0158</span></div>
            <div>• STATUS: <span style="font-weight:700; color:var(--green-main);" id="wo-status-text">AUTO-DISPATCHED (412 ms)</span></div>
            <div>• ASSIGNED DEPOT: <strong>DEPOT-NORTH-HUB-BAY-3</strong></div>
            <div>• RESERVED SPARES: <span style="color:var(--text-dark); font-weight:600;">PART-BLADE-HPC-KIT-A</span></div>
            <div>• OBSERVABILITY RATIO (DPR): <span style="color:var(--green-main); font-weight:700;">0.88 &ge; 0.75 (PRESERVED)</span></div>
          </div>

          <button class="btn-secondary" onclick="openWorkOrderModal()">
            <span>📄</span>
            <span>View & Download ISO 55000 Work Order</span>
          </button>
        </div>

      </div>
    </div>

    <!-- ================================================================= -->
    <!-- TAB 4: MLOPS GOVERNANCE & DRIFT REGISTRY                          -->
    <!-- ================================================================= -->
    <div id="tab-mlops" class="tab-content">
      <div class="glass-card">
        <div class="card-header">
          <h2><span>📊</span> MLflow Experiment Tracking & Drift Detection</h2>
          <span style="font-size:0.75rem; font-family:'JetBrains Mono'; color:var(--green-main); font-weight:700;" id="mlops-model-badge">● CHAMPION MODEL v1.1 ACTIVE (PRODUCTION)</span>
        </div>
        <div class="card-body">
          <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:1rem; margin-bottom:1.5rem;">
            <div class="dial-card" id="metric-card-rmse">
              <div class="dial-label"><span>TEST RMSE</span> <span style="color:var(--blue-main);">BENCHMARK</span></div>
              <div class="dial-val" id="metric-rmse" style="color:var(--blue-main);">18.21 <span style="font-size:0.75rem; color:var(--text-muted);">cycles</span></div>
            </div>
            <div class="dial-card" id="metric-card-mae">
              <div class="dial-label"><span>MEAN ABSOLUTE ERROR</span> <span style="color:var(--green-main);">ACCURATE</span></div>
              <div class="dial-val" id="metric-mae" style="color:var(--green-main);">11.65 <span style="font-size:0.75rem; color:var(--text-muted);">cycles</span></div>
            </div>
            <div class="dial-card" id="metric-card-nasa">
              <div class="dial-label"><span>NASA SCORE (ASYMMETRIC)</span> <span style="color:var(--yellow-main);">PENALIZED</span></div>
              <div class="dial-val" id="metric-nasa" style="color:var(--yellow-main);">1712.6</div>
            </div>
            <div class="dial-card" id="metric-card-acc">
              <div class="dial-label"><span>ACCURACY (&plusmn;15 CYCLES)</span> <span style="color:var(--green-main);">HIGH CONFIDENCE</span></div>
              <div class="dial-val" id="metric-acc" style="color:var(--green-main);">72.0%</div>
            </div>
          </div>

          <div style="background:#F8FAFC; border:1px solid var(--border-light); border-radius:10px; padding:1.2rem;">
            <div style="font-size:0.85rem; font-weight:700; margin-bottom:0.8rem; display:flex; justify-content:space-between; align-items:center;">
              <span>Continuous Feature Drift Monitoring (Kolmogorov-Smirnov Test)</span>
              <span style="color:var(--yellow-main); font-family:'JetBrains Mono'; background:var(--yellow-bg); padding:0.2rem 0.6rem; border-radius:6px; border:1px solid var(--yellow-border);">
                PSI = 0.312 (Drift Threshold &gt; 0.250)
              </span>
            </div>
            <p style="font-size:0.78rem; color:var(--text-muted); line-height:1.5; margin-bottom:1rem;">
              When telematics batches arrive from diverse flight conditions (cruise, climb, descent), the KS test checks for feature distribution divergence. If PSI exceeds 0.25, the system invokes the automated challenger retraining pipeline, backtests against holdouts, and automatically promotes the winning model to the production registry.
            </p>
            <div style="display:flex; gap:1rem;">
              <button class="btn-primary" onclick="triggerMLOpsRetrain()">
                <span>⚡</span>
                <span>Launch Autonomous Retraining Runner</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ================================================================= -->
    <!-- TAB 5: WORK ORDERS & AUDIT TRAIL                                  -->
    <!-- ================================================================= -->
    <div id="tab-audit" class="tab-content">
      <div class="glass-card">
        <div class="card-header">
          <h2><span>📋</span> Automated Work Orders Registry (ISO 55000 / MIMOSA)</h2>
          <span style="font-size:0.75rem; font-family:'JetBrains Mono'; color:var(--blue-main);">19 Orders Auto-Dispatched</span>
        </div>
        <div class="card-body">
          <table class="data-table">
            <thead>
              <tr>
                <th>Work Order ID</th>
                <th>Engine ID</th>
                <th>Flight Cycle</th>
                <th>Predicted RUL</th>
                <th>Severity</th>
                <th>Tier 1 Action</th>
                <th>Assigned Depot</th>
                <th>Inspection Action</th>
              </tr>
            </thead>
            <tbody id="work-orders-table-body">
              <!-- Dynamically populated -->
            </tbody>
          </table>
        </div>
      </div>
    </div>

  </main>

  <!-- ================================================================= -->
  <!-- MODAL: WORK ORDER INSPECTION & DISPATCH                           -->
  <!-- ================================================================= -->
  <div class="modal-backdrop" id="wo-modal">
    <div class="modal-window">
      <div class="modal-head">
        <h3 id="modal-wo-title">AUTOMATED WORK ORDER: AWO-ELXSI-U002-C0158</h3>
        <button style="background:none; border:none; font-size:1.5rem; cursor:pointer;" onclick="closeWorkOrderModal()">&times;</button>
      </div>
      <div class="modal-body-content">
        <pre id="modal-json-content"></pre>
      </div>
      <div class="modal-footer">
        <button class="btn-secondary" onclick="copyWorkOrderJSON()">
          <span>📋</span>
          <span>Copy JSON</span>
        </button>
        <button class="btn-secondary" onclick="downloadWorkOrderJSON()">
          <span>📥</span>
          <span>Download JSON File</span>
        </button>
        <button class="btn-primary" id="btn-dispatch-cmms" onclick="dispatchToCMMS()">
          <span>🚀</span>
          <span>Dispatch to SAP / Maximo API</span>
        </button>
      </div>
    </div>
  </div>

  <!-- ================================================================= -->
  <!-- MODAL: MLOPS AUTONOMOUS RETRAINING RUNNER                         -->
  <!-- ================================================================= -->
  <div class="modal-backdrop" id="retrain-modal">
    <div class="modal-window">
      <div class="modal-head">
        <h3><span>⚡</span> MLOps Autonomous Model Retraining Pipeline</h3>
        <button style="background:none; border:none; font-size:1.5rem; cursor:pointer;" onclick="closeRetrainModal()">&times;</button>
      </div>
      <div class="modal-body-content" style="background:#0B1120;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.8rem; font-family:'JetBrains Mono'; font-size:0.75rem; color:#94A3B8;">
          <span id="retrain-status-text">INITIALIZING RETRAINING PIPELINE...</span>
          <span id="retrain-pct-text">0%</span>
        </div>
        <div class="progress-bar-wrap" style="height:8px; background:#1E293B; margin-bottom:1rem;">
          <div class="progress-bar HEALTHY" id="retrain-progress-bar" style="width:0%;"></div>
        </div>

        <div class="console-box" id="retrain-console" style="height:260px;">
          <!-- Real-time log lines will stream here -->
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn-secondary" onclick="closeRetrainModal()">Cancel</button>
        <button class="btn-primary" id="btn-deploy-challenger" style="display:none;" onclick="applyRetrainedModel()">
          <span>✔</span>
          <span>Deploy Challenger v1.2 to Fleet</span>
        </button>
      </div>
    </div>
  </div>

  <!-- Universal Toast Container -->
  <div id="toast-container"></div>

  <script>
    const FLEET_DATA = {fleet_json_str};
    let currentEngine = FLEET_DATA.engines[1] || FLEET_DATA.engines[0];
    let isHealed = true;
    let isStreaming = false;
    let streamInterval = null;
    let currentFilter = 'ALL';
    let currentSearch = '';
    let currentSort = 'RUL_ASC';
    let activeWorkOrderPayload = null;

    window.addEventListener('DOMContentLoaded', () => {{
      renderEngineTiles();
      populateWorkOrdersTable();
      selectEngine(currentEngine.unit_id);
    }});

    /* Toast Notification Utility */
    function showToast(title, message, type = 'info') {{
      const container = document.getElementById('toast-container');
      const toast = document.createElement('div');
      toast.className = `toast ${{type}}`;
      
      let icon = 'ℹ️';
      if (type === 'success') icon = '✅';
      if (type === 'warning') icon = '⚠️';
      if (type === 'danger') icon = '🚨';

      toast.innerHTML = `
        <div class="toast-icon">${{icon}}</div>
        <div class="toast-content">
          <div class="toast-title">${{title}}</div>
          <div class="toast-msg">${{message}}</div>
        </div>
      `;

      container.appendChild(toast);
      setTimeout(() => {{
        toast.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
        toast.style.opacity = '0';
        toast.style.transform = 'translateX(100%)';
        setTimeout(() => toast.remove(), 400);
      }}, 3600);
    }}

    /* Tab Switching */
    function switchTab(tabId, el) {{
      document.querySelectorAll('.tab-content').forEach(tc => tc.classList.remove('active'));
      document.querySelectorAll('.nav-tab').forEach(nt => nt.classList.remove('active'));
      
      document.getElementById(tabId).classList.add('active');
      if (el) {{
        el.classList.add('active');
      }} else {{
        // Auto-highlight corresponding tab
        const tabs = document.querySelectorAll('.nav-tab');
        if (tabId === 'tab-fleet') tabs[0].classList.add('active');
        if (tabId === 'tab-inspector') tabs[1].classList.add('active');
        if (tabId === 'tab-healing') tabs[2].classList.add('active');
        if (tabId === 'tab-mlops') tabs[3].classList.add('active');
        if (tabId === 'tab-audit') tabs[4].classList.add('active');
      }}
    }}

    /* Fleet Grid Rendering with Filtering & Sorting */
    function renderEngineTiles() {{
      const container = document.getElementById('engine-tiles-container');
      container.innerHTML = '';

      let list = FLEET_DATA.engines.filter(e => {{
        const matchesFilter = (currentFilter === 'ALL' || e.state === currentFilter);
        const matchesSearch = currentSearch === '' || 
          `U-${{String(e.unit_id).padStart(3, '0')}}`.toLowerCase().includes(currentSearch.toLowerCase()) ||
          String(e.unit_id).includes(currentSearch);
        return matchesFilter && matchesSearch;
      }});

      // Apply Sort
      list.sort((a, b) => {{
        if (currentSort === 'RUL_ASC') return a.predicted_rul - b.predicted_rul;
        if (currentSort === 'RUL_DESC') return b.predicted_rul - a.predicted_rul;
        if (currentSort === 'UNIT_ASC') return a.unit_id - b.unit_id;
        if (currentSort === 'CYCLE_DESC') return b.current_cycle - a.current_cycle;
        return 0;
      }});

      list.forEach(eng => {{
        const tile = document.createElement('div');
        tile.className = `engine-tile ${{eng.unit_id === currentEngine.unit_id ? 'active' : ''}}`;
        tile.onclick = () => {{
          selectEngine(eng.unit_id);
          switchTab('tab-inspector');
          showToast(`Engine U-${{String(eng.unit_id).padStart(3, '0')}} Selected`, `Loaded prognostic twin: RUL ${{eng.predicted_rul}} cycles (${{eng.state}})`, eng.state === 'CRITICAL' ? 'danger' : 'info');
        }};

        const pct = Math.min(100, Math.max(0, (eng.predicted_rul / 125) * 100));

        tile.innerHTML = `
          <div class="tile-header">
            <span class="tile-id">ENGINE U-${{String(eng.unit_id).padStart(3, '0')}}</span>
            <span class="badge ${{eng.state}}">${{eng.state}}</span>
          </div>
          <div class="tile-stats">
            <span>Cycle: ${{eng.current_cycle}}</span>
            <span style="font-weight:700; color:var(--text-dark);">${{eng.predicted_rul}} CYC</span>
          </div>
          <div class="progress-bar-wrap">
            <div class="progress-bar ${{eng.state}}" style="width: ${{pct}}%;"></div>
          </div>
        `;
        container.appendChild(tile);
      }});
    }}

    function filterFleet(filter, btn) {{
      document.querySelectorAll('.filter-pills .pill-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentFilter = filter;
      renderEngineTiles();
      showToast('Fleet Filter Applied', `Showing ${{filter}} assets in connected grid`, 'info');
    }}

    function onSearchInput(val) {{
      currentSearch = val;
      renderEngineTiles();
    }}

    function onSortChange(sortVal) {{
      currentSort = sortVal;
      renderEngineTiles();
      showToast('Fleet Sorting Updated', `Ordered by ${{sortVal}}`, 'info');
    }}

    /* Select Engine Diagnostic Twin */
    function selectEngine(unitId) {{
      currentEngine = FLEET_DATA.engines.find(e => e.unit_id === unitId) || FLEET_DATA.engines[0];
      
      // Update Tab Header
      document.getElementById('tab-inspector-title').innerText = `Engine Diagnostic Twin (#${{String(unitId).padStart(3, '0')}})`;
      document.getElementById('inspector-unit-name').innerText = `Engine U-${{String(unitId).padStart(3, '0')}} Health Profile`;
      
      const badge = document.getElementById('inspector-badge');
      badge.className = `badge ${{currentEngine.state}}`;
      badge.innerText = currentEngine.state;

      // Stats
      document.getElementById('inspector-rul-val').innerHTML = `${{currentEngine.predicted_rul}} <span style="font-size:0.9rem; color:var(--text-muted);">Cycles</span>`;
      const res = (currentEngine.predicted_rul - currentEngine.true_rul).toFixed(1);
      document.getElementById('inspector-bench-val').innerText = `Ground Truth Benchmark: ${{currentEngine.true_rul}} Cycles (Residual: ${{res > 0 ? '+' : ''}}${{res}})`;
      document.getElementById('svg-current-cycle-label').innerText = `Cycle ${{currentEngine.current_cycle}} (Current)`;

      // Subsystem Degradation
      let hpcDeg = 68;
      if (currentEngine.state === 'HEALTHY') hpcDeg = 22;
      if (currentEngine.state === 'CRITICAL') hpcDeg = 92;
      document.getElementById('hpc-deg-val').innerText = `${{hpcDeg}}% Degradation`;
      document.getElementById('hpc-deg-bar').style.width = `${{hpcDeg}}%`;
      document.getElementById('hpc-deg-bar').className = `progress-bar ${{currentEngine.state}}`;

      // Telemetry Sensors
      if (currentEngine.sensors) {{
        document.getElementById('dial-s11').innerHTML = `${{currentEngine.sensors.sensor_11 || 47.45}} <span style="font-size:0.75rem; color:var(--text-muted);">psia</span>`;
        document.getElementById('dial-s12').innerHTML = `${{currentEngine.sensors.sensor_12 || 518.34}} <span style="font-size:0.75rem; color:var(--text-muted);">rpm</span>`;
        document.getElementById('dial-s4').innerHTML = `${{currentEngine.sensors.sensor_4 || 1406.47}} <span style="font-size:0.75rem; color:var(--text-muted);">°R</span>`;
        document.getElementById('dial-s2').innerHTML = `${{currentEngine.sensors.sensor_2 || 646.85}} <span style="font-size:0.75rem; color:var(--text-muted);">°R</span>`;
      }}

      // Self-Healing
      document.getElementById('wo-id-display').innerText = currentEngine.work_order_id || 'NO_DISPATCH_REQUIRED';
      
      // Update Physics Slider
      onThrottleSliderChange(document.getElementById('throttle-slider').value);
    }}

    /* Interactive Throttle Physics Engine */
    function onThrottleSliderChange(val) {{
      val = parseInt(val);
      const derate = 100 - val;
      const throttleLabel = document.getElementById('throttle-pct-label');
      const tempReadout = document.getElementById('physics-temp-readout');
      const stressReadout = document.getElementById('physics-stress-readout');
      const gainReadout = document.getElementById('physics-gain-readout');
      const s4Badge = document.getElementById('dial-s4-badge');
      const svgMitigatedPath = document.getElementById('svg-mitigated-path');
      const legendMitigated = document.getElementById('svg-legend-mitigated');
      const statusPill = document.getElementById('tier1-status-pill');
      const btn = document.getElementById('btn-toggle-heal');
      const btnText = document.getElementById('btn-heal-text');

      if (derate === 0) {{
        throttleLabel.innerText = '100% (NOMINAL)';
        throttleLabel.style.color = 'var(--text-muted)';
        tempReadout.innerText = '0°C (642°C Baseline)';
        tempReadout.style.color = 'var(--text-muted)';
        stressReadout.innerText = '0.0% (Full Mechanical Stress)';
        stressReadout.style.color = 'var(--text-muted)';
        gainReadout.innerText = '+0 CYCLES (Standard Decay)';
        gainReadout.style.color = 'var(--text-muted)';
        s4Badge.innerText = '642°C (BASELINE)';
        s4Badge.style.color = 'var(--yellow-main)';
        svgMitigatedPath.style.display = 'none';
        legendMitigated.style.display = 'none';
        statusPill.innerText = 'STANDBY (NOMINAL 100%)';
        statusPill.style.color = 'var(--text-muted)';
        btn.classList.add('derate-inactive');
        btnText.innerText = 'Apply In-Situ Throttle Derate (-15%)';
        isHealed = false;
      }} else {{
        const deltaTemp = Math.round(derate * 2.67);
        const deltaStress = (derate * 1.693).toFixed(1);
        const gainCycles = Math.round(derate * 1.667);
        const newTemp = 642 - deltaTemp;

        throttleLabel.innerText = `${{val}}% (DERATED)`;
        throttleLabel.style.color = 'var(--green-main)';
        tempReadout.innerText = `-${{deltaTemp}}°C (642°C → ${{newTemp}}°C)`;
        tempReadout.style.color = 'var(--green-main)';
        stressReadout.innerText = `-${{deltaStress}}%`;
        stressReadout.style.color = 'var(--green-main)';
        gainReadout.innerText = `+${{gainCycles}} OPERATING CYCLES GAINED`;
        gainReadout.style.color = 'var(--green-main)';
        s4Badge.innerText = `${{newTemp}}°C (-${{deltaTemp}}°C)`;
        s4Badge.style.color = 'var(--green-main)';

        // Dynamically recalculate SVG curve endpoint and control point
        const endX = Math.min(680, 560 + gainCycles * 3.6);
        svgMitigatedPath.setAttribute('d', `M 420 140 Q ${{420 + (endX - 420) * 0.5}} 150, ${{endX}} 180`);
        svgMitigatedPath.style.display = 'block';
        legendMitigated.style.display = 'inline';
        legendMitigated.innerText = `● Mitigated (+${{gainCycles}} Cyc)`;

        statusPill.innerText = `MITIGATING IN FLIGHT (-${{deltaTemp}}°C)`;
        statusPill.style.color = 'var(--green-main)';
        btn.classList.remove('derate-inactive');
        btnText.innerText = `In-Situ Throttle Derate Active (${{val}}%)`;
        isHealed = true;
      }}
    }}

    function toggleSoftHealing() {{
      const slider = document.getElementById('throttle-slider');
      if (isHealed) {{
        slider.value = 100;
        onThrottleSliderChange(100);
        showToast('In-Situ Derating Disengaged', 'Throttle restored to 100% nominal cruise limit', 'warning');
      }} else {{
        slider.value = 85;
        onThrottleSliderChange(85);
        showToast('In-Situ Derating Engaged', 'Throttle capped at 85%: Core temperature dropped by 40°C (+25 Cycles gained)', 'success');
      }}
    }}

    /* Work Orders Table */
    function populateWorkOrdersTable() {{
      const tbody = document.getElementById('work-orders-table-body');
      tbody.innerHTML = '';
      
      const orders = FLEET_DATA.engines.filter(e => e.has_work_order);
      orders.forEach(eng => {{
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td style="color:var(--blue-main); font-weight:700;">${{eng.work_order_id}}</td>
          <td>ENGINE U-${{String(eng.unit_id).padStart(3, '0')}}</td>
          <td>${{eng.current_cycle}}</td>
          <td>${{eng.predicted_rul}} CYC</td>
          <td><span class="badge ${{eng.state}}">${{eng.state}}</span></td>
          <td>${{eng.tier1_command}}</td>
          <td>DEPOT-NORTH-HUB-BAY-3</td>
          <td><button class="pill-btn" style="padding:0.25rem 0.6rem; font-size:0.75rem;" onclick="openWorkOrderModalFor('${{eng.work_order_id}}', ${{eng.unit_id}}, ${{eng.current_cycle}}, ${{eng.predicted_rul}}, '${{eng.state}}')">Inspect</button></td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    function openWorkOrderModal() {{
      openWorkOrderModalFor(currentEngine.work_order_id, currentEngine.unit_id, currentEngine.current_cycle, currentEngine.predicted_rul, currentEngine.state);
    }}

    function openWorkOrderModalFor(woId, unitId, cycle, rul, state) {{
      const modal = document.getElementById('wo-modal');
      const cleanWoId = woId || `AWO-ELXSI-U${{String(unitId).padStart(3, '0')}}-C${{cycle}}`;
      document.getElementById('modal-wo-title').innerText = `AUTOMATED WORK ORDER: ${{cleanWoId}}`;

      activeWorkOrderPayload = {{
        "work_order_id": cleanWoId,
        "standard_compliance": "ISO 55000 / MIMOSA-OSA-EAI",
        "asset_metadata": {{
          "unit_id": unitId,
          "asset_class": "Turbofan Engine (NASA C-MAPSS Class)",
          "current_flight_cycle": cycle,
          "predicted_remaining_useful_life": rul,
          "severity_rank": state === "CRITICAL" ? 1 : 2
        }},
        "tier_1_autonomic_remediation": {{
          "command": state === "CRITICAL" ? "EMERGENCY_THROTTLE_DERATE_20PCT" : "APPLY_OPERATIONAL_DERATE_15PCT",
          "throttle_cap": "85.0%",
          "core_temperature_reduction_deg_c": 40.0,
          "projected_cycle_extension": 25.0
        }},
        "tier_2_prescriptive_maintenance": {{
          "action_code": state === "CRITICAL" ? "BORESCOPE_INSPECT_AND_OVERHAUL_HPC" : "SCHEDULE_DEPOT_LUBRICATION",
          "target_depot": "DEPOT-NORTH-HUB-BAY-3",
          "reserved_spare_kits": ["PART-BLADE-HPC-KIT-A", "PART-SEAL-CORE-04"],
          "diagnostic_preservation_ratio_dpr": 0.88,
          "estimated_bay_hours": state === "CRITICAL" ? 14.5 : 4.0
        }},
        "automation_metadata": {{
          "agent_type": "Deterministic Rule-Based FSM (Non-LLM)",
          "turnaround_latency_ms": 412,
          "human_exception_required": false
        }}
      }};

      document.getElementById('modal-json-content').innerText = JSON.stringify(activeWorkOrderPayload, null, 2);
      modal.classList.add('open');
    }}

    function closeWorkOrderModal() {{
      document.getElementById('wo-modal').classList.remove('open');
    }}

    function copyWorkOrderJSON() {{
      if (!activeWorkOrderPayload) return;
      navigator.clipboard.writeText(JSON.stringify(activeWorkOrderPayload, null, 2));
      showToast('Copied to Clipboard', 'Full ISO 55000 work order payload copied', 'success');
    }}

    function downloadWorkOrderJSON() {{
      if (!activeWorkOrderPayload) return;
      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(activeWorkOrderPayload, null, 2));
      const downloadAnchor = document.createElement('a');
      downloadAnchor.setAttribute("href", dataStr);
      downloadAnchor.setAttribute("download", `${{activeWorkOrderPayload.work_order_id}}.json`);
      document.body.appendChild(downloadAnchor);
      downloadAnchor.click();
      downloadAnchor.remove();
      showToast('File Downloaded', `Saved ${{activeWorkOrderPayload.work_order_id}}.json to downloads`, 'success');
    }}

    function dispatchToCMMS() {{
      const btn = document.getElementById('btn-dispatch-cmms');
      btn.innerHTML = '<span>⏳</span> Dispatching to SAP / Maximo API...';
      btn.disabled = true;

      setTimeout(() => {{
        btn.innerHTML = '<span>✅</span> Dispatched (HTTP 201 Created)';
        btn.style.background = 'linear-gradient(135deg, #059669, #047857)';
        showToast('SAP / Maximo CMMS Dispatch Confirmed', 'HTTP 201 Created | Work Order #SAP-948210 registered at DEPOT-NORTH-HUB-BAY-3', 'success');
        
        setTimeout(() => {{
          btn.innerHTML = '<span>🚀</span> Dispatch to SAP / Maximo API';
          btn.disabled = false;
          closeWorkOrderModal();
        }}, 1400);
      }}, 750);
    }}

    /* Real-Time Telemetry Simulation */
    function toggleStreamSimulation() {{
      isStreaming = !isStreaming;
      const icon = document.getElementById('stream-icon');
      const label = document.getElementById('stream-label');
      const btn = document.getElementById('btn-stream-toggle');
      const badge = document.getElementById('stream-status-badge');

      if (isStreaming) {{
        icon.innerText = '⏸';
        label.innerText = 'Streaming Live Telemetry (1.0 Hz)...';
        btn.classList.add('active');
        badge.innerText = 'STREAM ACTIVE (1.0 Hz)';
        badge.style.color = 'var(--green-main)';
        showToast('Edge Telemetry Ingestion Started', 'Simulating real-time sensor packets at 1.0 Hz with stochastic jitter', 'success');

        streamInterval = setInterval(() => {{
          currentEngine.current_cycle += 1;
          currentEngine.predicted_rul = Math.max(0, (currentEngine.predicted_rul - 0.4).toFixed(1));
          
          // Realistic Gaussian Sensor Jitter
          const jitter11 = (47.45 + (Math.random() - 0.5) * 0.4).toFixed(2);
          const jitter12 = (518.34 + (Math.random() - 0.5) * 1.2).toFixed(2);
          const jitter4 = (1406.47 + (Math.random() - 0.5) * 4.2).toFixed(2);
          const jitter2 = (646.85 + (Math.random() - 0.5) * 0.8).toFixed(2);

          document.getElementById('dial-s11').innerHTML = `${{jitter11}} <span style="font-size:0.75rem; color:var(--text-muted);">psia</span>`;
          document.getElementById('dial-s12').innerHTML = `${{jitter12}} <span style="font-size:0.75rem; color:var(--text-muted);">rpm</span>`;
          document.getElementById('dial-s4').innerHTML = `${{jitter4}} <span style="font-size:0.75rem; color:var(--text-muted);">°R</span>`;
          document.getElementById('dial-s2').innerHTML = `${{jitter2}} <span style="font-size:0.75rem; color:var(--text-muted);">°R</span>`;

          document.getElementById('inspector-rul-val').innerHTML = `${{currentEngine.predicted_rul}} <span style="font-size:0.9rem; color:var(--text-muted);">Cycles</span>`;
          document.getElementById('svg-current-cycle-label').innerText = `Cycle ${{currentEngine.current_cycle}} (Current)`;

          // Append to Console
          const consoleEl = document.getElementById('telemetry-stream-console');
          const time = new Date().toTimeString().split(' ')[0];
          const line = document.createElement('div');
          line.className = 'console-line';
          line.innerText = `[${{time}}] PKT: U-${{String(currentEngine.unit_id).padStart(3, '0')}} | Cyc ${{currentEngine.current_cycle}} | S11=${{jitter11}} psi | S12=${{jitter12}} rpm | RUL=${{currentEngine.predicted_rul}} cyc`;
          consoleEl.appendChild(line);
          consoleEl.scrollTop = consoleEl.scrollHeight;

        }}, 1000);
      }} else {{
        icon.innerText = '▶';
        label.innerText = 'Simulate Real-Time Telemetry';
        btn.classList.remove('active');
        badge.innerText = 'STREAM STANDBY';
        badge.style.color = 'var(--text-muted)';
        clearInterval(streamInterval);
        showToast('Telemetry Stream Paused', 'Simulation socket detached', 'warning');
      }}
    }}

    /* MLOps Autonomous Retraining Runner */
    function triggerMLOpsRetrain() {{
      const modal = document.getElementById('retrain-modal');
      const consoleBox = document.getElementById('retrain-console');
      const pBar = document.getElementById('retrain-progress-bar');
      const pText = document.getElementById('retrain-pct-text');
      const statusText = document.getElementById('retrain-status-text');
      const deployBtn = document.getElementById('btn-deploy-challenger');

      modal.classList.add('open');
      consoleBox.innerHTML = '';
      deployBtn.style.display = 'none';
      pBar.style.width = '0%';
      pText.innerText = '0%';
      statusText.innerText = 'STARTING STREAMING RE-TRAIN...';

      const logSteps = [
        {{ delay: 200, pct: 15, text: '[00:00.12] Ingesting streaming telematics batch: 5,000 cycles from 100 edge aircraft...', cls: '' }},
        {{ delay: 700, pct: 35, text: '[00:00.48] Running Two-Sample Kolmogorov-Smirnov Feature Drift Test on Sensor 11 & Sensor 12...', cls: 'warn' }},
        {{ delay: 1200, pct: 55, text: '[00:00.82] DRIFT CONFIRMED: KS-stat D = 0.184 (p = 0.0031 < 0.05). Population Stability Index (PSI) = 0.312 > 0.250.', cls: 'warn' }},
        {{ delay: 1700, pct: 75, text: '[00:01.35] Initializing Challenger XGBoost model with NASA Asymmetric Loss Objective (alpha=10, beta=13)...', cls: '' }},
        {{ delay: 2200, pct: 90, text: '[00:01.90] Convergence at 108 boosting trees. Backtesting holdout validation split...', cls: '' }},
        {{ delay: 2800, pct: 100, text: '[00:02.45] BACKTEST COMPARISON:\\n           - Champion v1.1: RMSE = 18.21 cycles, MAE = 11.65 cycles, NASA = 1712.6\\n           - Challenger v1.2: RMSE = 17.42 cycles, MAE = 10.89 cycles, NASA = 1584.2\\n           - DELTA: -0.79 cycles (-4.34% error drop, -128.4 NASA score penalty).', cls: 'success' }},
        {{ delay: 3300, pct: 100, text: '[00:02.90] AUTOMATED GATE: Challenger meets DO-178C safety criteria. Ready for Production deployment.', cls: 'head' }}
      ];

      logSteps.forEach(step => {{
        setTimeout(() => {{
          pBar.style.width = `${{step.pct}}%`;
          pText.innerText = `${{step.pct}}%`;
          const line = document.createElement('div');
          line.className = `console-line ${{step.cls}}`;
          line.innerText = step.text;
          consoleBox.appendChild(line);
          consoleBox.scrollTop = consoleBox.scrollHeight;
        }}, step.delay);
      }});

      setTimeout(() => {{
        statusText.innerText = 'RETRAINING COMPLETE (CHALLENGER READY)';
        deployBtn.style.display = 'inline-flex';
      }}, 3500);
    }}

    function closeRetrainModal() {{
      document.getElementById('retrain-modal').classList.remove('open');
    }}

    function applyRetrainedModel() {{
      // Mutate DOM to reflect newly promoted model
      document.getElementById('metric-rmse').innerHTML = '17.42 <span style="font-size:0.75rem; color:var(--text-muted);">cycles</span>';
      document.getElementById('metric-mae').innerHTML = '10.89 <span style="font-size:0.75rem; color:var(--text-muted);">cycles</span>';
      document.getElementById('metric-nasa').innerText = '1584.2';
      document.getElementById('metric-acc').innerText = '76.0%';
      document.getElementById('mlops-model-badge').innerText = '● CHALLENGER MODEL v1.2 PROMOTED TO PROD';
      document.getElementById('nav-mlops-count').innerText = 'RMSE 17.42 (Active)';
      document.getElementById('nav-mlops-count').style.background = '#ECFDF5';
      document.getElementById('nav-mlops-count').style.color = '#065F46';

      // Visual pulse highlight on cards
      const cards = [document.getElementById('metric-card-rmse'), document.getElementById('metric-card-mae'), document.getElementById('metric-card-nasa'), document.getElementById('metric-card-acc')];
      cards.forEach(c => {{
        c.style.transition = 'all 0.5s ease';
        c.style.boxShadow = '0 0 16px rgba(16, 185, 129, 0.4)';
        c.style.borderColor = 'var(--green-main)';
        setTimeout(() => {{
          c.style.boxShadow = 'var(--shadow-sm)';
          c.style.borderColor = 'var(--border-light)';
        }}, 2000);
      }});

      closeRetrainModal();
      showToast('Model Registry Updated', 'MLflow: Challenger v1.2 promoted to Production (Test RMSE improved to 17.42 cycles)', 'success');
      switchTab('tab-mlops');
    }}
  </script>
</body>
</html>
"""

    # Output to both prototype/index.html and root AERO_SHIELD_Interactive_Prototype.html
    out_paths = [
        os.path.join(prototype_dir, "index.html"),
        os.path.join(project_root, "AERO_SHIELD_Interactive_Prototype.html")
    ]

    for p in out_paths:
        with open(p, "w", encoding="utf-8") as f:
            f.write(html_code)
        print(f"[SUCCESS] Light-Themed Glassmorphic Prototype generated at: {p}")

if __name__ == "__main__":
    generate_light_prototype()
