import pandas as pd
try:
    df = pd.read_csv("Workflow-CI/MLProject/dataset_preprocessing/dataset_clean.csv")
    print(df.head(2))
except Exception as e:
    print(e)
