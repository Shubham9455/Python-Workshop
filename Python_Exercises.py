
# ## Exercises
"""
  Shubham Jaiswal
  Electronics Engg
  1st Year
"""

# Answer the questions or complete the tasks outlined in bold below.


def power(a,b):
    
    # ** What is 7 to the power of 4?**
    
    return a**b



def split_str(s):
    
    # ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **

    return s.split()


def format(planet= "Earth",diameter= 12742):
    
# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.
    return "The diameter of {p} is {x} kilometers.".format(p=planet,x=diameter)





def indexing(lst):
    
# ** Given this nested list, use indexing to grab the word "hello" **

#lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

    return lst[3][1][2][0]


def dictionary(d):
    
# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


    return d['k1'][3]['tricky'][3]['target'][3]


def subjective():
    
# ** What is the main difference between a tuple and a list? **
# Tuple is _______
    return str("immutable")




def domainGet(email):
    
    # ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**
    l = email.split('@')
    return l[1]


def findDog(st):
    
# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

    return 'dog' in st.lower()


def countDog(st):

# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

    return st.lower().count('dog')



def lambdafunc(seq):
    
    # ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']

    return list(filter(lambda item: item[0]=='s',seq))


def caught_speeding(speed, is_birthday):
    
    
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **
    l = [60,81]
    if is_birthday:
        l = [x+5 for x in l]
    print(l)
    if speed<=l[0]:
        return 'No Ticket'
    elif speed>=l[1]:
        return 'Big Ticket'
    else:
        return 'Small Ticket'


## Numpy Exercises

import numpy as np


def create_arr_of_fives():
    
  #### Create an array of 10 fives
  #### Convert your output into list 
  #### e.g return list(arr) 
  arr = 5*np.ones(10,dtype=np.int16)
  return list(arr)



def even_num():
    
  ### Create an array of all the even integers from 10 to 50
  ### Convert your output into list 
  ### e.g return list(arr) 
  arr = np.arange(10,51,2)
  return list(arr)



def create_matrix():
    
  ### Create a 3x3 matrix with values ranging from 0 to 8
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  arr = np.arange(9)
  l = arr.reshape(3,3)
  return l.tolist()



def linear_space():
    
  ### Create an array of 20 linearly spaced points between 0 and 1
  ### Convert your output into list 
  ### e.g return list(arr) 
  l = np.linspace(0,1,20)
  return list(l)


def decimal_mat():
    
  ### Create an array of size 10*10 consisting of numbers from 0.01 to 1
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  arr = np.arange(1,101,1)
  arr = arr/100
  l = arr.reshape(10,10)
  return l.tolist()



def slices_1():
    
  # This is a given array
  arr = np.arange(1,26).reshape(5,5)
  # array([[ 1,  2,  3,  4,  5],
  #      [ 6,  7,  8,  9, 10],
  #      [11, 12, 13, 14, 15],
  #      [16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])

  # Write a code to slice this given array
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  # array([[12, 13, 14, 15],
  #      [17, 18, 19, 20],
  #      [22, 23, 24, 25]])

  return arr[2:,1:].tolist()



def slices_2():
    
  # This is a given array
  arr = np.arange(1,26).reshape(5,5)
  # array([[ 1,  2,  3,  4,  5],
  #      [ 6,  7,  8,  9, 10],
  #      [11, 12, 13, 14, 15],
  #      [16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])

  # Write a code to slice this given array
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  # array([[ 2],
  #      [ 7],
  #      [12]])
  arr = arr[:3,1:2]
  return arr.tolist()



def slices_3():
    
  # This is a given array
  arr = np.arange(1,26).reshape(5,5)
  # array([[ 1,  2,  3,  4,  5],
  #      [ 6,  7,  8,  9, 10],
  #      [11, 12, 13, 14, 15],
  #      [16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])

  # Write a code to slice this given array
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  # array([[16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])
  arr =   arr[3:]
  return arr.tolist()

# Great job!


