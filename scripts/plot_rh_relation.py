import seaborn as sns
import matplotlib.pyplot as plt

def plot_rh_relationships(dataframe):
    """
    This function creates scatter plots to visualize the relationship between
    Relative Humidity (RH) and other variables such as Ambient Temperature (Tamb),
    Global Horizontal Irradiance (GHI), Direct Normal Irradiance (DNI), and
    Diffuse Horizontal Irradiance (DHI).
    
    Parameters:
    dataframe (pd.DataFrame): The DataFrame containing the data.
    
    Returns:
    None
    """
    # Scatter plot between RH and Ambient Temperature (Tamb)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=dataframe['RH'], y=dataframe['Tamb'], color='red')
    plt.title('Scatter Plot: Relative Humidity (RH) vs. Ambient Temperature (Tamb)')
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)
    plt.show()
    
    # Scatter plot between RH and Global Horizontal Irradiance (GHI)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=dataframe['RH'], y=dataframe['GHI'], color='orange')
    plt.title('Scatter Plot: Relative Humidity (RH) vs. Global Horizontal Irradiance (GHI)')
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('GHI (W/m²)')
    plt.grid(True)
    plt.show()
    
    # Scatter plot between RH and Direct Normal Irradiance (DNI)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=dataframe['RH'], y=dataframe['DNI'], color='blue')
    plt.title('Scatter Plot: Relative Humidity (RH) vs. Direct Normal Irradiance (DNI)')
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('DNI (W/m²)')
    plt.grid(True)
    plt.show()
    
    # Scatter plot between RH and Diffuse Horizontal Irradiance (DHI)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=dataframe['RH'], y=dataframe['DHI'], color='green')
    plt.title('Scatter Plot: Relative Humidity (RH) vs. Diffuse Horizontal Irradiance (DHI)')
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('DHI (W/m²)')
    plt.grid(True)
    plt.show()

# Example usage
# plot_rh_relationships(dataframe1)
