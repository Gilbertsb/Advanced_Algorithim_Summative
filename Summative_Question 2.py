#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
def function_grading():                            #defining function
    
    studentsgrades=[]                             #making decralation of an array
    n=int(input("Enter number of students: "))     #getting number of students
    for i in range(n):                       
        item=int(input("Enter grade %d:"%i))         #getting grades of each student
        studentsgrades.append(item)
        
    print("\n")
    print("Original grades")
    print("==================")        
    print(studentsgrades)                  #printing original grades
    print("\n")
    print("Final grades")
    print("==================")
    start_time = time.time()                   #start time counter
    for i in range(len(studentsgrades)):       #for each student
        if studentsgrades[i] >= 38:            #if grad is less 38
            near_num = (studentsgrades[i] - (studentsgrades[i] % 5))+5  #check for nearest number wich is mulitple of five
            variant = near_num - studentsgrades[i]                    #finding the differnr b2n nearrest num and grade

            if variant < 3:                                    #as longo difference is less than 3
                studentsgrades[i] = near_num                  #grade will take the value of near number which is multiple of 5
     
    print("Time: %s seconds" % (time.time() - start_time))    #print time used for excution
    return studentsgrades
    

print(function_grading())


#Enter number of student first and then provde all grades for them
#ex:
#Test it with below data

#Number of students: 3
#Enter grade 0: 23
#Enter grade 0: 44
#Enter grade 0: 34



# In[ ]:




