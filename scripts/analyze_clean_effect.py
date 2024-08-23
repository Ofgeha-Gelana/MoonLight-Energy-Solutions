import pandas as pd

def analyze_cleaning_effects(dataframe, cleaning_column='Cleaning', sensors=['ModA', 'ModB']):
    """
    Analyzes the mean sensor readings before and after cleaning events.

    Parameters:
    - dataframe (pd.DataFrame): The input DataFrame containing sensor data and cleaning events.
    - cleaning_column (str): The name of the column indicating cleaning events.
    - sensors (list): A list of column names corresponding to sensor readings.

    Returns:
    - mean_before_cleaning (pd.Series): Mean sensor readings before cleaning events.
    - mean_after_cleaning (pd.Series): Mean sensor readings after cleaning events.
    """
    # Convert 'Cleaning' column to a boolean where 1 represents a cleaning event
    dataframe[cleaning_column] = dataframe[cleaning_column].astype(bool)

    # Group data into before and after cleaning events
    before_cleaning = dataframe[dataframe[cleaning_column] == False]
    after_cleaning = dataframe[dataframe[cleaning_column] == True]

    # Calculate mean sensor readings before and after cleaning
    mean_before_cleaning = before_cleaning[sensors].mean()
    mean_after_cleaning = after_cleaning[sensors].mean()

    # Display the results
    print("Mean sensor readings before cleaning:")
    print(mean_before_cleaning)

    print("\nMean sensor readings after cleaning:")
    print(mean_after_cleaning)

    return mean_before_cleaning, mean_after_cleaning

