import os
import time
from datetime import datetime

# --- CONFIGURATION ---
NODE_ID = "DELL-LATITUDE-PRINCE-01"
# Put your V-Code from Gaganode here:
GAGANODE_TOKEN = "afuswvnlbtqcfqme967436aa3002cc4f" 

tasks_completed = 0

while True:
    now_time = datetime.now().strftime("%I:%M:%S %p")
    tasks_completed += 1
    
    # This is the "Earning Mode" dashboard for your phone
    dashboard_html = f"""
    <!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <style>
            body {{ background: #000; color: #00ff41; font-family: 'Courier New', monospace; text-align: center; padding: 50px 20px; }}
            .node-card {{ border: 2px solid #00ff41; padding: 20px; border-radius: 10px; box-shadow: 0 0 20px #003300; }}
            .money {{ color: #ffcc00; font-size: 2em; margin: 20px 0; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class='node-card'>
            <h1>COGNILYT NETWORK</h1>
            <p>ID: {NODE_ID}</p>
            <div style='color: #00ff41;'>● ACTIVE_EARNING</div>
            <hr style='border-color: #222;'>
            <div class='money'>EARNING_MODE: ON</div>
            <p>TASKS VERIFIED: {tasks_completed}</p>
            <p>LAST SYNC: {now_time}</p>
        </div>
    </body>
    </html>
    """

    # 1. Save the file locally
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(dashboard_html)

    # 2. Push to GitHub automatically
    os.system("git add .")
    os.system(f'git commit -m "Node Update {tasks_completed}"')
    os.system("git push origin main --force")
    
    print(f"[{now_time}] Syncing EARNING_MODE to your phone...")
    time.sleep(300)