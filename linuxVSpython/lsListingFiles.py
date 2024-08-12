#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Linux VS Python : Notebook 1: Listing files in a directory i.e.,equvivalent to "ls <dir>" 
#print list of files in a given directory, with multiple options available in Python
#Step 1: Using Functions: listdir(), glob(),iglob(),walk(),scandir()
#Step 2: Using filters with above functions
#Step 3: Save output to file


# In[ ]:


import os


# In[ ]:


print("***********Python Program to print list the files in a directory.**********")
#Direc = input(r"Enter the path of the folder: ")
Direc = "C:\\Users\\bindu\\Documents"


# In[ ]:


#printing using listdir()
print(f"**********Files in the directory using Listdir(): {Direc} *********")
files = os.listdir(Direc)
print(*files, sep="\n")


# In[ ]:


#Filtering only the files
print("*********Printing files only objects***********")
files=[f for f in files if os.path.isfile(Direc+'/'+f)]
print(*files, sep="\n")


# In[ ]:


#Filtering only the files ending with pdf
print("*********Printing files ending with pdf ***********")
for x in files:
    if x.endswith(".pdf"):
        print(x)

