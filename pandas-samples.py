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


# %% [markdown]
# ### Stock prices ###

# %%
# contains share prices of Apple's stock over a period of two years
df_stock = pd.read_csv("./data-files/pandas/apple_share_price.csv")
df_stock.head(3)


# %%
df_stock.info()


# %%
# reformat data for better read
df_stock = pd.read_csv("./data-files/pandas/apple_share_price.csv",parse_dates={'Date1':[0]}, index_col="Date1")
df_stock.sample(3)


# %%
# retrieves the share prices between two dates now easily, like for: Jan 01, 2017 to Jan 15, 2017.

#df_stock.loc['2017-01-15':'2017-01-01'] # OR
df_stock['2017-01-01':'2017-01-15':-1]


# %%
# mean closing price during the above period
df_stock['2017-01-01':'2017-01-15':-1]['Close'].mean()

# %% [markdown]
# ### Day or Night ###
# 
# There are 10 pictures for sample. The first five are of during day time and the rest during night time. Each image is of size 100x100.
# 
# The file day_night_pics.csv has 17 columns. The first ten columns encode the ten images mentioned above. For each pixel, there are three values: (R,G,B). So an image is described by 3x100x100 values. The first three rows contain the R,G,B values of the top-left most pixel. The next three rows contain the RGB values of the next pixel and so on. Hence, there are 30000 rows.
# 
# Columns 10-16 has data for seven more images - not known. Let's find what they could be?

# %%
df_pics = pd.read_csv("./data-files/pandas/day_night_pics.csv")
df_pics.sample(3)


# %%
df_pics.shape


# %%
# Daytime pictures being brighter than night-time pictures will have higher pixel values .
# Looking at the mean pixel intensity, we can guess that pics 10, 13 and 14 were taken during day time.
df_pics.mean()


# %%
# lets validate other way - seems IMAGE 13 is difficult here! 
def meanIntensity(x):
    x = str(x)
    # mean of RGB of each image 
    return np.mean(list(zip(df_pics[''+x+''][::3].values, df_pics[''+x+''][1::3].values, df_pics[''+x+''][2::3].values)))


image_result = [meanIntensity(i) for i in range(15)]
min_imgDay = np.min(image_result[0:5]) # OR use #max_imgNight = np.max(image_result[5:10])
for j in range(10,15):
    if image_result[j] > min_imgDay:
        print('image['+str(j)+']:DAY')
    else:
        print('image['+str(j)+']:NIGHT')
        
# Based on sample data, using worst day pic (mean of the RGB of pic) as reference to find the rest of the pics
# closer to 0 is dark
# closer to 255 is bright

# %% [markdown]
# ### Student Marks ### 

# %%
df_sm = pd.read_csv('./data-files/pandas/studentmarks2.csv', sep=",", header=None)
df_sm.columns = ['Name', 'Marks1', 'Marks2']
df_sm.sample(3)


# %%
# a third column called "Average" which contains the average of the Marks1 and Marks2
df_sm['Average'] = df_sm[['Marks1','Marks2']].mean(axis=1)  
# OR df_sm['Average'] = (df_sm['Marks1']+df_sm['Marks2'])/2
df_sm.sample(3)


# %%
# Rank the students according to their average marks
df_sm["Rank"] = df_sm["Average"].rank(ascending=False) 
df_sm.sort_values("Average", ascending=False, inplace = True) 
df_sm


# %%
# students whose Marks1 is above 30 and Marks2 is below 25
criteria1 = df_sm['Marks1'] > 30
criteria2 = df_sm['Marks2'] < 25
df_sm[criteria1 & criteria2]


# %%
# Capitalize the names of the students
def cap(c):
    return c.capitalize()

df_sm['Name'] = df_sm['Name'].apply(cap)
df_sm


# %%
# a new column called 'Sex' and set it to 'F' if the student's name ends with the letter 'a' and 'M' otherwise
def gender(c):
    return 'F' if (c[-1:]=='a') else 'M'

df_sm['Sex'] = df_sm['Name'].apply(gender)
df_sm

# %% [markdown]
# ### Balance Calculator ###
# 
# The file transactions.csv contains records of transactions between a group of seven people. A row has three fields: From, To and Amount. An entry "Sandeep, Jai, 20" means that Sandeep gave Rs.20 to Jai. 
# 
# 

# %%
# Assumption: everybody has Rs. 0 to begin with
# Assumption: its possible for a person to have negative balance

# Lets find out the net balances of all seven individuals after the transactions
df_bc = pd.read_csv('./data-files/pandas/transactions.csv')
df_bc.sample(3)


# %%
# it would be easier if we break the columns into values
dfb = pd.melt(df_bc, id_vars=['Amount'], var_name='Transaction', value_name='Person')
dfb.head(3)


# %%
#to setup amount as per transaction. If given, reduce amount so negative. If got, add amount so plus
def absAmount(x, y):
    return -1*y if x=='From' else y

dfb['Amount'] = dfb.apply(lambda row: absAmount(row['Transaction'], row['Amount']), axis=1)
dfb.head(3)


# %%
#Now lets just group them up by person and get the sum that would give us what we seek
df_finalb = dfb.groupby(['Person']).sum()
df_finalb.T


