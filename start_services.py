import subprocess
import os

print("Memulai Docker Grafana...")
res1 = subprocess.run("docker start goofy_curran", shell=True, capture_output=True, text=True)
if res1.returncode == 0:
    print("✅ Grafana berhasil dinyalakan! (Buka http://localhost:3000)")
else:
    print(f"❌ Gagal menyalakan Grafana. Error: {res1.stderr}")

print("\nMemulai MLFlow UI di background...")
os.chdir("Membangun_model")
# Start MLFlow as a detached process
subprocess.Popen([r"..\.venv\Scripts\mlflow", "ui"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("✅ MLFlow UI berhasil dinyalakan! (Buka http://localhost:5000)")

print("\nSilakan buka browser Anda sekarang.")
