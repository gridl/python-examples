# Python script of some samples
# Author: Sandeep Mewara
# Location: Learn By Insight
# Github: https://github.com/samewara/python-examples/blob/master/python-samples.py
# #####################################
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ## PYTHON EXAMPLES ##
# %% [markdown]
# *** Palindrome ***

# %%
def ispalindrome(x):
    reverse_x = str(x)[::-1] #convert to string and then read reverse
    return str(x) == reverse_x

print("IsPalindrome(123321):",ispalindrome(123321))

# %% [markdown]
# *** Sum of Squares ***

# %%
def sumsquares(n):
    return sum(map(lambda x:x**2, range(1,n+1))) #Anonymous function was enough to define square of numbers range 1 to n

print("SumOfSquare(5):", sumsquares(5))

# %% [markdown]
# *** Sort Students marks list ***

# %%
# data-file: studentmarks1.csv
student_marks1 = open('./data-files/python-samples/studentmarks1.csv','r')
marks_list = student_marks1.read().splitlines()
marks_list


# %%
marks_dict = {} #hve the entire data in dictionary as key-value pair to sort 
for studententry in marks_list:
    name,marks = studententry.split(',')
    marks_dict[name]= int(marks)

sorted(marks_dict.items(), key=lambda x:x[1], reverse=True) #use sorted on marks data 

# %% [markdown]
# *** Sort Students marks list based on two columns, 1st column is priority, 2nd to decide if tie ***

# %%
# data-file: studentmarks2.csv
student_marks1 = open('./data-files/python-samples/studentmarks2.csv','r')
marks_list = student_marks1.read().splitlines()
marks_list


# %%
marks_dict = {} #hve the entire data in dictionary as key-value pair to sort 
for studententry in marks_list:
    name,marks1,marks2 = studententry.split(',')
    marks_dict[name]= float(marks1), float(marks2) #tuple stored for each key

sorted(marks_dict.items(), key=lambda x:(x[1][0],x[1][1]), reverse=True) #x[1] => marks tuple. x[1][y] => yth location in tuple. (1,2) < (1,3) 

# %% [markdown]
# *** Format Students marks list to 2 decimal places in table ***

# %%
# data-file: studentmarks2.csv
student_marks1 = open('./data-files/python-samples/studentmarks2.csv','r')
marks_list = student_marks1.read().splitlines()
marks_list


# %%
for ml in marks_list:
    name,marks1,marks2 = ml.split(',')
    print("{0:10s} {1:.2f} {2:.2f}".format(name,float(marks1),float(marks2)))
    # Refer for formatting: https://www.python-course.eu/python3_formatted_output.php

# %% [markdown]
# *** Word Frequency ***
# 
# The file <code>novel_conard.txt</code> contains the text of a book by Joseph Conard. We wish construct a dictionary that stores the number of times each word appears. Common words like <code>an, the, is, by</code>  are called stop words are not of much interest. So we want to construct a word frequency dictionary after removing the stop words from the novel. The list of stop_words is given in the file <code>stopwords.txt</code>.

# %%
novel_file = open('./data-files/python-samples/novel_conard.txt','r')
novel_text = novel_file.read().splitlines()
novel_text[0:10]


# %%
stop_file = open('./data-files/python-samples/stopwords.txt','r')
stop_word_list = stop_file.read().splitlines()
stop_word_list[0:10]


# %%
novel_text = " ".join(novel_text) # convert into continous text
novel_text [0:50]


# %%
novel_words = novel_text.split()


# %%
words_dict={}
for word in novel_words:
    if word.lower() not in stop_word_list:
        words_dict[word]=words_dict.get(word,0)+1

print("No. of words in Words dictionary:", len(words_dict))
print("Top 10 words with frequency are:")
sorted(words_dict.items(), key=lambda x:x[1], reverse=True)[:10] #show top 10


# %%
#END of few examples


