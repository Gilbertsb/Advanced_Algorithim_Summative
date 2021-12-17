#!/usr/bin/env python
# coding: utf-8

# In[4]:


def Superdig(n, k):    #function decalaration
    init_str = n        #intial str taking value of n
    for i in range(1, k):       #loop to go multiply string by k
        n += init_str     # Concatenating strings
    p=int(n)            #transforming strng into interger
    if (p == 0):        #if p is zero
        return 0        #return zero
    if (p % 9 == 0):    #if p is dicisable by 9 and 
        return 9         #return 9
    else:                #else
        return (p % 9)    #find the remind of p by 9

#test cases
n = "11237"
k = 2
print(Superdig(n, k))


# In[ ]:




