# data_loader.py

import pandas as pd

def load_file(file_path):
    """
    Load data from a CSV file into a DataFrame.
    
    Parameters:
    - file_path: str, path to the CSV file
    
    Returns:
    - DataFrame containing the data from the CSV file
    """
    return pd.read_csv(file_path)
