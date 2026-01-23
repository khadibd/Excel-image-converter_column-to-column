import os, pandas as pd

def create_report(results, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    pd.DataFrame(results).to_excel(path, index=False)
