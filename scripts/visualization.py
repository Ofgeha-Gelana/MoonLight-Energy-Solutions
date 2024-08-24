import matplotlib.pyplot as plt
import seaborn as sns

def plot_time_series(df):
    """
    Plots time series for GHI, DNI, DHI, and Tamb.
    """
    plt.figure(figsize=(14, 10))
    
    plt.subplot(2, 2, 1)
    plt.plot(df.index, df['GHI'], label='GHI', color='orange')
    plt.title('Global Horizontal Irradiance (GHI)')
    plt.xlabel('Time')
    plt.ylabel('GHI (W/m²)')
    plt.grid(True)

    plt.subplot(2, 2, 2)
    plt.plot(df.index, df['DNI'], label='DNI', color='blue')
    plt.title('Direct Normal Irradiance (DNI)')
    plt.xlabel('Time')
    plt.ylabel('DNI (W/m²)')
    plt.grid(True)

    plt.subplot(2, 2, 3)
    plt.plot(df.index, df['DHI'], label='DHI', color='green')
    plt.title('Diffuse Horizontal Irradiance (DHI)')
    plt.xlabel('Time')
    plt.ylabel('DHI (W/m²)')
    plt.grid(True)

    plt.subplot(2, 2, 4)
    plt.plot(df.index, df['Tamb'], label='Tamb', color='red')
    plt.title('Ambient Temperature (Tamb)')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def plot_correlation_heatmap(df):
    """
    Plots a heatmap of correlations between selected columns.
    """
    correlation_matrix = df[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.show()

def plot_scatter_matrix(df):
    """
    Plots a scatter matrix for solar irradiance and temperature measures.
    """
    sns.pairplot(df[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']])
    plt.suptitle('Scatter Matrix')
    plt.show()

def plot_wind_polar(df):
    """
    Plots wind speed and direction on a polar plot.
    """
    plt.figure(figsize=(10, 8))
    ax = plt.subplot(111, projection='polar')
    wind_direction = df['WD'].values
    wind_speed = df['WS'].values
    ax.scatter(wind_direction, wind_speed, c=wind_speed, cmap='hsv', alpha=0.75)
    plt.title('Wind Speed and Direction')
    plt.show()

def plot_temperature_vs_rh(df):
    """
    Plots temperature versus relative humidity.
    """
    plt.figure(figsize=(10, 8))
    plt.scatter(df['RH'], df['Tamb'], alpha=0.5)
    plt.title('Temperature vs. Relative Humidity')
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)
    plt.show()

def plot_histograms(df):
    """
    Plots histograms for selected columns.
    """
    plt.figure(figsize=(14, 10))

    plt.subplot(2, 2, 1)
    plt.hist(df['GHI'], bins=30, color='orange', edgecolor='black')
    plt.title('Histogram of GHI')

    plt.subplot(2, 2, 2)
    plt.hist(df['DNI'], bins=30, color='blue', edgecolor='black')
    plt.title('Histogram of DNI')

    plt.subplot(2, 2, 3)
    plt.hist(df['DHI'], bins=30, color='green', edgecolor='black')
    plt.title('Histogram of DHI')

    plt.subplot(2, 2, 4)
    plt.hist(df['WS'], bins=30, color='red', edgecolor='black')
    plt.title('Histogram of Wind Speed')

    plt.tight_layout()
    plt.show()

def plot_bubble_chart(df):
    """
    Plots a bubble chart with GHI vs. Tamb vs. WS, with bubble size representing RH.
    """
    plt.figure(figsize=(12, 8))
    plt.scatter(df['GHI'], df['Tamb'], s=df['RH'] * 10, c=df['WS'], cmap='viridis', alpha=0.6, edgecolors='w')
    plt.colorbar(label='Wind Speed (WS)')
    plt.title('GHI vs. Tamb vs. WS with Bubble Size for RH')
    plt.xlabel('GHI (W/m²)')
    plt.ylabel('Temperature (°C)')
    plt.show()
