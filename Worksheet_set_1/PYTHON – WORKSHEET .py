#!/usr/bin/env python
# coding: utf-8

# # Write a python program to find the factorial of a number.
#                 

# In[14]:


num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("The factorial of",num,"is",factorial)


# # Write a python program to find whether a number is prime or composite.

# In[9]:


def PrimeChecker(a):  
    if a > 1:   
        for j in range(2, int(a/2) + 1):   
            if (a % j) == 0:  
                print(a, "is a Composite number")  
                break   
        else:  
            print(a, "is a prime number")  
    
a = int(input("Enter an input number:"))   
PrimeChecker(a)


# # Write a python program to check whether a given string is palindrome or not.

# In[13]:


string = input("Please enter your own String : ")

if(string == string[:: - 1]):
   print("This is a Palindrome String")
else:
   print("This is Not a Palindrome String")


# # Write a Python program to get the third side of right-angled triangle from two given sides.

# In[39]:


import math

a = float(input("Enter base: "))
b = float(input("Enter height: "))

c = math.sqrt(a ** 2 + b ** 2)

print("Hypotenuse =", c)


# In[45]:


import math

a = float(input("Enter base: "))
b = float(input("Enter height: "))

c = math.sqrt(a ** 2 + b ** 2)

print("Hypotenuse =", c)


# # Write a python program to print the frequency of each of the characters present in a given string.

# In[17]:


string=input("Enter the string: ")
str1=list(string)
strlist=[]
for j in str1:
    if j not in strlist:
       strlist.append(j)
       count=0
       for i in range(len(str1)):
         if j==str1[i]:
           count+=1
       print("{},{}".format(j,count))


# In[ ]:




