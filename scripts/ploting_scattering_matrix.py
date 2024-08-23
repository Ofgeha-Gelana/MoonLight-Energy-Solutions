import seaborn as sns
import matplotlib.pyplot as plt

def plot_scatter_matrix(dataframe, columns, hue=None):
    """
    This function creates a scatter matrix (pair plot) for the specified columns in the DataFrame,
    with optional hue for a categorical variable.
    
    Parameters:
    dataframe (pd.DataFrame): The DataFrame containing the data.
    columns (list): List of column names to include in the scatter matrix.
    hue (str): Name of the categorical column to use for color encoding (default is None).
    
    Returns:
    None
    """
    # Create the pair plot
    pair_plot = sns.pairplot(dataframe[columns], diag_kind='kde', markers='+', hue=hue)
    
    # Set the title for the pair plot
    plt.suptitle('Scatter Matrix: Wind Conditions and Solar Irradiance', y=1.02)
    
    # Show the plot
    plt.show()

