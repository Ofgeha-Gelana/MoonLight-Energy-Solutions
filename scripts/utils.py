import matplotlib.pyplot as plt

def plot_time_series(dataframe):
    """
    Plots line graphs and area plots for GHI, DNI, DHI, and Tamb over time.

    Parameters:
    dataframe (pd.DataFrame): DataFrame containing time series data with columns 'GHI', 'DNI', 'DHI', 'Tamb'.
    """
    # Plotting line graphs
    plt.figure(figsize=(14, 10))

    # Plot GHI, DNI, DHI, and Tamb
    plt.subplot(2, 2, 1)
    plt.plot(dataframe.index, dataframe['GHI'], label='GHI', color='orange')
    plt.title('Global Horizontal Irradiance (GHI)')
    plt.xlabel('Time')
    plt.ylabel('GHI (W/m²)')
    plt.grid(True)

    plt.subplot(2, 2, 2)
    plt.plot(dataframe.index, dataframe['DNI'], label='DNI', color='blue')
    plt.title('Direct Normal Irradiance (DNI)')
    plt.xlabel('Time')
    plt.ylabel('DNI (W/m²)')
    plt.grid(True)

    plt.subplot(2, 2, 3)
    plt.plot(dataframe.index, dataframe['DHI'], label='DHI', color='green')
    plt.title('Diffuse Horizontal Irradiance (DHI)')
    plt.xlabel('Time')
    plt.ylabel('DHI (W/m²)')
    plt.grid(True)

    plt.subplot(2, 2, 4)
    plt.plot(dataframe.index, dataframe['Tamb'], label='Tamb', color='red')
    plt.title('Ambient Temperature (Tamb)')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

    # Plotting area plots
    plt.figure(figsize=(14, 10))

    plt.subplot(2, 2, 1)
    plt.fill_between(dataframe.index, dataframe['GHI'], color='orange', alpha=0.5)
    plt.title('Global Horizontal Irradiance (GHI)')
    plt.xlabel('Time')
    plt.ylabel('GHI (W/m²)')
    plt.grid(True)

    plt.subplot(2, 2, 2)
    plt.fill_between(dataframe.index, dataframe['DNI'], color='blue', alpha=0.5)
    plt.title('Direct Normal Irradiance (DNI)')
    plt.xlabel('Time')
    plt.ylabel('DNI (W/m²)')
    plt.grid(True)

    plt.subplot(2, 2, 3)
    plt.fill_between(dataframe.index, dataframe['DHI'], color='green', alpha=0.5)
    plt.title('Diffuse Horizontal Irradiance (DHI)')
    plt.xlabel('Time')
    plt.ylabel('DHI (W/m²)')
    plt.grid(True)

    plt.subplot(2, 2, 4)
    plt.fill_between(dataframe.index, dataframe['Tamb'], color='red', alpha=0.5)
    plt.title('Ambient Temperature (Tamb)')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

