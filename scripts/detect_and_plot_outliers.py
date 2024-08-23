import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def detect_and_plot_outliers(dataframe, columns, threshold=3):
    """
    This function calculates Z-scores for the specified columns in the DataFrame, 
    flags data points with Z-scores beyond the given threshold, and plots the data 
    with outliers highlighted.

    Parameters:
    dataframe (pd.DataFrame): The DataFrame containing the data.
    columns (list of str): The list of columns to analyze for outliers.
    threshold (float): The Z-score threshold for flagging outliers (default is 3).

    Returns:
    pd.DataFrame: A DataFrame containing the data points identified as outliers.
    """
    # Calculate Z-scores for each column
    z_scores = pd.DataFrame()
    
    for col in columns:
        z_scores[col] = (dataframe[col] - dataframe[col].mean()) / dataframe[col].std()

    # Flag data points with Z-scores beyond the threshold
    outliers = (z_scores.abs() > threshold)

    # Extract data points identified as outliers
    outliers_data = dataframe[outliers.any(axis=1)]

    # Display the outliers
    print("Outliers identified:")
    print(outliers_data)

    # Optionally, visualize outliers
    for col in columns:
        plt.figure(figsize=(10, 5))
        plt.plot(dataframe.index, dataframe[col], label=col)
        plt.scatter(outliers_data.index, outliers_data[col], color='red', label='Outliers')
        plt.title(f"{col} with Outliers")
        plt.xlabel('Time')
        plt.ylabel(col)
        plt.legend()
        plt.grid(True)
        plt.show()
    
    return outliers_data

