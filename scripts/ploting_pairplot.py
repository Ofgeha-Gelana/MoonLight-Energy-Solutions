import seaborn as sns
import matplotlib.pyplot as plt

def plot_pairplot(dataframe, columns):
    """
    This function creates a pair plot for the specified columns in the DataFrame using Seaborn.
    
    Parameters:
    dataframe (pd.DataFrame): The DataFrame containing the data.
    columns (list): List of column names to include in the pair plot.
    
    Returns:
    None
    """
    # Create the pair plot
    pair_plot = sns.pairplot(dataframe[columns], diag_kind='kde', markers='+')
    
    # Set the title for the pair plot
    plt.suptitle('Pair Plot: Solar Radiation and Temperature Measures', y=1.02)
    
    # Show the plot
    plt.show()

# Example usage
# correlation_columns = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB']
# plot_pairplot(dataframe1, correlation_columns)
