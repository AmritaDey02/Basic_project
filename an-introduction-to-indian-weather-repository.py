#!/usr/bin/env python
# coding: utf-8

# <center> <h1> Exploring Real-Time Weather Data for Indian Cities </h1>
#     <h3>Insights into India's Weather Trends</h3><br>
# 
# <center>This notebook offers an in-depth exploration of a comprehensive real-time weather dataset that provides valuable insights into the current weather conditions of major cities in India. Unlike traditional forecast data, this dataset unveils the present state of weather phenomena, allowing for a detailed analysis of temperature variations, wind patterns, precipitation levels, air quality, and more. Whether you're a meteorology enthusiast, a data scientist, or someone curious about India's diverse climate, this curated dataset opens doors to a wealth of information.<br>Throughout this notebook, we'll utilize the powerful Plotly library to visualize the dataset's features in an interactive and informative manner. From temperature distributions to wind patterns, air quality comparisons, and celestial events, we'll leverage Plotly's capabilities to bring the weather data to life.<br>Let's dive into the world of real-time weather data analysis and uncover intriguing insights together.
#     
# <br><br>
#  <a href="https://www.kaggle.com/datasets/nelgiriyewithana/indian-weather-repository-daily-snapshot">Dataset</a>
# 
# 
# 
# 

# In[ ]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import warnings

warnings.filterwarnings("ignore")

weather_data = pd.read_csv("/kaggle/input/indian-weather-repository-daily-snapshot/IndianWeatherRepository.csv")


# In[ ]:


weather_data


# # Location-wise Temperature Heatmap

# In[ ]:


fig10 = px.density_mapbox(weather_data, lat="latitude", lon="longitude", z="temperature_celsius", radius=11,
                         title="Location-wise Temperature Heatmap")
fig10.update_layout(mapbox_style="open-street-map")
fig10.show()


# # Temperature Distribution

# In[ ]:


fig1 = px.histogram(weather_data, x="temperature_celsius", nbins=20, title="Temperature Distribution")
fig1.show()


# #  Wind Speed vs Wind Direction

# In[ ]:


fig2 = px.scatter_polar(weather_data, r="wind_mph", theta="wind_direction", title="Wind Speed vs Wind Direction")
fig2.show()


# #  Humidity vs Cloud Cover

# In[ ]:


fig4 = px.scatter(weather_data, x="humidity", y="cloud", title="Humidity vs Cloud Cover")
fig4.show()


# # Air Quality Index Comparison

# In[ ]:


fig5 = px.bar(weather_data, x="location_name", y="air_quality_us-epa-index", 
              title="Air Quality Index Comparison",
              color="air_quality_us-epa-index", 
              color_continuous_scale="Viridis" 
             )
fig5.show()


# # Temperature vs Feels-like Temperature

# In[ ]:


fig8 = px.scatter(weather_data, x="temperature_celsius", y="feels_like_celsius", title="Temperature vs Feels-like Temperature")
fig8.show()


# # Sunrise vs Sunset

# In[ ]:


fig9 = px.scatter(weather_data, x="sunrise", y="sunset", title="Sunrise vs Sunset")
fig9.show()


# In[ ]:


corr_matrix = weather_data.corr()
fig2 = go.Figure(data=go.Heatmap(
    z=corr_matrix.values,
    x=corr_matrix.index,
    y=corr_matrix.columns,
    colorscale="Viridis"
))
fig2.update_layout(
    title="Correlation Heatmap",
    xaxis_title="Features",
    yaxis_title="Features"
)
fig2.show()

