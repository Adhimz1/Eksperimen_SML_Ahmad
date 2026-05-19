import subprocess

res = subprocess.run([r".venv\Scripts\python", "fix_run.py"], capture_output=True, text=True)
print("STDOUT:")
print(res.stdout)
if res.stderr:
    print("STDERR:")
    print(res.stderr)
