#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("enter the number of years")
y=input() 
def number_of_seconds(year) :
    seconds= year*365*24*60*60
    return seconds 
answer= print(number_of_seconds(float(y))) 


# In[2]:


print("enter the temperature in fehrehait")
temp_in_fehrenhait = input()
def convert_to_C (temp):
    temp_in_C=(temp -32)*.5555
    return temp_in_C
answer=print(convert_to_C (float(temp_in_fehrenhait)))


# In[3]:


print ("enter the words")
first=input()
second=input()
third=input()
fourth=input()
fifth=input()
answer="your story is "+first+" "+second+" "+third+" "+fourth+" "+fifth
print (answer)


# In[ ]:




