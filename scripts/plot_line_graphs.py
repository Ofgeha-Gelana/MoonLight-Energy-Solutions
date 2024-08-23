import matplotlib.pyplot as plt

def plot_irradiance_and_temperature(dataframe):
    """
    This function plots line graphs for GHI, DNI, DHI, and Tamb from the given DataFrame.
    
    Parameters:
    dataframe (pd.DataFrame): The DataFrame containing the data to plot.
    
    Returns:
    None
    """
    plt.figure(figsize=(14, 10))

    # Plot GHI
    plt.subplot(2, 2, 1)
    plt.plot(dataframe.index, dataframe['GHI'], label='GHI', color='orange')
    plt.title('Global Horizontal Irradiance (GHI)')
    plt.xlabel('Time')
    plt.ylabel('GHI (W/m²)')
    plt.grid(True)

    # Plot DNI
    plt.subplot(2, 2, 2)
    plt.plot(dataframe.index, dataframe['DNI'], label='DNI', color='blue')
    plt.title('Direct Normal Irradiance (DNI)')
    plt.xlabel('Time')
    plt.ylabel('DNI (W/m²)')
    plt.grid(True)

    # Plot DHI
    plt.subplot(2, 2, 3)
    plt.plot(dataframe.index, dataframe['DHI'], label='DHI', color='green')
    plt.title('Diffuse Horizontal Irradiance (DHI)')
    plt.xlabel('Time')
    plt.ylabel('DHI (W/m²)')
    plt.grid(True)

    # Plot Tamb
    plt.subplot(2, 2, 4)
    plt.plot(dataframe.index, dataframe['Tamb'], label='Tamb', color='red')
    plt.title('Ambient Temperature (Tamb)')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)

    plt.tight_layout()
    plt.show()
