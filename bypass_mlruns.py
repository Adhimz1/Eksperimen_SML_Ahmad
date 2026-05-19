import subprocess
res = subprocess.run([r".venv\Scripts\python", "find_mlruns.py"], capture_output=True, text=True)
print("OUTPUT:")
print(res.stdout)
