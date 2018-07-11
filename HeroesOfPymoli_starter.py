
# coding: utf-8

# ### Heroes Of Pymoli Data Analysis
# * Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).
# 
# * Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
# -----

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# Raw data file
file_to_load = "Resources/purchase_data.csv"

# Read purchasing file and store into pandas data frame
purchase_data = pd.read_csv(file_to_load)


# ## Player Count

# * Display the total number of players
# 

# In[2]:


total_player = pd.DataFrame({'total players':[len(purchase_data.SN.unique())]})
total_player


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[3]:


items = purchase_data['Purchase ID'].count()
items


# In[4]:


price = purchase_data['Price'].sum()
price


# In[5]:


unique_ID = len(purchase_data['Item ID'].unique())
unique_ID


# In[6]:


avg_price = purchase_data['Price'].mean()
avg_price


# In[7]:


p_analysis = pd.DataFrame({"Number of Unique Items":[unique_ID],"Average Price":[avg_price],"Number of Purchases":[items],"Total Revenue":[price]})
p_analysis
  


# ## Gender Demographics

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[18]:


Gen_D=pd.DataFrame({"Total Count":purchase_data.groupby('Gender').size()})
Gen_D["Percentage of Players"]=(Gen_D["Total Count"]/len(purchase_data.SN.unique()))*100

Gen_D=Gen_D[["Percentage of Players","Total Count"]]
Gen_D.sort_values("Total Count",ascending=False)


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, etc. by gender
# 
# 
# * For normalized purchasing, divide total purchase value by purchase count, by gender
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[5]:


gen = purchase_data.groupby("Gender")
pu_mean = gen['Price'].mean()
pu_count = gen['Purchase ID'].count()
pu_sum = gen['Price'].sum()
pu_norm = pu_sum/pu_count
pu_analysis = pd.DataFrame({"Purchase Count":pu_count,"Average Purchase Price":pu_mean,"Total Purchase Vale":pu_sum,"Normalized Total":pu_norm})
pu_analysis


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[13]:


age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
pu_data = purchase_data
pu_data["Age_d"] = pd.cut(pu_data["Age"], age_bins, labels=group_names)
pu_data = pu_data.groupby("Age_d")
tot_count= pu_data["SN"].count()
perc = tot_count /len(pu_data["SN"])
pu_analysis8 = pd.DataFrame({"Total Count":tot_count,"Percentage":perc})
pu_analysis8


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, etc. in the table below
# 
# 
# * Calculate Normalized Purchasing
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[17]:


# Establish bins for ages
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
pu_data = purchase_data
pu_data["Age_d"] = pd.cut(pu_data["Age"], age_bins, labels=group_names)
pu_data = pu_data.groupby("Age_d")

#tot_count= pu_data["SN"].count()
#tot_count
pu_mean1 = pu_data['Price'].mean()
pu_count1 = pu_data['Purchase ID'].count()
pu_sum1 = pu_data['Price'].sum()
pu_norm1 = pu_sum1/pu_count1
pu_analysis1 = pd.DataFrame({"Purchase Count":pu_count1,"Average Purchase Price":pu_mean1,"Total Purchase Vale":pu_sum1,"Normalized Total":pu_norm1})
pu_analysis1


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[16]:


pu_data2 = purchase_data.groupby("SN")
pu_mean2 = pu_data2['Price'].mean()
pu_count2 = pu_data2['Purchase ID'].count()
pu_sum2 = pu_data2['Price'].sum()
pu_norm2 = pu_sum2/pu_count2
pu_analysis2 = pd.DataFrame({"Purchase Count":pu_count2,"Average Purchase Price":pu_mean2,"Total Purchase Vale":pu_sum2,"Normalized Total":pu_norm2})
pu_analysis2= pu_analysis2.sort_values(["Total Purchase Vale"], ascending=False)
pu_analysis2.head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[15]:


pu_data3 = purchase_data[["Item ID", "Item Name","Price","Purchase ID"]]
pu_data3 = pu_data3.groupby(["Item ID","Item Name"])
pu_mean3 = pu_data3['Price'].mean()
pu_count3 = pu_data3['Purchase ID'].count()
pu_sum3 = pu_data3['Price'].sum()

pu_analysis3 = pd.DataFrame({"Purchase Count":pu_count3,"Average Purchase Price":pu_mean3,"Total Purchase Vale":pu_sum3})
pu_analysis3= pu_analysis3.sort_values(["Purchase Count"], ascending=False)
pu_analysis3.head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[14]:


pu_data3 = purchase_data[["Item ID", "Item Name","Price","Purchase ID"]]
pu_data3 = pu_data3.groupby(["Item ID","Item Name"])
pu_mean3 = pu_data3['Price'].mean()
pu_count3 = pu_data3['Purchase ID'].count()
pu_sum3 = pu_data3['Price'].sum()

pu_analysis3 = pd.DataFrame({"Purchase Count":pu_count3,"Average Purchase Price":pu_mean3,"Total Purchase Vale":pu_sum3})
pu_analysis3= pu_analysis3.sort_values(["Total Purchase Vale"], ascending=False)
pu_analysis3.head()

