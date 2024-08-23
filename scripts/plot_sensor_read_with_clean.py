import matplotlib.pyplot as plt

def plot_sensor_readings_with_cleaning(dataframe, mod_columns=['ModA', 'ModB'], cleaning_column='Cleaning'):
    """
    Plots sensor readings over time and highlights cleaning events.

    Parameters:
    - dataframe (pd.DataFrame): The input DataFrame containing sensor data and cleaning events.
    - mod_columns (list): List of columns representing sensor readings to plot (e.g., ['ModA', 'ModB']).
    - cleaning_column (str): The column name indicating cleaning events.
    """
    plt.figure(figsize=(14, 7))

    # Plot sensor readings over time
    for mod_column in mod_columns:
        plt.plot(dataframe.index, dataframe[mod_column], label=mod_column)

    # Highlight the cleaning events
    cleaning_events = dataframe[dataframe[cleaning_column] == True].index
    for event in cleaning_events:
        plt.axvline(event, color='red', linestyle='--', alpha=0.5)

    plt.title('Sensor Readings Over Time with Cleaning Events')
    plt.xlabel('Time')
    plt.ylabel('Sensor Readings')
    plt.legend()
    plt.grid(True)
    plt.show()

