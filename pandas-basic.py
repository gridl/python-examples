# Python script of panda basics
# Author: Sandeep Mewara
# Location: Learn By Insight
# Github: https://github.com/samewara/python-examples/blob/master/pandas-basic.py
# #####################################
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Pandas #
# 
# - is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
# 
# - built on top of the Python programming language.
# 

# %%
# imports!
import pandas as pd 
import numpy as np 

# %% [markdown]
# ## Series ##

# %%
l1 = pd.Series([1,2,3]) #Series defined from a list
l1


# %%
# series back to numpy
l1.values


# %%
l2 = pd.Series(np.array([1,2,3,4,5,6,7,8])) #Series defined from an array
l2


# %%
type(l2)


# %%
l3 = pd.Series(np.array([1,3,5,7,'',9,11])) #Series can have mixed datatypes, though it would allow only operations on them
print('pandas l3:\n',l3)
print('mean:', l3.mean()) # empty string is a valid value - treated as if zero
print('max:', l3.max())

# Though below would throw an error and not allowed. 
#l4 = pd.Series(np.array([1,'Sandeep',4]))
#l4.mean()


# %%
l3.replace("1","2") #multiple funtions like replace available


# %%
print('#indexing allowed to access the data:',l3[0]) #indexing allowed to access the data
print('#datatype post basic indexing:', type(l3[0]))
print('#DEFAULT series index defined as:', l3.index)
print('#post defined indexing #1:', l3[0:3])
print('#post defined indexing #2:', l3[2:])
print('#post defined indexing #3:', l3[:-1])
print('#post defined indexing #4:', l3[1:-1:2])
print('#post defined indexing #5:', l3[::2])


# %%
l4 = pd.Series([1,3,5,7,9], index=['A','B','C','D','E']) # CUSTOM index defined
print('l4[''A'']:',l4['A']) # case-sensitive l4['a'] NOT allowed
print('l4[''B'']:',l4['B']) 
print('l4[''C'']:',l4['C']) 
print('l4[''B'':''D'']:',l4['B':'D']) #Range indexing on custom index allowed 

# %% [markdown]
# ## Dataframes ##
# %% [markdown]
# *** Dataframe from list of tuples ***

# %%
name = ['Sandeep','Murari','Niya','John','Swarnima']
age = [35, 25, 30, 33, 23]

people = list (zip(name,age))
print(people)
df = pd.DataFrame(data=people, columns=['Name','Age'])
df


# %%
df.rank() # compute numerical data ranks (1 through n) along axis

# %% [markdown]
# *** Data Retrieval from Data Frames ***

# %%
# rows can be retrieved via index
df.iloc[0]


# %%
# columns can be retrieved using names
df ["Name"]


# %%
print(type(df["Age"])) #each column is a Series!
print("Index access in a Series:",df["Name"][0])


# %%
# index is not unique. Thus, when accessed, if multiple values - gives all
findme = pd.Series(["LEARN","BY","INSIGTH"])
findme = findme.append(pd.Series(["INSIGHT","BY","LEARN"]), ignore_index=True)
findme = findme.append(pd.Series(["LEARNBYINSIGHT"])) #resets index by default on append
print(findme)
print("Row access of Series using index directly:\n",findme[0]) # returns both values (visible)
print("Row access of Series using iloc:\n", findme.iloc[6]) # returns actual index (assume hidden unique) 


# %%
df.info() # basic info about dataframe, generally first thing to gauge about


# %%
df2 = pd.DataFrame(data=people)
df2[0] #only allowed when columns are not defined. Thus, df[0] will throw error as Name, Age defined.


# %%
#Can define any column as index
df.set_index('Name', inplace=True)
df


# %%
# cannot do df['Sandeep'] - its not an accessible index
# range around them can be done
df['Sandeep':'Niya']


# %%
#loc access can be done (SEE: loc and not iloc => no more numerical index)
df.loc['Sandeep']


