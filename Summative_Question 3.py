#!/usr/bin/env python
# coding: utf-8

# In[70]:


import random 
 
def encrypt(s: str) -> str: 
    L = list(s) 
    random.shuffle(L)  # shuffling text
    return "".join(L)   #return shufled text


def decrypt(Ogtext, encrytext):
    decrtext=''              #variable to keep decrypted text
    for i in Ogtext:        # for each character in orign text 
        if i in encrytext:  # if charcter is encrypted text
            decrtext+=i      #re-arrange accourding to og 
        
    return decrtext         #return decrypted text


#test case
text="Kigali is nice"
print("Origin text:", text)     #Og text

print("Encrpted text :", encrypt(text))   #encry text

print("Decrpted text :", decrypt(text, encrypt(text)))   #decrytext

 


# In[ ]:




