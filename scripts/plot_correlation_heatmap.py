import seaborn as sns
import matplotlib.pyplot as plt

def plot_corr_heat(dataframe, columns):
    """
    This function calculates the correlation matrix for the specified columns in the DataFrame
    and plots a heatmap to visualize the correlations.
    
    Parameters:
    dataframe (pd.DataFrame): The DataFrame containing the data.
    columns (list): List of column names for which the correlation matrix is calculated.
    
    Returns:
    None
    """
    # Select relevant columns for correlation analysis
    correlation_matrix = dataframe[columns].corr()
    
    # Plotting the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Heatmap: Solar Radiation and Temperature Measures')
    plt.show()



def test_fun():
    print("this is test function")