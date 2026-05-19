import subprocess

res = subprocess.run([r".venv\Scripts\python", "auto_train.py"], capture_output=True, text=True)
print("STDOUT:", res.stdout)
print("STDERR:", res.stderr)
