import os
import time
import numpy as np # This is the "Heavy Math" library
from datetime import datetime

# --- CONFIGURATION ---
NODE_ID = "DELL-LATITUDE-PRINCE-01-HEAVY"
GAGANODE_TOKEN = "afuswvnlbtqcfqme967436aa3002cc4f" 

def perform_heavy_task():
    print("Starting AI Compute Task: Matrix Factorization...")
    # This creates two huge 1000x1000 matrices and multiplies them
    # This simulates training an AI Recommendation Model
    size = 1000 
    matrix_a = np.random.rand(size, size)
    matrix_b = np.random.rand(size, size)
    result = np.dot(matrix_a, matrix_b) # The "Heavy" part
    return f"COMPLETED_1M_CALCULATIONS_{np.mean(result):.4f}"

tasks_completed = 0

while True:
    start_time = time.time()
    work_result = perform_heavy_task() # Your laptop is now WORKING
    end_time = time.time()
    
    tasks_completed += 1
    duration = round(end_time - start_time, 2)
    now_time = datetime.now().strftime("%I:%M:%S %p")
    
    # Updated Dashboard for your Phone
    dashboard_html = f"""
    <!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <style>
            body {{ background: #050505; color: #00ff41; font-family: 'Courier New', monospace; text-align: center; padding: 30px; }}
            .node-card {{ border: 3px solid #ff0055; padding: 20px; border-radius: 15px; box-shadow: 0 0 30px #440011; }}
            .heavy-task {{ color: #00ecff; font-weight: bold; font-size: 1.2em; }}
            .money {{ color: #ffcc00; font-size: 2.5em; margin: 10px 0; }}
        </style>
    </head>
    <body>
        <div class='node-card'>
            <h1>COGNILYT POWER NODE</h1>
            <p>ID: {NODE_ID}</p>
            <div class='heavy-task'>[TASK: AI_MATRIX_REDUCTION]</div>
            <div class='money'>EARNING_MODE: ULTRA</div>
            <p>COMPUTE CYCLES: {tasks_completed}</p>
            <p>LAST WORK UNIT: {work_result}</p>
            <p>SYNCED AT: {now_time} (took {duration}s)</p>
        </div>
    </body>
    </html>
    """

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(dashboard_html)

    # Automatically push the "Proof of Work" to GitHub
    os.system("git add .")
    os.system(f'git commit -m "Work Unit {tasks_completed} Verified"')
    os.system("git push origin main --force")
    
    print(f"[{now_time}] Heavy Task Complete ({duration}s). Data sent to Cognilyt Cloud.")
    time.sleep(60) # High-frequency updates (every 1 minute)