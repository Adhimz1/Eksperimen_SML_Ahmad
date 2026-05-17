import pandas as pd
import os
import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("Basic_ML_Experiment")

df = pd.read_csv('dataset_preprocessing/dataset_clean.csv')
X = df[['umur', 'nilai_ujian']]
y = df['status_lulus']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

input_example = X_train.head(1)

with mlflow.start_run(run_name="RandomForest_Basic"):
    rf = RandomForestClassifier(n_estimators=10, max_depth=2, random_state=42)
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    signature = infer_signature(X_train, y_pred)
    mlflow.log_param("model", "RandomForest")
    mlflow.log_metric("accuracy", acc)
    mlflow.sklearn.log_model(rf, "random_forest_model", signature=signature, input_example=input_example)

with mlflow.start_run(run_name="LogisticRegression_Basic"):
    lr = LogisticRegression(random_state=42)
    lr.fit(X_train, y_train)
    y_pred = lr.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    signature = infer_signature(X_train, y_pred)
    mlflow.log_param("model", "LogisticRegression")
    mlflow.log_metric("accuracy", acc)
    mlflow.sklearn.log_model(lr, "logistic_regression_model", signature=signature, input_example=input_example)
