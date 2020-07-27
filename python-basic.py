# Python script of the basic operations
# Author: Sandeep Mewara
# Location: Learn By Insight
# Github: https://github.com/samewara/python-examples/blob/master/python-basic.py
# #####################################
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ## Data Types
# %% [markdown]
# ***Variables and Conditionals***

# %%
x = 21
print ('x:',x,type(x)) #type is defined by the value it refers to
y = 4.1
print ('y:',y,type(y))
x = x * y
print ('x:',x,type(x)) #type of value it refers to can change over the course of program execution
x = 'Sandeep Mewara'
print ('x:',x,type(x)) #str - string


# %%
#some simple operations
x=2
x+=10 # x=x+10
print (x)

x*=5  # x=x*5
print (x)

x = 10
print (x**2) #raise to the power of 2

# %% [markdown]
# *** Conditional statements ***

# %%
x=75
if x > 100:
    print ("More")
elif x > 70:
    print ("Less")
else:
    print ("Not defined")


# %%
x,y = 10,5  # x = 10;y = 5
if x > 5 and y<10: # 'and' evaluates to true only if all the conditions are true
    print ('and condition')

if x > 10 or y == 5: # 'or' evaluates to true if either of the condition are true
    print ('or condition')

if not x == 100: # 'not' toggles true to false & vice versa
    print ('not condititon')

# %% [markdown]
# *** String manipulations ***

# %%
s = "Python for Machine Learning"
print (s[0]) #Print the first character

t = 'Data Science'
q = """is awesome!
Know it's power."""
print (t, q)
print (q[3:11])


# %%
s = 'Python for Machine Learning.' 
print (s*2) # '*' operator on string repeats the string

v = "... Learn by Insight!!!" 
t = s + v # concatenate strings
print(t)


# %%
s="sandeep mewara" 

#s[0]='H' #trying to replace ’h’ with ’H’ => INCORRECT
s = s.replace('s','S')
print (s)
t = s.replace('m','M')
print (s,',',t) # original string is preserved


# %%
x = "I got my BTech from %s in year %d" %('IIT',2005) # string construction
print(x)

# %% [markdown]
# ***Type conversion***

# %%
a,b='18','54.8'
print (a+b) # a,b => they are strings, not numbers.


# %%
s,t=5,10
print (str(s)+str(t)) # non-string to string add
print (s+t) # normal add

# %% [markdown]
# ***Formatting Strings***

# %%
#% is a format operator and %d, %s, %f are special format sequences

print("%15s"%"FillWord") # right align in a column width 15
print("There is %-8s space"%"more") # negative number for left alignment

print("%4d"%42) #convert to 4 decimals
print("%04d"%42) #pack leading zeros

print("%.3f"%42.34656) # %.<fixed number of digits to the right of Dot.>f
print("%.5f"%42.34)


# %%
print ("Formatting using the format func: {0:.3f}lakh {1:02d}km {2:5s}".format(2.1,4,"LearnByInsight"))


# %%
print ('milk' in 'milky way')
print ('a' in 'milk')

# %% [markdown]
# ## Data Structures
# %% [markdown]
# ***List***

# %%
# indexed by integers, starting from 0.

l=[1,2,3,5,8,13] #items of the same type
print (l)

lst=[1,'x',2,'t',3.0] #items of mixed types
print (lst)


# %%
lst = [1,2,3,5,8,'sm',13,21,34]
print ("List:",lst)
print ("Length of the list:",len(lst)) #length of the list

pop_element = lst.pop() #pop by default removes & returns the last element from the list
print ("Popped out element:%s,\nList after pop operation:%s"%(pop_element,lst))

lst.pop(2) #pop can also be used to remove an element based on index starting from 0
print (lst)


# %%
lst = [1,2,3,5,8,'sm']
print ("Before deleting:",lst)
del lst[len(lst)-1]
print ("After deleting 2nd element",lst)


# %%
lst = [1,2,3,5,8,'sm']
lst.insert(2,"insert") #insert at an index
print (lst)


# %%
lst = [1,2,3,5,8,'sm']
last_element = lst[-1] #negative index to access list elements from the end, -1 refers to the last element of the list
last_element


# %%
# List copy

x = [1,2,3,5,8]
x_copy = x #copy the contents of the list x
x_copy[3] = -3 # change the content of the new list x_copy
print (x,x_copy) # change made to the copied list affects original list too


# %%
#List Splicing

x = [1,2,3,5,8,'sm']
x_copy = x[:] # [start:end:step] default step 1. Returns a new list from start to end-1

print ("List x:",x)
print ("List x_copy", x_copy)

print ("x[1:3]=%s, x[:3]=%s, x[2:]=%s, x[-2:]=%s"%(x[1:3],x[:3],x[2:],x[-2:]))
print ("x[1:5:2]=%s"%x[1:5:2] ) #with step 2


# %%
x = [1,2,3,5,8,'sm']
print (x)
del x[1:3] # Remove more than one element
print (x)


# %%
lst = [1,2,3,5,8,'sm']
print ("List:",lst)

