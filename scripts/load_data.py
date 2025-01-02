
import pandas as pd

def load_file(file_path):
    try:
          df = pd.read_csv(file_path)
    except Exception as e:
         print(f'File not found: {e}')
    
    return df