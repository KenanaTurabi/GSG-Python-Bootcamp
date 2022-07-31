#!/usr/bin/env python
# coding: utf-8

# In[24]:


#Assignment2
#Question1
#part1

# a simple time module Just save the time before and after the execution of code and subtract them! 
#But this method is not precise as there might be a background process momentarily running which
#disrupts the code execution and you will get significant variations in the running time of small code snippets.

#timeit runs the snippet of code millions of times (default value is 1000000) 
#so that we get the statistically most relevant measurement of code execution time


#part2&3
#the previos method
import functools
import time
def timer(func):
    """print sth"""
    def wrapper(*args,**kwargs):
        start=time.perf_counter()
        value=func(*args,**kwargs)
        end=time.perf_counter()
        run_time=end-start
        print(run_time)
        return value
    return wrapper
@timer
def waste_time(num):
    for x in range(num):
        sum([i**2 for i in range (10000)])
        
waste_time(1000)
waste_time(1)


# In[ ]:


#the new methos 
#note: i couldn't run it correctly 
import timeit
from functools import wraps
    
def tool(func):
    """Include debug statement and timeit setup"""
    @wraps(func)
    def wrapper(*args):
        print(func.__doc__, args)
        res = func(*args)
        print(res)
        times = timeit.repeat(
            stmt=lambda: func(*args),
            repeat=3, number=10000)
        print(times)
    return wrapper

@tool
def fun(num):
    for x in range(num):
        sum([i**2 for i in range (10000)])
fun(1000)


# In[7]:


#Logic problem
#Question2

def func2(arr,num):
    arr.sort(reverse = True)
    for i in range(num):
        print(arr[i],end=" ")
    
arry = [1, 23, 12, 9, 30, 2, 50]
k=3
func2(arry,k)


# In[11]:


#Python Built-in functions
#Question3
def func3(int_value,str_value,list_values):
   if isinstance(int_value,int):
    if isinstance(str_value,str):
        if isinstance(list_values,list):
            return True
   return False     
        
        
x=3
y="hello"
z=["ok","yes","yup"]
print(func3(x,y,z))
print(func3(y,x,z))    
print(func3(z,y,x))
      

#Is is_instance the best way to check types ?? No because we can check types like this --> type(x) is int ---> this method needs
#less execution time

print(type(x) is int)
print(type(y) is list)
print(type(z) is list)







