import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import os
import shutil

df = pd.read_csv('dataset_preprocessing/dataset_clean.csv')
X = df[['umur', 'nilai_ujian']]
y = df['status_lulus']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

with mlflow.start_run():
    rf = RandomForestClassifier(n_estimators=10, max_depth=2, random_state=42)
    rf.fit(X_train, y_train)
    mlflow.log_metric("accuracy", rf.score(X_test, y_test))
    
    # Simpan model untuk log bawaan MLflow
    mlflow.sklearn.log_model(rf, "model")
    
    # Ekspor model ke folder agar mudah dibaca oleh Docker di GitHub Actions
    if os.path.exists("model_artefak"):
        shutil.rmtree("model_artefak")
    mlflow.sklearn.save_model(rf, "model_artefak")
    
    print("Model berhasil dilatih dan disimpan ke folder model_artefak!")