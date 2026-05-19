import os
import zipfile

def zip_directory(folder_path, zip_path):
    print("Mulai membuat file ZIP...")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            # Exclude folders
            dirs[:] = [d for d in dirs if d not in ['.venv', '.git', '__pycache__']]
            
            for file in files:
                # Exclude specific files if needed
                if file == os.path.basename(zip_path):
                    continue
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)
    print(f"Selesai! File ZIP tersimpan di: {zip_path}")

# Run it
zip_directory('.', 'Submission_Eksperimen_SML_Ahmad.zip')
