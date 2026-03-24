import os
import time
from datetime import datetime
import math

# --- NODE CONFIGURATION ---
NODE_ID = "DELL-LATITUDE-PRINCE-01"
# We simulate a "Market Price" for CPU Compute (e.g., $0.02 per 1k tasks)
PRICE_PER_TASK = 0.0002 

def run_ai_math_task():
    # This simulates a "Neural Network Inference" step
    start = time.time()
    for i in range(500000):
        _ = math.sqrt(i) * math.exp(math.sin(i))
    end = time.time()
    return round(end - start, 4)

tasks_completed = 0
total_simulated_earnings = 0.0

while True:
    now_time = datetime.now().strftime("%I:%M:%S %p")
    
    # 1. Execute the Workload
    print(f"[{now_time}] Executing AI Math Workload...")
    compute_seconds = run_ai_math_task()
    tasks_completed += 1
    total_simulated_earnings += PRICE_PER_TASK
    
    # 2. Build the Business Dashboard
    dashboard_html = f"""
    <!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <style>
            body {{ background: #0a0a0a; color: #00ff41; font-family: 'Courier New', monospace; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
            .node-container {{ border: 2px solid #00ff41; padding: 25px; border-radius: 5px; box-shadow: 0 0 20px #003300; width: 90%; max-width: 400px; }}
            .header {{ font-size: 1.2em; border-bottom: 1px solid #333; margin-bottom: 15px; padding-bottom: 10px; color: #fff; }}
            .metric {{ margin: 12px 0; display: flex; justify-content: space-between; }}
            .label {{ color: #888; text-transform: uppercase; font-size: 0.8em; }}
            .value {{ color: #00ff41; font-weight: bold; }}
            .earning {{ color: #ffcc00; font-size: 1.4em; text-align: center; margin-top: 20px; border-top: 1px solid #333; padding-top: 10px; }}
        </style>
    </head>
    <body>
        <div class='node-container'>
            <div class='header'>COGNILYT COMPUTE NODE 01</div>
            <div class='metric'><span class='label'>Status</span><span class='value'>MINING_COMPUTE ●</span></div>
            <div class='metric'><span class='label'>Tasks Done</span><span class='value'>{tasks_completed}</span></div>
            <div class='metric'><span class='label'>Last Task Speed</span><span class='value'>{compute_seconds}s</span></div>
            <div class='metric'><span class='label'>System Clock</span><span class='value'>{now_time}</span></div>
            <div class='earning'>EST. CREDIT: ${total_simulated_earnings:.4f}</div>
        </div>
    </body>
    </html>
    """

    # 3. Write and Push to Public Ledger (GitHub)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(dashboard_html)

    os.system("git add index.html")
    os.system(f'git commit -m "Compute Task {tasks_completed} Verified"')
    os.system("git push origin main")
    
    print(f"Task {tasks_completed} verified and synced. Waiting 5 mins...")
    time.sleep(300)