# %%
#df['Name'] => NOT allowed. No more a column but index
df['Age'] # => Allowed

# %% [markdown]
# *** Dataframe from a dictionary ***

# %%
educated_dict = { 'Country': [ 'India', 'China', 'United States', 'Malaysia' ],
                  'Educated' : [200001234, 300001234, 100001234, 20001234] }

for k,v in educated_dict.items():
    print (k,v)

df2 = pd.DataFrame(educated_dict)
df2


# %%
df2.info()


# %%
#df.head() => would give entire data back
df2.head(2)


# %%
df2.sample(2) #any 
# df2.tail()  # similar commands


# %%
df2["Country"]

# %% [markdown]
# *** Dataframe from CSV ***

# %%
# The option sep="," is used to indicate field separators
# The file name can be replaced with a URL
df3 = pd.read_csv('./data-files/pandas/population.csv',sep=",") 
df3.head()


# %%
df3.info() #get the jist of data => 14885 rows :thumbsup: 


# %%
# Random sample of 20 distinct countries from the list
uniqueCountries = df3['Country Name'].unique()
np.random.choice(uniqueCountries, 20)


# %%
# df3.iloc[0:4]
# The general for of iloc is df.iloc[ row_indexer , col_indexer].
# explicit column selection
df3.iloc[ 0:4, [1,3] ] # same as df3.iloc[ :4, range(1,3) ]

# iloc does not support label-based access. In this case we must drop use loc.
# df.iloc[ 0:1, ['Year','Value']  ] => Invalid


# %%
# Boolean Indexing => MASKING
# We select rows that satisfy those boolean conditions (one or multiple) 
# Boolean index can be made from a combination of logical operators of AND &, OR |, NOT ~.
bool1 = df3['Value']>1000000000
bool2 = df3['Year']>2000
df3[bool1 & bool2].sample(5)


# %%
# isin is a useful operator when building a boolean index
selection_condition_3 = df3['Country Name'].isin( ['China','India'] )
df3[selection_condition_3].sample(5)


# %%
# where is useful when we want to retain the shape of the original table.
# The values that dont match the selection critieria are set to NaN
df3b = df3.where(df3['Year']>2011)
df3b


# %%
print((df3.describe().mean()).Value)
print((df3.describe().std()).Value)


# %%
# countries whose GDP is more than three standard deviations from the average
con1 = df3['Value'] > (-df3.describe().mean()).Value + 3*(df3.describe().std()).Value
df3[con1]

# %% [markdown]
# *** Dataframe from Built-in dataset ***
# 
# Packages like sklearn and seaborn come with practice datasets
# 

# %%
#Pandas dataframe from iris dataset
from sklearn.datasets import load_iris

iris = load_iris()
print(iris.feature_names) # dataset features 
print(iris.data.shape) # metdata
print(type(iris.data)) # data type


# %%
# Create a pandas dataframe with iris data

df_iris = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df_iris


# %%
# df_iris.columns
df_iris.info() # dataframe metadata


# %%
df_iris.describe() # summary of numerical columns
# df.describe(include='all') # some info for string datatype also

# %% [markdown]
# *** Modifying data in dataframe ***

# %%
df_marks = pd.read_csv('./data-files/pandas/studentmarks2.csv', sep=",", header=None)
df_marks


# %%
# setup column names for easy reference
df_marks.columns = ['Name', 'Marks1', 'Marks2']
df_marks


# %%
df_marks.info()


# %%
# Add two new students to the existing data.
df_marks = df_marks.append(pd.DataFrame([['pratul',18,20],['pradeep',25,25] ], columns=['Name','Marks1','Marks2']))
df_marks


# %%
# Notice that there are common index for two students. 
# 
# There are two ways to avoid this situation:
# Either use ignore_index=True option when appending or reset the index as shown below
# df_marks = df_marks.append(pd.DataFrame( [ ['pratul',18,20],['pradeep',25,25] ], columns=['Name','Marks1','Marks2']), ignore_index=True)
df_marks.reset_index() # # This method does not change df_marks until assigned


