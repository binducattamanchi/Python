#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Linux VS Python : Notebook 1: Listing files in a directory i.e.,equvivalent to "ls <dir>" 
#print list of files in a given directory, with multiple options available in Python
#Step 1: Using Functions: listdir(), glob(),iglob(),walk(),scandir()
#Step 2: Using filters with above functions
#Step 3: Save output to file

import os
import sys
import glob
try:
    print("***********Python Program to print list the files in a directory.**********")
    #Direc = input(r"Enter the path of the folder: ")
    Direc = "C:\\Users\\bindu\\Documents"
    #printing using listdir()
    print(f"**********Files in the directory using Listdir(): {Direc} *********")
    files = os.listdir(Direc)
    print(*files, sep="\n")
    #Filtering only the files
    print("*********Printing files only objects***********")
    files=[f for f in files if os.path.isfile(Direc+'/'+f)]
    print(*files, sep="\n")
    #Filtering only the files ending with pdf
    print("*********Printing files ending with pdf ***********")
    for x in files:
        if x.endswith(".pdf"):
            print(x)
    #printing using walk()
    print(f"**********Files in the directory using Listdir(): {Direc} *********")
    files = os.walk(Direc)
    print(*files, sep="\n")
    
    #printing using walk()
    print("*********Printing files with filter using os.walk():")
    list= []
    for (root,dirs,files) in os.walk(Direc) :
        for f in files:
            if f.endswith(".pdf") :
                print(f)
    #printing using scandir()
    print("*********Printing files with filter using os.scandir():")
    obj = os.scandir()
    print("Files and Directories in '% s':" % Direc)
    for e in obj:
        if e.name.endswith(".py"):
            print(e.name)
        if e.is_file():
            print(e.name) 
    #printing using scandir()
    print("*********Printing files with filter using glob and iglob:")
    print('\nFiles and Directories:')
    for files in glob.glob(Direc + '*'):
        print(files)
    print('\nNamed with pdf:')
    for files in glob.glob(Direc + '/*.pdf'):
        print(files)
    print('\nNamed with pdf:')
    for file in glob.iglob(Direc + '/*.pdf', recursive=True):
        print(file)
    
            
    
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert list to an string.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
        


