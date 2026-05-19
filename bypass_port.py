import subprocess
res = subprocess.run([r".venv\Scripts\python", "check_port.py"], capture_output=True, text=True)
print(res.stdout)
