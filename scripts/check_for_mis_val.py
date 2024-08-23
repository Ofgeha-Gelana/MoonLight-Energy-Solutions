def check_missing_values(dataframe):
    """
    This function checks for missing values in a given DataFrame and prints the count of missing values for each column.

    Returns:
    pd.Series: A series containing the count of missing values for each column.
    """
    missing_values = dataframe.isnull().sum()
    # print("Missing Values:\n", missing_values)
    return missing_values
