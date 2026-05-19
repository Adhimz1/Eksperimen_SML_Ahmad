import pandas as pd
import os

def load_data():
    print("Membaca dataset raw...")
    # Membaca file dataset dummy
    return pd.read_csv('../dataset_raw/dataset_dummy.csv')

def preprocess_data(df):
    print("Melakukan preprocessing (menghapus missing values)...")
    # Menghapus baris yang kosong (sama seperti di notebook)
    df_clean = df.dropna()
    return df_clean

def save_data(df):
    output_dir = 'dataset_preprocessing'
    # Memastikan folder output tersedia
    os.makedirs(output_dir, exist_ok=True) 
    
    # Menyimpan dataset yang sudah bersih
    output_path = f'{output_dir}/dataset_clean.csv'
    df.to_csv(output_path, index=False)
    print(f"Data bersih berhasil disimpan di {output_path}")

if __name__ == "__main__":
    raw_df = load_data()
    clean_df = preprocess_data(raw_df)
    save_data(clean_df)