import requests
import json
import time

def run_inference():
    # URL Flask API yang berjalan (bukan langsung ke MLFlow)
    url = "http://127.0.0.1:8000/predict"
    
    # Payload format MLFlow "dataframe_split"
    payload = {
        "dataframe_split": {
            "columns": ["Pclass", "Age", "Fare"],
            "data": [
                [3, 22.0, 7.25],
                [1, 38.0, 71.28],
                [3, 26.0, 7.92]
            ]
        }
    }
    
    print(f"Mengirim request ke Flask API di {url}...")
    try:
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            print("\n=== HASIL INFERENCE BUKTI MELALUI FLASK API ===")
            predictions = response.json().get('predictions', [])
            for i, pred in enumerate(predictions):
                status = "Selamat (Survived)" if pred == 1 else "Tidak Selamat"
                print(f"Penumpang {i+1} -> Prediksi: {pred} ({status})")
        else:
            print(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"Gagal menghubungi server. Pastikan Flask API dan MLFlow Serve sudah berjalan! Error: {e}")

if __name__ == "__main__":
    while True:
        run_inference()
        time.sleep(2) # Kirim request setiap 2 detik agar grafik Prometheus naik
