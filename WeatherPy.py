
# coding: utf-8

# In[5]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
import json
from citipy import citipy

# Import API key
import api_keys1

# Incorporated citipy to determine city based on latitude and longitude
from citipy import citipy

# Output File (CSV)
output_data_file = "output_data/cities.csv"

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)


# ## Generate Cities List

# ## Perform API Calls

# In[96]:


# List for holding lat_lngs and cities
lat_lngs = []
cities = []
citycount = 0

# Create a set of random lat and lng combinations
lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    city1 = city.replace(" ","%20",3)
    # If the city is unique, then add it to a our cities list
    if citycount <=500:
     if city1 not in cities:
        cities.append(city1)
        citycount +=1
    else:
        break

# Print the city count to confirm sufficient count
len(cities)


# In[103]:


# OpenWeatherMap API Key
api_key = api_keys1.key

c_list=[];
lat = [];
temp = [];
city_list=[];

for city in cities:

# Starting URL for Weather Map API Call
 url = "http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=" + api_key +"&q="+city
 print("City:" +city,"URL:"+url)
 try:
        
    c_list = requests.get(url).json()
    lat = c_list["coord"]["lat"]
    temp = c_list["main"]["temp"]
    hum = c_list["main"]["humidity"]
    clouds = c_list["clouds"]["all"]
    wind = c_list["wind"]["speed"]
    

 except:
        pass
 city_list.append({"City":city,"Latitude":lat,"Temperature":temp,"Humidity":hum,"Cloudiness":clouds,"Wind Speed":wind})


# In[105]:



city_df = pd.DataFrame(city_list)
print(len(city_df))

city_df.head()


# In[107]:


plt.scatter(city_df["Latitude"], city_df["Temperature"])

# Incorporate the other graph properties
plt.title("Temperature in World Cities")
plt.ylabel("Temperature (Celsius)")
plt.xlabel("Latitude")
plt.grid(True)

# Save the figure
plt.savefig("TemperatureInWorldCities.png")

# Show plot
plt.show()


# In[109]:


plt.scatter(city_df["Latitude"], city_df["Humidity"])

# Incorporate the other graph properties
plt.title("Humidity in World Cities")
plt.ylabel("Humidity")
plt.xlabel("Latitude")
plt.grid(True)

# Save the figure
plt.savefig("HumidityInWorldCities.png")

# Show plot
plt.show()


# In[110]:


plt.scatter(city_df["Latitude"], city_df["Cloudiness"])

# Incorporate the other graph properties
plt.title("Cloudiness in World Cities")
plt.ylabel("Cloudiness")
plt.xlabel("Latitude")
plt.grid(True)

# Save the figure
plt.savefig("CloudinessInWorldCities.png")

# Show plot
plt.show()


# In[111]:


plt.scatter(city_df["Latitude"], city_df["Wind Speed"])

# Incorporate the other graph properties
plt.title("Wind Speed in World Cities")
plt.ylabel("Wind Speed")
plt.xlabel("Latitude")
plt.grid(True)

# Save the figure
plt.savefig("Wind SpeedInWorldCities.png")

# Show plot
plt.show()

