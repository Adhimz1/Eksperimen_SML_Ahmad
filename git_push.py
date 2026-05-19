import os
import subprocess

def run(cmd):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout: print(result.stdout)
    if result.stderr: print(result.stderr)

run("git add .")
run('git commit -m "Fix criteria 1-4 with Titanic dataset and autolog"')
run("git push origin main")
