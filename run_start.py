import subprocess
res = subprocess.run([r".venv\Scripts\python", "start_services.py"], capture_output=True, text=True)
print(res.stdout)
