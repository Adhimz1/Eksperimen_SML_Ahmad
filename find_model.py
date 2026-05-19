import os
for root, dirs, files in os.walk("."):
    if "MLmodel" in files:
        print("Model found at:", root)
