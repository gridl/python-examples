# Python script of panda basics
# Author: Sandeep Mewara
# Location: Learn By Insight
# Github: https://github.com/samewara/python-examples/blob/master/pandas-samples.py
# #####################################
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# ## Pandas Samples ##
# %% [markdown]
# ### Uber taxi Drivers ###
# 
# dataset about 10000 Uber rides from one day in New York city. 
# The columns give information about time and location of each pickup
# 

# %%
import pandas as pd

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# %%
uber_df = pd.read_csv('./data-files/pandas/uber-apr14.csv')
uber_df.columns


# %%
uber_df.sample(3)


# %%
uber_df.info()


# %%
# column 'Date/Time' is in object format, lets correct it
uber_df['Date/Time'] = uber_df['Date/Time'].apply(pd.to_datetime)
uber_df.info()


# %%
# for some pattern, lets get DayOfWeek, Day & only Date for each data point

def dayOfWeek(x):
    return x.weekday()+1

def dayName(x):
    return x.day_name()

uber_df['DayOfWeek'] = uber_df['Date/Time'].apply(dayOfWeek)
uber_df['DayName'] = uber_df['Date/Time'].apply(dayName)
uber_df['DateOnly'] = uber_df['Date/Time'].apply(lambda x: x.date())
uber_df.head(3)


# %%
# average no of rides/DayofWeek

uber_df_gr = uber_df.groupby(['DayOfWeek', 'DateOnly']) # to find average we need to know no of days contributing to a dayofweek
uber_df_gr.count()


# %%
# notice for DayofWeek==2, we have multiple days contributing data
# now, we can groupby dayofweek and take mean 

uber_df_gr.count().groupby('DayOfWeek').mean()


# %%
# Plotting a graph of Lat/Lon to see the spread of rides to highlevel access if rides are concentrated to a region
plt.figure(figsize=(12, 12))
plt.plot(uber_df['Lon'], uber_df['Lat'], '.',alpha=0.5)


# %%
# we can see that most of the rides happen within the city
# lets zoom it up using the xlim & ylim
plt.figure(figsize=(12, 12))
plt.plot(uber_df['Lon'], uber_df['Lat'], '.',alpha=0.5)
plt.xlim(-74.05,-73.90)
plt.ylim(40.65, 40.85)


