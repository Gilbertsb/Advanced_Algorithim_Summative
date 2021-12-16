#!/usr/bin/env python
# coding: utf-8

# In[6]:


import time

def Sumup(num):             #define a function
    start_time = time.time() #starting time count  it will take
    sum=0                     #initialize sum to zero
    for i in range(num+1):    #loop to count all numbers
        sum+=i                #adding to sum
    print("Time: %s seconds" % (time.time() - start_time))   #printing time take for fucntion to run
    return sum                                #returning sum

#Test cases  just uncomment one to check

# Sumup(10)
# Sumup(10000)
Sumup(1000000)
# Sumup(1000000000 )


# In[ ]:




