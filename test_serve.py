import os
import subprocess

def find_all_models():
    found_models = []
    for root, dirs, files in os.walk("."):
        if "MLmodel" in files:
            found_models.append(root)
    return found_models

models = find_all_models()
if not models:
    print("SANGAT ANEH: Tidak ada model MLFlow yang tersimpan di seluruh folder proyek ini!")
else:
    best_model_path = models[0]
    print(f"Menggunakan model dari path: {best_model_path}")
    mlflow_cmd = [r".venv\Scripts\mlflow", "models", "serve", "-m", best_model_path, "-p", "5005", "--env-manager", "local"]
    print("Menjalankan:", " ".join(mlflow_cmd))
    try:
        res = subprocess.run(mlflow_cmd, capture_output=True, text=True, timeout=10)
        print("STDOUT:", res.stdout)
        print("STDERR:", res.stderr)
    except subprocess.TimeoutExpired as e:
        print("Timed out, which means it probably started successfully!")
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)
