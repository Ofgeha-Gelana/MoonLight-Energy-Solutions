import seaborn as sns
import matplotlib.pyplot as plt

def plot_rh_jointplots(dataframe):
    """
    This function creates joint plots to visualize the relationship between Relative Humidity (RH)
    and other variables such as Ambient Temperature (Tamb), Global Horizontal Irradiance (GHI),
    Direct Normal Irradiance (DNI), and Diffuse Horizontal Irradiance (DHI).
    
    
    Returns:
    None
    """
    # Joint plot between RH and Ambient Temperature (Tamb)
    sns.jointplot(x='RH', y='Tamb', data=dataframe, kind='scatter', color='red', height=8)
    plt.suptitle('Joint Plot: Relative Humidity (RH) vs. Ambient Temperature (Tamb)', y=1.02)
    plt.show()

    # Joint plot between RH and Global Horizontal Irradiance (GHI)
    sns.jointplot(x='RH', y='GHI', data=dataframe, kind='scatter', color='orange', height=8)
    plt.suptitle('Joint Plot: Relative Humidity (RH) vs. Global Horizontal Irradiance (GHI)', y=1.02)
    plt.show()

    # Joint plot between RH and Direct Normal Irradiance (DNI)
    sns.jointplot(x='RH', y='DNI', data=dataframe, kind='scatter', color='blue', height=8)
    plt.suptitle('Joint Plot: Relative Humidity (RH) vs. Direct Normal Irradiance (DNI)', y=1.02)
    plt.show()

    # Joint plot between RH and Diffuse Horizontal Irradiance (DHI)
    sns.jointplot(x='RH', y='DHI', data=dataframe, kind='scatter', color='green', height=8)
    plt.suptitle('Joint Plot: Relative Humidity (RH) vs. Diffuse Horizontal Irradiance (DHI)', y=1.02)
    plt.show()