# %%
df_marks.iloc[7]


# %%
# add a new column of total marks (derived column)
df_marks["Total"] = df_marks["Marks1"]+df_marks["Marks2"]
df_marks

# few more examples
# df_marks['newCriter'] = df_marks['Marks1']*.5+ df_marks['Marks2']
# df_marks['copy'] = df_marks['Total']
# del df['copy']


# %%
# assign names as the index
df_marks.set_index(keys=['Name'], inplace=True) # In order to modify the table use the option inplace=True.
df_marks


# %%
# reset back to normal indexes
df_marks.reset_index(inplace=True)
df_marks


# %%
# Sorting based on a list of columns is easy. This however does not modify the dataframe.
# In order to modify the table use the option inplace=True.

df_marks.sort_values(by=['Total','Marks1'],ascending=[False,True])


# %%
df_marks.drop("Total", axis=1)  # not done inplace


# %%
df_marks

# %% [markdown]
# *** Groupby Operation ***

# %%
df_marks['Grade'] = ['First','Fourth','Fourth','Third',"Third","Third","Second","Second","Second","Third","Second","Second" ]
df_marks


# %%
df_marks['Grade'].value_counts() #groups by column value and provides count sorted


# %%
# Mean score of student by grade
#df_gradeSecond = df_marks[['Marks1', 'Marks2']] # new data frame from two of the columns of existing dataframe
df_grade = df_marks[['Marks1', 'Marks2']].groupby(df_marks['Grade'])
df_grade


# %%
# We can apply aggregate operations like count, sum, max, min, mean, etc. on a group by object
print(df_grade.mean())
print(df_grade.count())

# %% [markdown]
# *** Custom Functions: Apply Method ***
# 
# apply allows to manipulate data using custom function.

# %%
# standard deviation of the marks. There is no built-in aggregate function for std. dev but we can use a fuction from numpy.

df_grade.apply(np.std) 


# %%
# Example: apply on columns
# Capitalize all the names of student 
# using custom function 
def DoCapital(c):
    return c.capitalize()

df_marks['Name'].apply(DoCapital)


# %%
# Example: apply on rows
# using the option axis=1 or axis='columns'
# average marks of students
def FindAvg(row):
    return (row['Marks1']+row['Marks2'])/2

df_marks['Avergage'] = df_marks.apply(FindAvg,axis=1)
df_marks

# %% [markdown]
# *** Pre-Processing ***
# 
# Few functions in Pandas that are handy in converting a raw table to the required format

# %%
# sample dataset of tshirts to play around
# datafile: tshirts.csv
df_tshirts = pd.read_csv('./data-files/pandas/tshirts.csv', sep=",")
df_tshirts


# %%
# Quick observation: 
# # 1. 19 rows
# # 2. Column Brand has 1 NaN
# # 3. Column Price has 2 NaN
df_tshirts.info()

# %% [markdown]
# **** How to handle the missing value? ****

# %%
#1. DROP them
# viable option if no of rows getting impacted is comparitively ignorable if removed
# dropna()

df_tshirts_drop = df_tshirts.copy()
df_tshirts_drop.head(3)


# %%
# handy function dropna
df_tshirts_drop.dropna( subset=['Brand','Price'] , inplace = True)
df_tshirts_drop.info()


# %%
#2. Replace with mean
# viable option for mostly handling missing numeric values 
# if data is random and not particular visible relation in place
# fillna()
df_tshirts_fill = df_tshirts.copy()
df_tshirts_fill['Price'].fillna(df_tshirts_fill['Price'].mean(), inplace=True)
df_tshirts_fill


# %%
#3. Replace with most frequent item
# viable option for mostly handling missing string values 
# mode() - returns a list so we use 0 to pick the first value
# fillna()


