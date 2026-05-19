import subprocess
res = subprocess.run("docker ps -a", shell=True, capture_output=True, text=True)
print(res.stdout)
