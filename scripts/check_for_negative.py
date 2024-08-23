def check_negative_values(dataframe, columns):
    """
    This function checks for negative values in specified columns of a DataFrame and prints the count of negative values for each column.
    
    Parameters:
    dataframe (pd.DataFrame): The DataFrame to check for negative values.
    columns (list): A list of column names to check for negative values.

    Returns:
    pd.Series: A series containing the count of negative values for each specified column.
    """
    negative_values = dataframe[columns].lt(0).sum()
    # print("\nNegative Values Count:\n", negative_values)
    return negative_values
