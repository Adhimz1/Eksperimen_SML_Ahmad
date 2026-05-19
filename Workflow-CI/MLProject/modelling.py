import pandas as pd
import mlflow
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Aktifkan MLflow Autologging
mlflow.autolog()

print("Memuat dataset bersih...")
try:
    df = pd.read_csv('dataset_preprocessing/dataset_clean.csv')
except FileNotFoundError:
    df = pd.read_csv('../Workflow-CI/MLProject/dataset_preprocessing/dataset_clean.csv')

X = df[['Pclass', 'Age', 'Fare']]
y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

with mlflow.start_run():
    print("Memulai proses training...")
    rf = RandomForestClassifier(n_estimators=50, max_depth=5, random_state=42)
    rf.fit(X_train, y_train)
    
    # Karena kita menggunakan mlflow.autolog(), kita TIDAK PERLU lagi melakukan logging manual
    # seperti mlflow.sklearn.save_model() atau mlflow.log_metric().
    # Semuanya otomatis dicatat oleh autolog!
    
    y_pred = rf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Training selesai! Akurasi: {acc:.2f}")
    print("Silakan cek MLflow UI untuk melihat artefak yang otomatis tersimpan.")
