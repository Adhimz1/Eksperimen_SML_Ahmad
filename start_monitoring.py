import subprocess
import time
import os

print("1. Menyalakan Prometheus Exporter...")
subprocess.Popen([r".venv\Scripts\python", r"Monitoring dan Logging\3.prometheus_exporter.py"])
time.sleep(2)

print("2. Menyalakan Docker Prometheus...")
res = subprocess.run("docker start prometheus_baru", shell=True, capture_output=True)
if res.returncode != 0:
    # Buat container baru jika belum ada
    subprocess.run('docker run -d -p 9090:9090 --name prometheus_baru -v "C:\\Users\\ahmad\\Eksperimen_SML_Ahmad\\Monitoring dan Logging\\2.prometheus.yml":/etc/prometheus/prometheus.yml prom/prometheus', shell=True)

print("3. Menyalakan Docker Grafana...")
subprocess.run("docker start goofy_curran", shell=True)

print("\n✅ Semua sistem Monitoring telah menyala! Grafiknya akan muncul di Grafana dalam 10-20 detik.")
