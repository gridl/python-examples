# Python script of the samples of numpy
# Author: Sandeep Mewara
# Location: Learn By Insight
# Github: https://github.com/samewara/python-examples/blob/master/numpy-basic.py
# #####################################
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ## NUMPY SAMPLES ##

# %%
import numpy as np

# %% [markdown]
# *** Random Walk simulation ***
# 
# 1000-step random walk exercise where a person starting from 0 takes one step to the right(+1) or to the left(-1) with equal probability. To get 'd' being the max distance reached from the origin during the walk. 
# 
# Simulate it (N trials) and find the mean of the max distance of all trails.

# %%
# unit
steps = 1000
rw_seq = np.random.choice([-1,1],steps) #random sequence of steps
net_d = rw_seq.cumsum() #total distance = cumulative sum of all steps
max_d_from_origin = np.max(np.abs(net_d))

print('Max distance from origin: ',max_d_from_origin)


# %%
# for simulation

def simulate_d():
    steps = 1000
    rw_seq = np.random.choice([-1,1],steps) #random sequence of steps
    net_d = rw_seq.cumsum() #total distance = cumulative sum of all steps
    max_d_from_origin = np.max(np.abs(net_d))
    return max_d_from_origin

simulation_count = 100,1000,10000,100000
for i in range(len(simulation_count)):
    max_d_all = [simulate_d() for x in range(simulation_count[i])] # list comprehension - all max_d in a list
    mean_d = np.mean(max_d_all)
    print('Mean distance for {0} simulation is: {1}'.format(simulation_count[i], mean_d))
    
# based on the results, seems the max distance far from origin is around 40

# %% [markdown]
# *** Triangle simulation ***
# With a unit length stick - break into 3 sticks randomly. Carry out N trails and see the probability of finding the right pieces that can form the sides of the triangle using these 3 broken pieces
# 

# %%
# unit validation

stick_l = 1
# this would be incorrect logically as fixed unit length is there
# pieces_length = np.random.rand(2) #2 random numbers between 0 & 1 

#x = pieces_length[0]
#y = pieces_length[1]

x = np.random.uniform(0,1)
y = np.random.uniform(0,1-x)

z = 1 - (x+y)
print ('x:{0},y:{1},z:{2}'.format(x,y,z))

# for triangle to be valid any two side sum should always be greater than third
if(x+y>z and y+z>x and z+x>y):
    print('We got a traingle!')
else:
    print('SORRY! No triangle')


# %%
# for simulation
stick_l = 1

def getxyz():
    x = np.random.uniform(0,stick_l)
    y = np.random.uniform(0,stick_l-x)
    z = stick_l - (x+y)
    return x,y,z

def istriangle(x,y,z):
    if (x+y>z and y+z>x and z+x>y):
        return 1
    else:
        return 0


simulation_count = 100,1000,10000,100000
for i in range(len(simulation_count)):
    triangle_all = [istriangle(*(getxyz())) for x in range(simulation_count[i])] # list comprehension - all true/false in a list
    probability = np.sum(triangle_all)/simulation_count[i]
    print('Probablity for {0} simulation is: {1}'.format(simulation_count[i], probability))
    
    
# based on the results, seems the probablility f formaing triangle from pieces would be just under 20%

# %% [markdown]
# *** Random Number ***
# 
# Generate 10 random numbers in the interval 0,1 and obtain an array X
# 
# Generate another array Y such that $Y[i]$=1 if $X[i]$≥0.5 and 0 otherwise. 

# %%
X = np.random.rand(10)

# Generate the array Y == Random Number
Y = np.where(X>=0.5,1,0)
Y

# %% [markdown]
# *** Pearson's correlation coefficient ***
# 
# Given two arrays $X,Y$, correlation is a measure of linear dependence of values of one array on the other. For example, heights and weights of a group of people are correlated. Validate the below formula for correlation and verify the result using numpy's corrcoef method.
# 
# This is given by $\frac{\sum(X-X_{mean})(Y-Y_{mean})}{\sqrt{\sum(X-X_{mean})^2\sum(Y-Y_{mean})^2}}$  . 
# 

# %%
X = np.random.randint(0,10,20)
Y = X + np.random.randint(20)

X_mean = np.mean(X)
Y_mean = np.mean(Y)

exp = np.sum((X-X_mean)*(Y-Y_mean))
std = np.sqrt(np.sum((X-X_mean)**2) * np.sum((Y-Y_mean)**2))
coeff_corr = exp/std
print('PCC via fomula: ',coeff_corr)
print('PCC via Numpy: ',np.corrcoef(X,Y))

# %% [markdown]
# *** Mean & Variance of crude oil prices ***
# 
# data-file: crude_oil.csv
# Find the mean & the standard deviation of the two types of crude oil. 
# 
# Handle:
# 1. Header
# 2. Missing/Unknown data (should not be part of calcs)

# %%
data = np.genfromtxt('./data-files/numpy/crude_oil.csv',delimiter=";")
# data
# Row1 & Column1 look like not a number here so
data=data[1:,1:]
data


# %%
data = np.genfromtxt('./data-files/numpy/crude_oil.csv',delimiter=";",skip_header=1, encoding=None)
data=data[:,1:]
data


# %%
crude_data = np.nan_to_num(data)
crude_data


# %%
crude1_data = crude_data[~np.isnan(data[:,0])][:,0] #all rows but not nan, 0th column => using masking 
crude2_data = crude_data[~np.isnan(data[:,1])][:,1] #all rows but not nan, 1st column 


# %%
print('crude1_mean:{0},crude2_mean:{1}'.format(np.mean(crude1_data),np.mean(crude2_data)))
print('crude1_sd:{0},crude2_sd:{1}'.format(np.std(crude1_data),np.std(crude2_data)))