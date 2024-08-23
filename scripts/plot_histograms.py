import matplotlib.pyplot as plt

def plot_histograms(dataframe, variables):
    """
    This function creates histograms for a list of specified variables in the given DataFrame.
    
    Parameters:
    dataframe (pd.DataFrame): The DataFrame containing the data.
    variables (list of str): A list of column names for which histograms should be plotted.
    
    Returns:
    None
    """
    # Create a figure to hold the subplots
    plt.figure(figsize=(14, 12))

    # Loop through each variable and create a histogram
    for i, var in enumerate(variables, 1):
        plt.subplot(3, 3, i)
        plt.hist(dataframe[var], bins=30, color='skyblue', edgecolor='black')
        plt.title(f'Histogram of {var}')
        plt.xlabel(var)
        plt.ylabel('Frequency')
        plt.grid(True)

    # Adjust layout to prevent overlapping
    plt.tight_layout()
    plt.show()

# Example usage
# plot_histograms(dataframe1, ['GHI', 'DNI', 'DHI', 'WS', 'Tamb', 'TModA', 'TModB'])
