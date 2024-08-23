import seaborn as sns
import matplotlib.pyplot as plt

def plot_rh_correlation_heatmap(dataframe):
    """
    This function calculates the correlation matrix between Relative Humidity (RH) and other variables
    (Ambient Temperature, GHI, DNI, DHI) and plots a heatmap of the correlations.
    
    Parameters:
    dataframe (pd.DataFrame): The DataFrame containing the data.
    
    Returns:
    None
    """
    # Calculate correlations between RH and temperature/solar radiation
    correlation_matrix = dataframe[['RH', 'Tamb', 'GHI', 'DNI', 'DHI']].corr()
    
    # Plotting the heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Heatmap: Relative Humidity vs. Temperature and Solar Radiation')
    plt.show()

