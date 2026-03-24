import os
import time
from datetime import datetime
import math
import random

# --- CONFIGURATION ---
NODE_ID = "DELL-LATITUDE-PRINCE-01"
CORE_SPEED = "2.4 GHz" # Check your Task Manager for your actual speed

def simulate_ai_workload():
    # This simulates a "Neural Network" calculation
    # It uses your CPU to solve 100,000 math problems
    start = time.time()
    for i in range(100000):
        _ = math.sqrt(i) * math.sin(i)
    end = time.time()
    return round(end - start, 4) # Returns how many seconds it took

tasks_completed = 0

while True:
    now_time = datetime.now().strftime("%I:%M:%S %p")
    
    # 1. Run the "AI Task"
    print(f"[{now_time}] Starting AI Compute Task...")
    compute_time = simulate_ai_workload()
    tasks_completed += 1
    
    # 2. Update the Dashboard for the "Client" (You on your phone)
    dashboard_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <style>
            body {{ background: #000; color: #00ff41; font-family: 'Courier New', monospace; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
            .node-box {{ border: 2px solid #00ff41; padding: 25px; border-radius: 5px; box-shadow: 0 0 20px #004400; width: 85%; }}
            .header {{ font-size: 1.2em; border-bottom: 1px solid #00ff41; margin-bottom: 15px; padding-bottom: 5px; }}
            .stat {{ margin: 10px 0; font-size: 1.1em; }}
            .value {{ color: #fff; font-weight: bold; }}
            .pulse {{ animation: blink 1.5s infinite; color: #00ff41; }}
            @keyframes blink {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0.2; }} 100% {{ opacity: 1; }} }}
        </style>
    </head>
    <body>
        <div class='node-box'>
            <div class='header'>COGNILYT_COMPUTE_NODE_v1.0</div>
            <div class='stat'>NODE_ID: <span class='value'>{NODE_ID}</span></div>
            <div class='stat'>CPU_SPEED: <span class='value'>{CORE_SPEED}</span></div>
            <div class='stat'>STATUS: <span class='pulse'>ACTIVE_COMPUTING ●</span></div>
            <hr style='border: 0.5px solid #222;'>
            <div class='stat'>TASKS_COMPLETED: <span class='value'>{tasks_completed}</span></div>
            <div class='stat'>LAST_TASK_SPEED: <span class='value'>{compute_time}s</span></div>
            <div class='stat'>NETWORK_UPTIME: <span class='value'>{now_time}</span></div>
        </div>
    </body>
    </html>
    """

    with open("index.html", "w") as f:
        f.write(dashboard_html)

    # 3. Push proof of work to the Cloud
    os.system("git add index.html")
    os.system(f'git commit -m "Task {tasks_completed} Complete"')
    os.system("git push origin main")
    
    print(f"Task {tasks_completed} logged to the Network.")
    
    # Wait 5 minutes for the next cycle
    time.sleep(300)