lst.append(13)  #add a single element
print ("Appending single element 13:",lst)

lst.extend([-13,-8]) #add more than one element
print ("Adding more than one element -13 & -8:",lst)


# %%
lst = [1,2,3,5,8,'sm']
lst.append([-5,-8]) #list of list
print ("Appending a list [-5,-8]:",lst)

mat = [[2,1],[4,3]] #Define a matrix
print ("Matrix: ",mat)
print ("Accessing individual elements: 2nd element in 1st row:",mat[0][1])


# %%
lst = [1,2,3,5,8,'sm']
print ("list:",lst) 
print ("5 in list:",5 in lst)
print ('a in list:','a' in lst)


# %%
text = "Machine Learning is awesome !!!"
word_list = text.split() #split by space
print (text,"\nWord list",word_list)

text = "Split,this,string,using,comma,separator"
ex_list=text.split(',') #comma as delimiter
print ("ex_list:",ex_list)


# %%
text = "Machine Learning is awesome !!!"
word_list = text.split()
print ("List of words",word_list)
sentence = " ".join(word_list)
print ("Reconstruct:",sentence)

new_delimiter_sentence = "*".join(word_list) #via different delimiter
print ("Reconstructed using a '*':", new_delimiter_sentence)


# %%
s = "   Water vapor and icy particles errupt from Enceladus  "
t = s.strip() #remove leading and trailing whitespace if no chars is given in strip
print(t)

# %% [markdown]
# ***Tuple***

# %%
t = 1,2,'a','x',3,5
print (type(t),t)
print (t[3]) #access the elements the same way as in Lists
print (t[2:5])

t= (1,'a',2,'x') #Define a tuple enclosing it in a parantheses
print(t)

t = 10  #Tuple with a single element
print (type(t),t)

t = tuple() #an empty tuple
print (type(t),t)

t = tuple('tuple') #Argument string
print (type(t),t) 

t = tuple([1,2,3,5]) #Argument list
print (type(t),t) 

t = tuple(['sm','lbi']) #Argument list
print (type(t),t) 


# %%
d = dict() #create an empty dictionary
print (d)

space_probes = {"voyager1":1977,"cassini":1997,"juno":2011,"mangalyaan":2013} # colon ':', separates the key and value
print (type(space_probes),space_probes)

print (space_probes['juno']) #Accessing dictionary values

# Tuples as keys of the dictionary 
name_id_num = {("Sandeep","Mewara"):24568,("Code","Projct"):7418}
print (name_id_num)
print (name_id_num[("Sandeep","Mewara")])


# %%
# range
x = range(10)
print (type(x),x)

for i in x:
    print (i,end=" ")

print('\nRange defined:')
for j in range(3,9):
    print (j,end=" ")

print('\nRange defined with steps defined:')
x = range(2,21,3)
for i in x:
    print (i,end=" ")


# %%
# while
lst =[7,3,5,2,9,1]
i=0
while lst[i] > 2:
    i=i+1

print (i)


# %%
#continue

x = [1,3,4,8,9,5]
for i in x:
    if i%2 == 0:
        continue 
    print (i) 


# %%
# break
x = [1,2,3,4,-5,8,9]
for i in x:
    if i < 0:
        break
    print (i)


# %%
# zip
lst1 = range(5)
lst2 = range(5,10)

for x,y in zip(lst1,lst2):
    print (x,y,x+y)


# %%
#using zip to find the max element and index in a list
lst = [1,5,2,17,8,-2]
print (max(lst))
lst_index = list(zip(lst,range(len(lst))))
print (lst_index)
print ("Max val and idx",max(lst_index))


# %%
# list comprehension
#Generate the squares of the first 'n' numbers
number_squares = [x*x for x in range(5)]
print (number_squares)

#list of even numbers upto 10
even_nos = [x for x in range(10) if x%2]
print (even_nos)

even_nos = [x for x in range(1,10,2)]
print (even_nos)

#remove spaces from the word list 
word_list = [' river','hills  ',' and','shepherd']
new_list = [word.strip() for word in word_list] #string the leading and trailing spaces
new_list

# %% [markdown]
# ## Functions

# %%
def find_avg(x):
    avg = sum(x)/len(x)
    return avg

print (find_avg([1,2,3,5,8,13]))
print (find_avg([1,-2,3,-5]))


# %%
def prod(x,y,z=1): 
    return (x+1)*(y+2)*(z+3)

print (prod(1,2,3))
print (prod(1,2)) # z default is defined so can be skipped
print (prod(x=1,y=5))
print (prod(z=2,y=1,x=0)) #Supply arguments in arbitary order


# %%
# variable scope
x = 5
y = -5
def check_scope():
    global x 
    x = 10
    y = 20
    print ("x,y => Inside the func:",x,y)

check_scope()
print ("x,y => Outside the func:",x,y)


# %%
def sum_num(x,*y): # can accept a variable number of arguments if we add * to the last parameter name
    print ("Variable length arg:",y)
    s = x
    for i in y:
        s+=i
    return i
print (sum_num(10,20))
print (sum_num(11,22,33,44,55))


