import pandas as pd
import mlflow
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

mlflow.autolog()

print("Memuat dataset bersih...")
try:
    df = pd.read_csv('dataset_preprocessing/dataset_clean.csv')
except FileNotFoundError:
    df = pd.read_csv('../dataset_preprocessing/dataset_clean.csv')

X = df[['umur', 'nilai_ujian']]
y = df['status_lulus']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

with mlflow.start_run():
    print("Memulai proses training...")
    rf = RandomForestClassifier(n_estimators=10, max_depth=2, random_state=42)
    rf.fit(X_train, y_train)
    
    # Simpan artefak model untuk pipeline CI
    os.makedirs('model_artefak', exist_ok=True)
    mlflow.sklearn.save_model(rf, "model_artefak")
    print("Model berhasil disimpan ke model_artefak!")
