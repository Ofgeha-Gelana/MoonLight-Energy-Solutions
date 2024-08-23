import pandas as pd
import numpy as np

# Function for data cleaning
def clean_data(df):
    """
    Cleans the dataset by performing the following steps:
    1. Drops irrelevant columns like 'Comments'.
    2. Handles missing values by dropping rows with missing critical data and applying forward/backward fill.
    3. Handles anomalies by replacing negative values with NaN.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to clean.
    
    Returns:
    pd.DataFrame: The cleaned DataFrame.
    """
    # Step 1: Drop irrelevant columns like 'Comments' which are entirely null
    df_cleaned = df.drop(columns=['Comments'], errors='ignore')
    
    # Step 2: Handle missing values
    # Drop rows with missing values in critical columns (e.g., GHI, DNI, DHI, ModA, ModB)
    df_cleaned = df_cleaned.dropna(subset=['GHI', 'DNI', 'DHI', 'ModA', 'ModB'])

    # Optionally, fill remaining missing values with forward fill, backward fill, or mean
    df_cleaned.fillna(method='ffill', inplace=True)
    df_cleaned.fillna(method='bfill', inplace=True)
    
    # Step 3: Handle anomalies
    # Replace negative values with NaN, assuming negative values are not valid
    columns_to_check = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'Tamb', 'RH', 'WS', 'WSgust', 'WD', 'BP']
    df_cleaned[columns_to_check] = df_cleaned[columns_to_check].applymap(lambda x: np.nan if x < 0 else x)

    # Drop rows with NaN values created after replacing negative values
    df_cleaned.dropna(inplace=True)

    return df_cleaned

