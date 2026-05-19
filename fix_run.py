import mlflow
import subprocess
import os
import re

# Set tracking URI to the one inside Membangun_model
mlflow.set_tracking_uri("file:./Membangun_model/mlruns")

try:
    runs = mlflow.search_runs(order_by=["start_time desc"], max_results=1)
    if not runs.empty:
        latest_run_id = runs.iloc[0].run_id
        print(f"=== LATEST RUN ID DITEMUKAN: {latest_run_id} ===")
        
        # 4. Update inference.py
        inference_file = "Monitoring dan Logging/7.inference.py"
        with open(inference_file, "r") as f:
            content = f.read()
        
        # Replace the dummy run id
        content = re.sub(r'runs:/[^/]+/model', f'runs:/{latest_run_id}/model', content)
        
        with open(inference_file, "w") as f:
            f.write(content)
        print("[OK] File 7.inference.py berhasil di-update dengan Run ID terbaru!")
        
        # 5. Run inference
        print("\nSedang menjalankan Inference...\n")
        res3 = subprocess.run([r".venv\Scripts\python", inference_file], capture_output=True, text=True)
        print(res3.stdout)
        if res3.stderr:
            print("Error:", res3.stderr)
    else:
        print("No MLflow runs found in Membangun_model.")
except Exception as e:
    print(f"Failed to get run id: {e}")
