import time
import random
import psutil
from prometheus_client import start_http_server, Counter, Gauge, Summary

# --- 10 METRIK UNTUK TARGET ADVANCE GRAFANA ---
# 1-2. Counter
REQUEST_COUNT = Counter('model_request_total', 'Total prediksi yang diminta')
ERROR_COUNT = Counter('model_error_total', 'Total error saat prediksi')
# 3-4. Gauge (Hardware)
CPU_USAGE = Gauge('system_cpu_usage_percent', 'Penggunaan CPU sistem')
MEMORY_USAGE = Gauge('system_memory_usage_mb', 'Penggunaan Memori sistem')
# 5. Summary (Latency)
REQUEST_LATENCY = Summary('model_request_latency_seconds', 'Waktu respons model')
# 6-7. Gauge (Bisnis/Prediksi)
ACTIVE_REQUESTS = Gauge('model_active_requests', 'Jumlah request yang sedang diproses')
PREDICTION_SCORE = Gauge('model_prediction_score', 'Skor probabilitas prediksi terakhir')
# 8-9. Counter (Hasil Prediksi)
LULUS_COUNT = Counter('model_prediction_lulus_total', 'Total prediksi status lulus')
GAGAL_COUNT = Counter('model_prediction_gagal_total', 'Total prediksi status gagal')
# 10. Gauge (Data Drift - Simulasi)
DATA_DRIFT = Gauge('model_data_drift_score', 'Indikator pergeseran data')

@REQUEST_LATENCY.time()
def process_request():
    ACTIVE_REQUESTS.inc()
    REQUEST_COUNT.inc()
    
    time.sleep(random.uniform(0.1, 0.5)) # Simulasi latency
    
    # Simulasi prediksi
    if random.random() > 0.1:
        score = random.uniform(0.6, 0.99)
        PREDICTION_SCORE.set(score)
        if score > 0.7:
            LULUS_COUNT.inc()
        else:
            GAGAL_COUNT.inc()
    else:
        ERROR_COUNT.inc()
        
    ACTIVE_REQUESTS.dec()

def update_system_metrics():
    CPU_USAGE.set(psutil.cpu_percent())
    MEMORY_USAGE.set(psutil.virtual_memory().used / (1024 * 1024))
    DATA_DRIFT.set(random.uniform(0.01, 0.05))

if __name__ == '__main__':
    start_http_server(8000)
    print("Prometheus Exporter berjalan di http://localhost:8000")
    
    while True:
        process_request()
        update_system_metrics()
        time.sleep(2)