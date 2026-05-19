import subprocess

def run(cmd):
    print(f"Running: {cmd}")
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.stdout: print(res.stdout)
    if res.stderr: print(res.stderr)

run("git add .")
run('git commit -m "Fix criteria 1-4: Kaggle Titanic Dataset, Autolog, Grafana 3 metrics, and Telegram Alert"')
run("git push origin main")
