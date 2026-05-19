import pandas as pd
import mlflow
from sklearn.model_selection import train_test_split, GridSearchCV
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
    print("Memulai proses hyperparameter tuning...")
    rf = RandomForestClassifier(random_state=42)
    
    param_grid = {
        'n_estimators': [10, 50],
        'max_depth': [3, 5]
    }
    
    grid = GridSearchCV(rf, param_grid, cv=3)
    grid.fit(X_train, y_train)
    
    print("Tuning selesai!")
    print(f"Best params: {grid.best_params_}")
    print(f"Best score: {grid.best_score_:.2f}")