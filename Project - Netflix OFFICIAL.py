#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv("ViewingActivity.csv")
df.head()


# In[2]:


df.shape


# In[3]:


df.columns


# In[4]:


# Remove unnecessary columns
newdfaus = df.filter(items = ["Profile Name","Start Time", "Duration", "Title"])
newdfaus


# In[5]:


# AUS - Convert Start Time column elements to datetime type
newdfaus["Start Time"] = pd.to_datetime(newdfaus["Start Time"], utc = True)
newdfaus.dtypes


# In[6]:


# AUS - Set the Start Time column as the index to convert to Australia/Melbourne timezone
newdfaus = newdfaus.set_index("Start Time")
newdfaus.index = newdfaus.index.tz_convert("Australia/Melbourne")
newdfaus


# In[7]:


# AUS - Reset the index column to make the Start Time a column again
newdfaus = newdfaus.reset_index()
newdfaus


# In[8]:


# AUS - Double check the datatype
newdfaus.dtypes


# In[9]:


# AUS - Convert Duration to timedelta type and double check the datatype
newdfaus["Duration"] = pd.to_timedelta(newdfaus["Duration"])
newdfaus.dtypes


# In[10]:


# VN - Create a new variable newdfvn using the newdfaus to convert the Start Time column to Asia/Ho_Chi_Minh timezone
newdfvn = newdfaus.set_index("Start Time")
newdfvn.index = newdfvn.index.tz_convert("Asia/Ho_Chi_Minh")
newdfvn


# In[11]:


# VN - Reset the index column to make the Start Time a column again
newdfvn = newdfvn.reset_index()
newdfvn


# In[12]:


# VN - Double check the datatype
newdfvn.dtypes


# In[13]:


# AUS - filter profile name as my user name and Archer as the title
tatiendat21aus = newdfaus[newdfaus["Profile Name"].str.contains("tatiendat21") & newdfaus["Title"].str.contains("Archer")]
tatiendat21aus


# In[14]:


# VN - filter profile name as my user name and Archer as the title
tatiendat21vn = newdfvn[newdfvn["Profile Name"].str.contains("tatiendat21") & newdfvn["Title"].str.contains("Archer")]
tatiendat21vn


# In[15]:


# AUS - Filter duration to avoid the data from watching trailet or autoplay
tatiendat21archeraus = tatiendat21aus[tatiendat21aus["Duration"] > "0 days 00:05:00"]
tatiendat21archeraus.shape


# In[16]:


# VN - Filter duration to avoid the data from watching trailet or autoplay
tatiendat21archervn = tatiendat21vn[tatiendat21vn["Duration"] > "0 days 00:05:00"]
tatiendat21archervn.shape


# In[17]:


# AUS & VN - Sum the duration to see how much time did I spend to watch Archer
tatiendat21archeraus["Duration"].sum()


# In[18]:


# AUS - Split weekday, hour and date from Start Time column
tatiendat21archeraus["weekday"] = tatiendat21archeraus["Start Time"].dt.weekday
tatiendat21archeraus["hour"] = tatiendat21archeraus["Start Time"].dt.hour
tatiendat21archeraus["date"] = tatiendat21archeraus["Start Time"].dt.date
tatiendat21archeraus


# In[19]:


# VN - Split weekday, hour and date from Start Time column
tatiendat21archervn["weekday"] = tatiendat21archervn["Start Time"].dt.weekday
tatiendat21archervn["hour"] = tatiendat21archervn["Start Time"].dt.hour
tatiendat21archervn["date"] = tatiendat21archervn["Start Time"].dt.date
tatiendat21archervn


# In[20]:


# VN - Filter the data when I was living in Vietnam
startdatevn = pd.to_datetime("2022-09-16").date()
enddatevn = pd.to_datetime("2023-05-12").date()
tatiendat21archervn_2 = tatiendat21archervn.loc[(tatiendat21archervn["date"] >= startdatevn) & 
                                                (tatiendat21archervn["date"] <= enddatevn)]
tatiendat21archervn_2


# In[21]:


# AUS - Filter the data when I was living in Australia
enddateaus = pd.to_datetime("2023-07-24").date()
tatiendat21archeraus_2 = tatiendat21archeraus.loc[(tatiendat21archeraus["date"] > enddatevn) & 
                                                  (tatiendat21archeraus["date"] <= enddateaus)]
tatiendat21archeraus_2


# In[22]:


import matplotlib.pyplot as plt


# In[23]:


# VN - Count and sort the weekday values
tatiendat21archervn_2_byday = tatiendat21archervn_2["weekday"].value_counts()
tatiendat21archervn_2_bydaysort = tatiendat21archervn_2_byday.sort_index(ascending = True)
tatiendat21archervn_2_bydaysort


# In[24]:


# VN - Plot the bar chart using the weekday values
plt.rcParams.update({'font.size': 15})
tatiendat21archervn_2_bydaysort.plot(kind = "bar", color = "green")
plt.title("Archer Series Watched By Day In Vietnam")
plt.show()


# In[25]:


# VN - Count and sort the hour values
tatiendat21archervn_2_byhour = tatiendat21archervn_2["hour"].value_counts()
tatiendat21archervn_2_byhoursort = tatiendat21archervn_2_byhour.sort_index(ascending = True)
tatiendat21archervn_2_byhoursort


# In[26]:


# VN - Plot the bar chart using the hour values with Vietnam's timezone
plt.rcParams.update({'font.size': 12})
tatiendat21archervn_2_byhoursort.plot(kind = "bar", color = "c")
plt.title("Archer Series Watched By Hour In Vietnam")
plt.show()


# In[27]:


# AUS - Count and sort the weekday values
tatiendat21archeraus_2_byday = tatiendat21archeraus_2["weekday"].value_counts()
tatiendat21archeraus_2_bydaysort = tatiendat21archeraus_2_byday.sort_index(ascending = True)
tatiendat21archeraus_2_bydaysort


# In[28]:


# AUS - Plot the bar chart using the weekday values
plt.rcParams.update({'font.size': 15})
tatiendat21archeraus_2_bydaysort.plot(kind = "bar", color = "yellow")
plt.title("Archer Series Watched By Day In Australia")
plt.show()


# In[29]:


# AUS - Count and sort the hour values
tatiendat21archeraus_2_byhour = tatiendat21archeraus_2["hour"].value_counts()
tatiendat21archeraus_2_byhoursort = tatiendat21archeraus_2_byhour.sort_index(ascending = True)
tatiendat21archeraus_2_byhoursort


# In[30]:


# AUS - Plot the bar chart using the hour values with Melbourne's timezone
plt.rcParams.update({'font.size': 12})
tatiendat21archeraus_2_byhoursort.plot(kind = "bar", color = "purple")
plt.title("Archer Series Watched By Hour In Australia")
plt.show()

