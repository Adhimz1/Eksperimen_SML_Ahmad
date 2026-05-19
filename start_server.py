import os
import subprocess
import time
import sys

# Tambahkan .venv\Scripts ke PATH agar mlflow bisa menemukan waitress-serve
os.environ["PATH"] = os.path.abspath(r".venv\Scripts") + os.pathsep + os.environ.get("PATH", "")

def find_all_models():
    found_models = []
    for root, dirs, files in os.walk("."):
        if "MLmodel" in files:
            found_models.append(root)
    return found_models

models = find_all_models()
if not models:
    print("SANGAT ANEH: Tidak ada model MLFlow yang tersimpan di seluruh folder proyek ini!")
    sys.exit(1)

best_model_path = models[0]
print(f"Menggunakan model dari path: {best_model_path}")

print("\n1. Menyalakan MLFlow Serve API (port 5005) di background...")
# Run MLFlow serve without conda for faster boot
mlflow_cmd = [r".venv\Scripts\mlflow", "models", "serve", "-m", best_model_path, "-p", "5005", "--env-manager", "local"]
subprocess.Popen(mlflow_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("MLFlow Serve API berjalan!")

time.sleep(5) # Tunggu 5 detik agar port 5005 siap

print("\n2. Menyalakan Docker Prometheus...")
subprocess.run("docker start prometheus_baru", shell=True)

print("3. Menyalakan Docker Grafana...")
subprocess.run("docker start goofy_curran", shell=True)

print("\n4. Menyalakan Flask API / Prometheus Exporter (port 8000)...")
print("Buka terminal baru untuk menjalankan 7.inference.py agar metrik naik!")
subprocess.run([r".venv\Scripts\python", r"Monitoring dan Logging\3.prometheus_exporter.py"])
