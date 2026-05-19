import os

for root, dirs, files in os.walk("."):
    if "mlruns" in root:
        for f in files:
            print(os.path.join(root, f))
