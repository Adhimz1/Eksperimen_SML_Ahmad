import os
import mlflow.pyfunc
import pandas as pd

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
    print(f"Loading model dari path fisik: {best_model_path}")
    
    try:
        loaded_model = mlflow.pyfunc.load_model(best_model_path)
        data = pd.DataFrame({
            'Pclass': [3, 1, 3],
            'Age': [22.0, 38.0, 26.0],
            'Fare': [7.25, 71.28, 7.92]
        })
        print("\nData untuk diprediksi:")
        print(data)
        
        predictions = loaded_model.predict(data)
        
        print("\n=== HASIL INFERENCE ===")
        for i, pred in enumerate(predictions):
            status = "Selamat (Survived)" if pred == 1 else "Tidak Selamat"
            print(f"Penumpang {i+1} -> Prediksi: {pred} ({status})")
            
    except Exception as e:
        print(f"Error loading model: {e}")
