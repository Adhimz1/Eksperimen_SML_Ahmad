import subprocess
res = subprocess.run([r".venv\Scripts\python", "create_zip.py"], capture_output=True, text=True)
print(res.stdout)
if res.stderr: print(res.stderr)
