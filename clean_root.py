import os
import shutil

root_dir = "c:/Users/ahmad/Eksperimen_SML_Ahmad"
keep_dirs = {".git", ".github", ".venv", "Membangun_model", "Monitoring dan Logging", "Workflow-CI", "dataset_raw", "preprocessing"}
keep_files = {".gitignore", "Eksperimen_SML_Ahmad.txt"}

for item in os.listdir(root_dir):
    path = os.path.join(root_dir, item)
    if os.path.isdir(path):
        if item not in keep_dirs:
            print(f"Deleting directory: {item}")
            try: shutil.rmtree(path)
            except: pass
    else:
        if item not in keep_files and not item.endswith('.py'):
            print(f"Deleting file: {item}")
            try: os.remove(path)
            except: pass

# Delete .py files manually except this script itself for now, or just let it delete everything
for item in os.listdir(root_dir):
    if item.endswith('.py') and item != 'clean_root.py':
        path = os.path.join(root_dir, item)
        print(f"Deleting python script: {item}")
        try: os.remove(path)
        except: pass
