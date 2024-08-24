import streamlit as st
import pandas as pd
import os, sys

rpath = os.path.abspath('..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

import streamlit as st
import pandas as pd
from scripts.data_processing import fetch_data, clean_data
from scripts.visualization import (
    plot_time_series,
    plot_correlation_heatmap,
    plot_scatter_matrix,
    plot_wind_polar,
    plot_temperature_vs_rh,
    plot_histograms,
    plot_bubble_chart
)

# Set the title of the app
st.title('Data Insights Dashboard')

# Fetch and clean data
data = fetch_data('../data/benin-malanville.csv')
cleaned_data = clean_data(data)

# Sidebar for user inputs
st.sidebar.header('User Inputs')
start_date = st.sidebar.date_input('Start Date', value=pd.to_datetime('2021-08-09'))
end_date = st.sidebar.date_input('End Date', value=pd.to_datetime('2021-08-10'))

# Filter data based on user inputs
filtered_data = cleaned_data[(cleaned_data.index >= start_date) & (cleaned_data.index <= end_date)]

# Plot time series
st.header('Time Series Analysis')
st.pyplot(plot_time_series(filtered_data))

# Plot correlation heatmap
st.header('Correlation Heatmap')
st.pyplot(plot_correlation_heatmap(filtered_data))

# Plot scatter matrix
st.header('Scatter Matrix')
st.pyplot(plot_scatter_matrix(filtered_data))

# Plot wind polar
st.header('Wind Speed and Direction')
st.pyplot(plot_wind_polar(filtered_data))

# Plot temperature vs. RH
st.header('Temperature vs. Relative Humidity')
st.pyplot(plot_temperature_vs_rh(filtered_data))

# Plot histograms
st.header('Histograms')
st.pyplot(plot_histograms(filtered_data))

# Plot bubble chart
st.header('Bubble Chart')
st.pyplot(plot_bubble_chart(filtered_data))
