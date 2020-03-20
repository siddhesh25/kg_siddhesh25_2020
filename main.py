#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
str_input=input().split()        #Split two inputs from the string and store it in a list 'str_input'
#We need to whether a one-to-one character mapping exists from one string, s1, to another string,s2.
#Checking if both the strings are defined. If not, throw an error.
if(len(str_input)==0):
    sys.exit("Enter strings s1 and s2 with space in between");
if(len(str_input)==1):
    sys.exit("Enter strings s1 and s2 with space in between");
s1 = str_input[0]                #Splitting both strings into s1 and s2. The list str_input first element has s1.
s2 = str_input[1]                #Splitting both strings into s1 and s2. The list str_input second element has s2.
str_dict = dict()
is_unique = True
for character in s1:             #Looping through the first string
    if(not str_dict.get(character, False)):   #Checking if the character exists in the dictionary or not
        str_dict[character] = character       #If does not exists then enter in the dictionary for further use if required 
    else:
        is_unique = False                     #If does not exists then set the flag to false
        break
#print the result based on flag
if is_unique:
    print("True")
else:
    print("False")


# In[ ]:




