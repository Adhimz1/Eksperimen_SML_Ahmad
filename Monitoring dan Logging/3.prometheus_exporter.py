from flask import Flask, request, jsonify, Response
import requests
import time
import psutil
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Metrik untuk API model
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests')
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP Request Latency')
THROUGHPUT = Counter('http_requests_throughput', 'Total number of requests per second')

# Metrik untuk sistem
CPU_USAGE = Gauge('system_cpu_usage', 'CPU Usage Percentage')
RAM_USAGE = Gauge('system_ram_usage', 'RAM Usage Percentage')

# Tambahan 1 metrik untuk genapkan jadi 3 metrik yang berjalan terus
DATA_DRIFT = Gauge('model_data_drift_score', 'Data Drift Simulator')
import random

@app.route('/metrics', methods=['GET'])
def metrics():
    # Update metrik sistem setiap kali /metrics diakses
    CPU_USAGE.set(psutil.cpu_percent(interval=1))
    RAM_USAGE.set(psutil.virtual_memory().percent)
    DATA_DRIFT.set(random.uniform(0.01, 0.05)) # Simulasi drift
    
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.route('/predict', methods=['POST'])
def predict():
    start_time = time.time()
    REQUEST_COUNT.inc()
    THROUGHPUT.inc()
    
    # Kirim request ke MLFlow Serve API model
    # Format MLFlow Serve menerima "dataframe_split" atau "dataframe_records"
    api_url = "http://127.0.0.1:5005/invocations"
    data = request.get_json()
    
    try:
        response = requests.post(api_url, json=data)
        duration = time.time() - start_time
        REQUEST_LATENCY.observe(duration)
        
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Menjalankan Flask Prometheus Exporter di http://127.0.0.1:8000")
    app.run(host='127.0.0.1', port=8000)