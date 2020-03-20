#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
#We need to check whether a one-to-one character mapping exists from one string, s1, to another string,s2.
#Checking if both the strings are defined frm input argument. If not, throw an error.
if(len(sys.argv) != 3):
    sys.exit("Enter strings s1 and s2 with space in between");
s1 = sys.argv[1]                 #Splitting both strings into s1 and s2.
s2 = sys.argv[2]                 #Splitting both strings into s1 and s2.
if(len(s1) != len(s2)):
    sys.exit("Enter strings s1 and s2 of same length as it is assumed that one on one mapping is required");
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
    print("True");
else:
    print("False");


# In[ ]:




