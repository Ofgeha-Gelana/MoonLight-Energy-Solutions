import numpy as np
import matplotlib.pyplot as plt

def plot_wind_polar(dataframe, wind_dir_col='WD', wind_speed_col='WS'):
    """
    This function creates a polar plot for wind speed distribution based on wind direction.
    
    Parameters:
    dataframe (pd.DataFrame): The DataFrame containing the wind direction and speed data.
    wind_dir_col (str): The name of the column containing wind direction in degrees (default is 'WD').
    wind_speed_col (str): The name of the column containing wind speed (default is 'WS').
    
    Returns:
    None
    """
    # Convert wind direction to radians
    wind_direction_rad = np.deg2rad(dataframe[wind_dir_col])
    
    # Create the polar plot
    plt.figure(figsize=(10, 8))
    ax = plt.subplot(111, polar=True)
    ax.scatter(wind_direction_rad, dataframe[wind_speed_col], c='blue', alpha=0.75, label='Wind Speed (WS)')
    
    # Configure polar plot appearance
    ax.set_theta_direction(-1)  # Wind directions go clockwise
    ax.set_theta_offset(np.pi / 2.0)  # 0 degrees at the top (North)
    ax.set_title('Polar Plot: Wind Speed and Direction', va='bottom')
    
    # Show legend and plot
    plt.legend(loc='upper right')
    plt.show()


