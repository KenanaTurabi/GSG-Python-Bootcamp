#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Filtering Lists

#Question1 part1 

list1= [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]
list1[-3:]


# In[16]:


#Question1 part2

def fun(item):
    if item<10:
        return True
    else:
        return False
list2=filter(fun,list1)
print(list(list2))


# In[30]:


#List Comprehensions
#Question2
list11= [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]
List22=[x for x in list11 if x<10]
print(list(List22))


# In[ ]:


# list Comprehensions is easier than Filtering lists


# In[32]:


# Modifying Lists
# Map() Function

#Question3
#part1
test_list=[1,2,3,4,5]
def fun(value):
    return value**2

new_list=map(fun,test_list)

print(list(new_list))


# In[33]:


#Question3
#part2
test_list=[1,2,3,4,5]
new_list=[x**2 for x in test_list ]
print(list(new_list))


# In[34]:


#Combining Lists with the Zip() Function
#Question4
numbers=[1,2,3]
chars=['a','b','b']
merged_list=zip(numbers,chars)
print(list(merged_list))


# In[37]:


#Finding the Most Common Item in a List
#Question5
#part1
list_s=['name','name','age','city']
#part2
mySet=set(list_s)
print(mySet)
#part3
print(max (list_s,key=list_s.count))


# In[ ]:




