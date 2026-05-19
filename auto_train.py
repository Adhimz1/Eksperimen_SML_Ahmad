import os
import shutil
import subprocess
import mlflow
import pandas as pd

# 1. Copy dataset_clean to all places where modelling.py might look for it
os.makedirs("dataset_preprocessing", exist_ok=True)
os.makedirs("Membangun_model/dataset_preprocessing", exist_ok=True)
shutil.copy("Workflow-CI/MLProject/dataset_preprocessing/dataset_clean.csv", "dataset_preprocessing/dataset_clean.csv")
shutil.copy("Workflow-CI/MLProject/dataset_preprocessing/dataset_clean.csv", "Membangun_model/dataset_preprocessing/dataset_clean.csv")

# 2. Train the model using python
print("Training model in Membangun_model...")
os.chdir("Membangun_model")
res1 = subprocess.run([r"..\.venv\Scripts\python", "modelling.py"], capture_output=True, text=True)
print(res1.stdout)
print(res1.stderr)
os.chdir("..")

print("Training model in Workflow-CI/MLProject...")
os.chdir("Workflow-CI/MLProject")
res2 = subprocess.run([r"..\..\.venv\Scripts\python", "modelling.py"], capture_output=True, text=True)
print(res2.stdout)
print(res2.stderr)
os.chdir("../..")

# 3. Get the latest RUN_ID
try:
    runs = mlflow.search_runs(order_by=["start_time desc"], max_results=1)
    if not runs.empty:
        latest_run_id = runs.iloc[0].run_id
        print(f"LATEST RUN ID: {latest_run_id}")
        
        # 4. Update inference.py
        inference_file = "Monitoring dan Logging/7.inference.py"
        with open(inference_file, "r") as f:
            content = f.read()
        
        # Replace the dummy run id
        import re
        content = re.sub(r'runs:/[^/]+/model', f'runs:/{latest_run_id}/model', content)
        
        with open(inference_file, "w") as f:
            f.write(content)
        print("Updated 7.inference.py with latest run id")
        
        # 5. Run inference
        print("Running inference...")
        res3 = subprocess.run([r".venv\Scripts\python", inference_file], capture_output=True, text=True)
        print("--- INFERENCE OUTPUT ---")
        print(res3.stdout)
    else:
        print("No MLflow runs found.")
except Exception as e:
    print(f"Failed to get run id: {e}")

