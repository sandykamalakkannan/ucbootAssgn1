
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# File to Load (Remember to change these)
city_data_to_load = "data/city_data.csv"
ride_data_to_load = "data/ride_data.csv"

# Read the City and Ride Data
city_df = pd.read_csv("data/city_data.csv")
ride_df = pd.read_csv("data/ride_data.csv")
# Combine the data into a single dataset
combined_city_ride_df = pd.merge(ride_df,city_df, how='left', on='city')
combined_city_ride_df.head()
# Display the data table for preview


# In[3]:


type_df= combined_city_ride_df.groupby('type')
type_df.count()


# In[9]:


driver_count = combined_city_ride_df.groupby(["type","city"])
d_total = driver_count['driver_count'].sum()
d_total


# In[5]:


y = combined_city_ride_df.groupby(["type","city"]).mean()
x = combined_city_ride_df.groupby(["type","city"]).count()

x_rural = x.loc["Rural","fare"]
y_rural = y.loc["Rural","ride_id"]



x_urban = x.loc["Urban","fare"]
y_urban = y.loc["Urban","ride_id"]


x_suburban = x.loc["Suburban","fare"]
y_suburban = y.loc["Suburban","ride_id"]


# In[22]:


plt.scatter(x_rural,y_rural,s = d_total,marker="o",facecolors="blue",edgecolors="black",alpha=0.75,label='Rural')
plt.scatter(x_urban,y_urban,s = d_total,marker="o",facecolors="red",edgecolors="black",alpha=0.75,label='Urban')
plt.scatter(x_suburban ,y_suburban,s = d_total,marker="o",facecolors="orange",edgecolors="black",alpha=0.75,label='SubUrban')

plt.legend(title='City Type')
plt.xlabel("Total Number of rides (Per City)")
plt.ylabel("Average Fare ($)")
plt.title("Pyber Ride sharing Data (2016)")
plt.text(43,35,'Note\nCircle size correlates with driver count per city')
plt.grid()
plt.savefig("../Images/Pyber_Ridesharing_Data.png")   
plt.show()


# ## Bubble Plot of Ride Sharing Data

# In[2]:


# Obtain the x and y coordinates for each of the three city types


# Build the scatter plots for each city types

# Incorporate the other graph properties

# Create a legend

# Incorporate a text label regarding circle size

# Save Figure


# In[3]:


# Show plot
plt.show()


# ## Total Fares by City Type

# In[24]:


# Calculate Type Percents
type_df1=combined_city_ride_df[['type','fare']]
type_df1=type_df1.groupby('type').sum()
type_df1['percentage']=(type_df1['fare']/type_df1['fare'].sum())*100
#plt.title='% of total fares by city type'
# Build Pie Chart
plt.pie(type_df1['percentage'],explode=(0,0,0.1),labels=['Rural','Suburban','Urban'],autopct="%1.1f%%", shadow=True,colors=['blue','green','yellow'],startangle=140);
plt.title("% of total fares by city type");
# Save the plot and display it
plt.savefig("../Images/fare_percent.png")


# In[25]:


# Show Figure
plt.show()


# ## Total Rides by City Type

# In[26]:


# Calculate Ride Percents
type_df2=combined_city_ride_df[['ride_id','type']]
type_df2=type_df2.groupby('type').count()
type_df2['percentage']=(type_df2['ride_id']/type_df2['ride_id'].sum())*100
#plt.title='% of total rides by city type'
# Build Pie Chart
plt.pie(type_df2['percentage'],explode=(0,0,0.1),labels=['Rural','Suburban','Urban'],autopct="%1.1f%%", shadow=True,colors=['blue','red','orange'],startangle=140);
plt.title("% of total rides by city type");
# Save the plot and display it
plt.savefig("../Images/ride_percent.png")


# In[27]:


# Show Figure
plt.show()


# ## Total Drivers by City Type

# In[29]:


d_count=city_df[['driver_count','type']]
d_count=city_df.groupby('type').sum()
d_count['percentage']=(d_count['driver_count']/d_count['driver_count'].sum())*100
#plt.title='% of total rides by city type'
# Build Pie Chart
plt.pie(d_count['percentage'],explode=(0,0,0.1),labels=['Rural','Suburban','Urban'],autopct="%1.1f%%", shadow=True,colors=['purple','pink','yellow'],startangle=140);
plt.title("% of total drivers by city type");
# Save the plot and display it
plt.savefig("../Images/driver_percent.png")
plt.show()


# In[30]:


# Show Figure
plt.show()

