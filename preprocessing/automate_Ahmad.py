import pandas as pd
import os
import argparse

def process_data(input_path, output_path):
    print(f"Memuat data dari: {input_path}")
    df = pd.read_csv(input_path)
    
    print("Memilih fitur Pclass, Age, Fare dan target Survived...")
    df_selected = df[['Pclass', 'Age', 'Fare', 'Survived']].copy()
    
    print("Menghapus baris dengan missing values...")
    df_clean = df_selected.dropna()
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_clean.to_csv(output_path, index=False)
    print(f"Data bersih disimpan ke: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default='../dataset_raw/titanic.csv', help='Path ke file raw dataset')
    parser.add_argument('--output', type=str, default='dataset_preprocessing/dataset_clean.csv', help='Path ke file output')
    args = parser.parse_args()
    
    process_data(args.input, args.output)