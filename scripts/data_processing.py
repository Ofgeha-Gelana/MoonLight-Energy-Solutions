import pandas as pd

import os, sys

rpath = os.path.abspath('..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)



def fetch_data(file_path='path/to/your/datafile.csv'):
    """
    Fetches data from a CSV file and sets the index to the 'Timestamp' column.
    """
    df = pd.read_csv(file_path, parse_dates=['Timestamp'])
    df.set_index('Timestamp', inplace=True)
    return df

def clean_data(df):
    """
    Cleans the data by handling missing values and anomalies.
    """
    # Drop rows with NaN values in critical columns
    df = df.dropna(subset=['GHI', 'DNI', 'DHI'])
    
    # Remove or replace outliers (e.g., negative values)
    df = df[df['GHI'] >= 0]
    df = df[df['DNI'] >= 0]
    df = df[df['DHI'] >= 0]
    
    # Replace 'Comments' column if needed (e.g., fill missing values)
    df['Comments'].fillna('No Comment', inplace=True)
    
    return df

