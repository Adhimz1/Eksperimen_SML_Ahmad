import nbformat as nbf

notebook_path = 'c:/Users/ahmad/Eksperimen_SML_Ahmad/Eksperimen_Ahmad.ipynb'

# Read existing notebook
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

# Create new cells based on the MSML Template
md_intro = nbf.v4.new_markdown_cell("""# 1. Perkenalan Dataset

Dataset ini adalah dataset dummy tentang prediksi kelulusan siswa berdasarkan umur dan nilai ujian.
**Sumber Dataset**: Dibuat secara mandiri / dummy data untuk eksperimen.
**Deskripsi**: Terdiri dari kolom `id`, `umur`, `nilai_ujian`, dan target `status_lulus`.
""")

md_import = nbf.v4.new_markdown_cell("""# 2. Import Library

Pada tahap ini, kita mengimpor pustaka (library) Python yang dibutuhkan.
""")

md_load = nbf.v4.new_markdown_cell("""# 3. Memuat Dataset

Memuat dataset raw ke dalam notebook.
""")

md_preprocess = nbf.v4.new_markdown_cell("""# 5. Preprocessing Data

Membersihkan data dari missing values dan menyimpannya.
""")

# Code cell for to_csv
code_save = nbf.v4.new_code_cell("""# Menyimpan dataset bersih ke folder dataset_preprocessing
import os
os.makedirs('Membangun_model/dataset_preprocessing', exist_ok=True)
df_clean.to_csv('Membangun_model/dataset_preprocessing/dataset_clean.csv', index=False)
print("Dataset berhasil disimpan ke dataset_clean.csv!")
""")

# We have 3 existing cells in the notebook.
existing_cell_1 = nb.cells[0] # The one with import pandas and read_csv
existing_cell_2 = nb.cells[1] # df.info
existing_cell_3 = nb.cells[2] # dropna

# Split the first cell into import and load data
import_code = "import pandas as pd\nimport os"
load_code = "df = pd.read_csv('dataset_raw/dataset_dummy.csv')\ndisplay(df)"

code_import = nbf.v4.new_code_cell(import_code)
code_load = nbf.v4.new_code_cell(load_code)

# Reconstruct notebook cells
md_eda = nbf.v4.new_markdown_cell("""# 4. Exploratory Data Analysis (EDA)

Mengecek info dataset dan mendeteksi jumlah missing values.
""")

new_cells = [
    md_intro,
    md_import,
    code_import,
    md_load,
    code_load,
    md_eda,
    existing_cell_2,
    md_preprocess,
    existing_cell_3,
    code_save
]

nb.cells = new_cells

with open(notebook_path, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print("Notebook berhasil diperbarui dengan template MSML!")