# %%
df_tshirts_fill2 = df_tshirts.copy()
df_tshirts_fill2['Brand'].mode()


# %%
#pick any one and fill in to move
df_tshirts_fill2['Brand'].fillna( df_tshirts_fill2['Brand'].mode()[1] , inplace=True)
df_tshirts_fill2


# %%
#4. Replace with mean value of a group
# viable option for mostly handling missing numeric values 
# if data has particular visible relation in place
# fillna()

# price means by brand
df_pmbb = df_tshirts_fill2.groupby('Brand')['Price'].mean()
df_pmbb


# %%
def fill_missing(f):
    f_mean = f.mean()
    return f.fillna( f_mean )

df_fillbygroup = df_tshirts_fill2.groupby(['Brand'])['Price'] # splits into three Series objects-one for each brand
df_fillbygroup.transform( fill_missing ) #passes each of the three Series objects one by one to the function fill_missing & then combines back into one series


# %%
#5. Convert categories (strings) into numbers - easier to work across
# Meaningful order (ORDINAL feature)
# here size can be low to high. 

size_number = {
    'S':0,
    'M':1,
    'L':2,
    'XL':3,
    'XXL':4
}

df_of = df_tshirts.copy()
df_of['Size'] = df_of['Size'].apply(lambda x: size_number[x]) # reassign as apply does not have inplace=True
df_of 


# %%
#6. Convert categories (strings) into numbers - easier to work across
# Random - cannot be ordered (NOMINAL feature)
# here Colors are example of it
# represent each unique color as a (dummy) feature of its own
# Once transformed, for every data point, exactly one feature has the value 1 and the rest of them have zero. 
# This representation is known as one-hot encoding

df_nf = df_of.copy()
df_nf_onehotencoded = pd.get_dummies(df_nf, columns=['Color'], drop_first=True) #drop_first will remove the string column
df_nf_onehotencoded


# %% [markdown]
# *** Reshaping Dataframes ***

# %%
# 1. CROSSTAB - to see the item counts of various different combinations of categories
# Example: https://archive.ics.uci.edu/ml/datasets/Car+Evaluation
# a dataset of cars with categorical attributes. The categories describe how the price of the car, maintenance, space, etc

df_cars = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data', header=None)
df_cars.sample(3)


# %%
# lets define columns for clarity and to playaround
df_cars.columns = ['Buying_Price', 'Maintenance', 'Doors', 'Persons', 'Boot_Space', 'Safety', 'Acceptability']
df_cars.head(3)


# %%
# to see the number of cars of across different price ranges and acceptability. # like cross matrix giving details
pd.crosstab( df_cars['Buying_Price'] , df_cars['Acceptability'], margins=True )


# %%
# 2. MERGE - Similar to join in SQL

df_bikes = pd.read_csv('./data-files/pandas/bike_price.csv')
df_bikes.sample(3)


# %%
df_type= pd.read_csv('./data-files/pandas/bike_type.csv')
df_type.sample(3)


# %%
# clearly both the data can be mapped based on the typenumber, so lets do it
pd.merge(df_bikes,df_type,on='TypeNumber',how='inner')


# %%
#3. MELT - reshapes the dataframe by converting column names into values.

temp_week = {
    'Channel': [ 'BT-TV' ,'CNN','BBC', 'Google'],
    'Mon': [26,26,27,25],
    'Tue': [25,26,27,25],
    'Wed': [27,26,27,25],
    'Thu': [29,28,28,28],
    'Fri': [26,26,27,26],
    'Sat': [26,24,27,25],
    'Sun': [23,23,23,22]
}
df_melt = pd.DataFrame(data=temp_week)
df_melt


# %%
temp_df = pd.melt(df_melt, id_vars=['Channel'], var_name='Day', value_name='Rating')
temp_df.sample(5)


# %%
#4. PIVOT - reverse of MELT
temp_df = temp_df.pivot(index='Channel', columns='Day', values='Rating')
temp_df




