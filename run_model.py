import os
import subprocess
import sys

def run(cmd):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout: print(result.stdout)
    if result.stderr: print(result.stderr)

python_exe = os.path.abspath(".venv/Scripts/python.exe")

os.chdir("Workflow-CI/MLProject")
run(f'"{python_exe}" modelling.py')

os.chdir("../../Membangun_model")
run(f'"{python_exe}" modelling.py')
