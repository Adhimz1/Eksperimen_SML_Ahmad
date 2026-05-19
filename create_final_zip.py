import os
import zipfile

def create_submission_zip():
    zip_name = "Submission_Eksperimen_SML_Ahmad_Final.zip"
    
    # Tambahkan Workflow-CI.txt!
    allowed_items = [
        "dataset_raw",
        "preprocessing",
        "Membangun_model",
        "Workflow-CI",
        "Monitoring dan Logging",
        "Eksperimen_SML_Ahmad.txt",
        "Workflow-CI.txt"
    ]
    
    print(f"Membuat {zip_name} yang sangat BERSIH khusus untuk reviewer...")
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for item in allowed_items:
            if os.path.exists(item):
                if os.path.isdir(item):
                    for root, dirs, files in os.walk(item):
                        if "__pycache__" in root or ".ipynb_checkpoints" in root:
                            continue
                        for file in files:
                            file_path = os.path.join(root, file)
                            zipf.write(file_path, file_path)
                            print(f"Menambahkan: {file_path}")
                else:
                    zipf.write(item, item)
                    print(f"Menambahkan: {item}")
            else:
                print(f"PERINGATAN: {item} tidak ditemukan!")

    print(f"\nSelesai! File {zip_name} telah berhasil dibuat!")
    print("Silakan upload file zip ini ke Dicoding.")

if __name__ == "__main__":
    create_submission_zip()
