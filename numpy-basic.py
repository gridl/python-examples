# Python script of the basic operations numpy
# Author: Sandeep Mewara
# Location: Learn By Insight
# Github: https://github.com/samewara/python-examples/blob/master/numpy-basic.py
# #####################################
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ## Numpy (Numerical python)
# 
# Packages for numerical computation designed for efficiency to work on large data sets
# %% [markdown]
# *** Initalizing Matrix - via LIST ***

# %%
import numpy as np


# %%
#mat = np.array([1, 2, 3, 4, 5])

lst = [1,2,3,4,5]
mat = np.array(lst)
mat


# %%
print("mat.shape:", mat.shape)
print("mat[2]:", mat[2])
print("mat.flatten():", mat.flatten())

# %% [markdown]
# *** Initializing Matrix - via NULL MATRIX (ZEROS) ***

# %%
# 5x4 numpy array where the ith row and jth col has the entry i+j
x,y=5,4
matij = np.zeros((x,y))
matij


# %%
for i in range(x):
    for j in range(y):
        matij[i][j] = i+j

matij

# %% [markdown]
# *** Initializing Matrix - via IDENTITY MATRX ***

# %%
size=3
mat_i = np.identity(size)
mat_i

# %% [markdown]
# *** Initializing Matrix - via ONES MATRIX ***

# %%
m,n=3,2
mat_1=np.ones((m,n))
mat_1

# %% [markdown]
# *** Transpose ***

# %%
mat_1=np.ones((m,n))
mat_1_transpose = mat_1.T
mat_1_transpose

# %% [markdown]
# *** Reshape ***

# %%
mat_1=np.ones((m,n))
mat_1_reshape = mat_1.reshape(1,6) #size is still the same 3*2 = 1*6
mat_1_reshape

# %% [markdown]
# *** Indexing ***

# %%
# An array of grand slam information
Players = ['Roger Federer', 'Margaret Court', 'Rafael Nadal', 'Maria Sharapova', 'Pete Sampras', 'Steffi Graf', 'Novak Djokovic']
Titles = [20, 24, 17, 23, 15, 22, 14]
Finals = [30, 29, 25, 29, 24, 31, 19]

grand_slam=np.array([Players,Titles,Finals])
grand_slam


# %%
# select all players from the matrix
grand_slam[0,::1] #0th row & all column, then the indexing of list :: matrix[row, column], row, column are list so start:stop:step


# %%
# select alternate players with data and ten transpose for easy reading

grand_slam[:,::2].T #all of row and all of columns but step jump 2

# %% [markdown]
# *** Simulation #1 *** 
# Simulate the process of rolling a 6 faced die 100 times and find the probability of getting a number that is divisible by 3. 

# %%

trials = 100
draws = np.random.randint(1,7,trials) # Generate 10 random integers in the range 1-6
draws


# %%
draws[draws%3==0] #masking - give all the values back that satisfy the mask in the list


# %%
probab_3 = len(draws[draws%3==0])/trials # or can use .size of the list instead of using len
print("probability for numbers divisble by 3:", probab_3) 


# %%
# simulation with multiple counts
trials_multiple = 100,1000,10000,100000
for i in range(len(trials_multiple)):
    draws = np.random.randint(1,7,trials_multiple[i])
    probab_3 = len(draws[draws%3==0])/trials_multiple[i] # or can use .size of the list instead of using len
    print("probability for numbers divisble by 3 in {0} trials:{1}".format(trials_multiple[i], probab_3)) 

# %% [markdown]
# *** Simulation #2 ***
# Two six-faced dice are rolled. Find the probability that their faces sum to 4.

# %%
trials_multiple = 100,1000,10000,100000
for i in range(len(trials_multiple)):
    draws1, draws2 = np.random.randint(1,7,trials_multiple[i]), np.random.randint(1,7,trials_multiple[i])
    probab_sum4 = len(draws1[draws1+draws2 == 4])/trials_multiple[i] #filter the values
    print("probability for sum be 4 in {0} trials:{1}".format(trials_multiple[i], probab_sum4)) 

# %% [markdown]
# *** Reading CSV Files ***
# 
# data-file: economy_data.CSV
# 
# sample data on a quarterly basis on Indian economy sampled from RBI database containing Gross Value added, Forex, Borrowings for the period 2016 - Q1 2018. Find the correlation among different indicators

# %%
f=open('./data-files/numpy/economy_data.csv')
data = f.read().split('\n')
data


# %%
# For better data read
for content in data[:-1]:
    print("{0:>9s}  {1:9s} {2:7s} {3:10s} {4:4s}".format(*(content.split(','))))


# %%
#read data into numpy array
#skip the header and 1st column
data_np = np.genfromtxt('./data-files/numpy/economy_data.csv',delimiter=",",skip_header=1,usecols=[1,2,3,4],dtype="float32")
print("Data shape:",data_np.shape, ", Data size:",data_np.size, ", Data type:",data_np.dtype)
print(data_np)


# %%
# Correlation between Forex & Borrowing

gva = data_np[:,0] #select all rows from 1st column
forex = data_np[:,1]
borrowing = data_np[:,2]
cpi = data_np[:,3]

print("Corrleation coefficients forex,borrowing\n",np.corrcoef(forex,borrowing))


# %%
# Forex Data in Q2 (17-18)

data_np[5,:]


# %%
# rows where cpi is less than 3

data_np[data_np[:,-1] < 3]


# %%
# average cpi for all the years

np.round(np.mean(cpi),2)

# %% [markdown]
# *** Broadcasting ***
# 
# When two arrays are of different shapes this describes how the arithmetic works between them.
# 
# Arrays are compatible for broadcasting when the trailing dimension match or either of them is of length 1, then the broadcasting is done over the missing dimension or length 1 dimension

# %%
#When trailing dimension match
a=np.array([[1,2,3],[3,4,5]])
b=np.array([8,9,10])
print("shape of a",a.shape," shape of b",b.shape)
a+b #broadcasting on row


# %%
#trailing dimension is 1
b=np.array([[10],[12]])
print("shape of a",a.shape," shape of b",b.shape)
a+b #broadcasting on column


# %%
#vertical/horizontal stacking
a = np.identity(3)
b = np.array([[ 1, 2, 3],
[ 4, 5, 6],
[ 7, 8, 9]])
print("vertical:\n",np.vstack((a,b)))
print("horizontal:\n",np.hstack((a,b)))


# %%
np.concatenate([a,b],axis=0) #same as vstack 

# %% [markdown]
# *** Image Processing ***

# %%
# show an image using matpotlib
import matplotlib.image as mimg
import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
img = mimg.imread('./data-files/numpy/hulk.png') # read an image

original_image_pixels = np.array(img,dtype='float32')  # make an numpy array
print (original_image_pixels) # Note the values are between 0 and 1
plt.imshow(original_image_pixels,cmap='gray'); # use a gray scale color map


# %%
# increase contrast pixel by pixel
contrast_enhanced_pixels = original_image_pixels*3 #increase the contrast; but some values may now be more than 1
contrast_enhanced_pixels[contrast_enhanced_pixels > 1] = 1 #clamp the values to max 1
plt.imshow(contrast_enhanced_pixels,cmap='gray')


# %%



