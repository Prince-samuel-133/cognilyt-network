import os
import time
from datetime import datetime

# Everything below 'while True:' MUST be indented (pushed to the right)
while True:
    now = datetime.now().strftime("%H:%M:%S")
    
    # 1. Create the file
    with open("index.html", "w") as f:
        f.write(f"<h1>Node: DELL-LATITUDE-PRINCE-01</h1>")
        f.write(f"<h2>Status: ONLINE</h2>")
        f.write(f"<p>Last Update: {now}</p>")
    
    # 2. Push to GitHub
    print(f"[{now}] Sending to GitHub...")
    os.system("git add index.html")
    os.system('git commit -m "Auto-update"')
    os.system("git push origin main")
    
    # 3. Wait
    print("Sleeping...")
    time.sleep(300)