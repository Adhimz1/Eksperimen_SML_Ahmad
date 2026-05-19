import os
import pandas as pd
import nbformat as nbf

# 1. Download Titanic
print("Downloading Titanic dataset...")
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
os.makedirs('dataset_raw', exist_ok=True)
df = pd.read_csv(url)
df.to_csv('dataset_raw/titanic.csv', index=False)
print("Saved to dataset_raw/titanic.csv")

# 2. Rebuild Notebook
nb = nbf.v4.new_notebook()

md_intro = nbf.v4.new_markdown_cell("""# 1. Perkenalan Dataset

Dataset yang digunakan dalam eksperimen ini adalah **Titanic Dataset**.
**Sumber Dataset**: Kaggle (https://www.kaggle.com/c/titanic/data)
**Deskripsi**: Dataset ini berisi data penumpang kapal Titanic. Tujuan klasifikasi adalah memprediksi apakah seorang penumpang selamat (`Survived` = 1) atau tidak (`Survived` = 0) berdasarkan fitur-fitur seperti kelas tiket (`Pclass`), umur (`Age`), dan tarif penumpang (`Fare`).
""")

md_import = nbf.v4.new_markdown_cell("""# 2. Import Library

Pada tahap ini, kita mengimpor pustaka (library) Python yang dibutuhkan untuk manipulasi data dan visualisasi.
""")

code_import = nbf.v4.new_code_cell("""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
""")

md_load = nbf.v4.new_markdown_cell("""# 3. Memuat Dataset

Memuat dataset raw `titanic.csv` ke dalam DataFrame.
""")

code_load = nbf.v4.new_code_cell("""df = pd.read_csv('../dataset_raw/titanic.csv')
display(df.head())
""")

md_eda = nbf.v4.new_markdown_cell("""# 4. Exploratory Data Analysis (EDA)

Melakukan eksplorasi untuk melihat informasi tipe data, mengecek *missing values*, dan melihat distribusi kelas target (Survived).
""")

code_eda = nbf.v4.new_code_cell("""print("--- Info Dataset ---")
df.info()

print("\\n--- Jumlah Missing Values ---")
print(df.isnull().sum())

# Plot distribusi target
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='Survived')
plt.title('Distribusi Penumpang Selamat (1) dan Tidak (0)')
plt.show()

# Plot hubungan Umur dan Keselamatan
plt.figure(figsize=(8,5))
sns.histplot(data=df, x='Age', hue='Survived', kde=True)
plt.title('Distribusi Umur berdasarkan Keselamatan')
plt.show()
""")

md_preprocess = nbf.v4.new_markdown_cell("""# 5. Preprocessing Data

Membersihkan data dari missing values (khususnya pada kolom `Age`) dan memilih fitur utama (`Pclass`, `Age`, `Fare`) beserta target (`Survived`).
""")

code_preprocess = nbf.v4.new_code_cell("""# Memilih kolom yang relevan saja untuk eksperimen ini
df_selected = df[['Pclass', 'Age', 'Fare', 'Survived']].copy()

# Menghapus baris yang memiliki missing values pada kolom Age
df_clean = df_selected.dropna()

print("--- Dataset setelah dibersihkan dan difilter ---")
display(df_clean.head())
""")

code_save = nbf.v4.new_code_cell("""# Menyimpan dataset bersih
os.makedirs('../Workflow-CI/MLProject/dataset_preprocessing', exist_ok=True)
df_clean.to_csv('../Workflow-CI/MLProject/dataset_preprocessing/dataset_clean.csv', index=False)

# Juga simpan ke folder preprocessing (untuk jaga-jaga kriteria)
os.makedirs('dataset_preprocessing', exist_ok=True)
df_clean.to_csv('dataset_preprocessing/dataset_clean.csv', index=False)

print("Dataset berhasil disimpan!")
""")

nb.cells = [md_intro, md_import, code_import, md_load, code_load, md_eda, code_eda, md_preprocess, code_preprocess, code_save]

notebook_path = 'preprocessing/Eksperimen_Ahmad.ipynb'
os.makedirs('preprocessing', exist_ok=True)
with open(notebook_path, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print(f"Notebook {notebook_path} successfully generated.")
