import pandas as pd
import os
import mlflow
import mlflow.sklearn
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ==========================================
# 1. KONFIGURASI DAGSHUB (ISI BAGIAN INI)
# ==========================================
DAGSHUB_USERNAME = "Adhimz1"
DAGSHUB_TOKEN = "34a973da619af7ba7165e6b06f251db939bba4e1" 
DAGSHUB_URI = "https://dagshub.com/Adhimz1/Eksperimen_SML_Ahmad.mlflow"

# Set environment variable agar MLflow bisa login otomatis
os.environ['MLFLOW_TRACKING_USERNAME'] = DAGSHUB_USERNAME
os.environ['MLFLOW_TRACKING_PASSWORD'] = DAGSHUB_TOKEN

mlflow.set_tracking_uri(DAGSHUB_URI)
mlflow.set_experiment("Eksperimen_Tuning_Ahmad")

# ==========================================
# 2. LOAD DATA & SPLIT
# ==========================================
print("Membaca dataset bersih...")
df = pd.read_csv('dataset_preprocessing/dataset_clean.csv')

# Pisahkan fitur (X) dan target (y). Hapus 'id' karena tidak relevan
X = df[['umur', 'nilai_ujian']]
y = df['status_lulus']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==========================================
# 3. HYPERPARAMETER TUNING & MANUAL LOGGING
# ==========================================
# Matikan autolog karena kita mengejar target Advance (Manual Logging)
mlflow.autolog(disable=True) 

with mlflow.start_run(run_name="RandomForest_Tuning"):
    print("Memulai Hyperparameter Tuning...")
    
    # Menyiapkan model dan parameter yang akan di-tuning
    rf = RandomForestClassifier(random_state=42)
    param_grid = {
        'n_estimators': [10, 50],
        'max_depth': [2, 5]
    }
    
    # Karena data dummy kita sangat kecil, cv (cross-validation) diset 2
    grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=2)
    grid_search.fit(X_train, y_train)
    
    # Ambil model terbaik
    best_model = grid_search.best_estimator_
    
    # Prediksi ke data test
    y_pred = best_model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Model terbaik ditemukan dengan akurasi: {accuracy}")

    # --- MANUAL LOGGING PARAMETER & METRICS ---
    mlflow.log_params(grid_search.best_params_)
    mlflow.log_metric("accuracy", accuracy)
    
    # --- MEMBUAT & MENYIMPAN 2 ARTEFAK (SYARAT ADVANCE) ---
    print("Membuat artefak tambahan...")
    os.makedirs("artefak", exist_ok=True)
    
    # Artefak 1: Plot Confusion Matrix (.png)
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix')
    plt.ylabel('Aktual')
    plt.xlabel('Prediksi')
    cm_path = "artefak/confusion_matrix.png"
    plt.savefig(cm_path)
    plt.close()
    
    # Artefak 2: Classification Report (.txt)
    report = classification_report(y_test, y_pred, zero_division=0)
    report_path = "artefak/classification_report.txt"
    with open(report_path, "w") as f:
        f.write(report)
        
    # --- MANUAL LOGGING ARTIFACTS & MODEL ---
    mlflow.log_artifact(cm_path)
    mlflow.log_artifact(report_path)
    
    # Log model ke MLflow
    mlflow.sklearn.log_model(best_model, "random_forest_model")
    
    print("Semua proses selesai! Hasil telah dikirim ke DagsHub.")