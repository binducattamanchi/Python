#!/usr/bin/env python
# coding: utf-8

# In[16]:


#Find the size of given file
#3 different methods

import os

#1: using stat

file='/Users/bindu/Documents/a.pdf'
file_size =os.stat(file)

print("Full stat: ",file_size , "\n Size of file : ", file_size.st_size, "bytes")


#2: using path
a=os.path.getsize(file)

print("File Size is :", a, "bytes")


#3: using seek and tell
# open file 
file = open('/Users/bindu/Documents/a.pdf')
 
# get the cursor positioned at end
file.seek(0, os.SEEK_END)
 
# get the current position of cursor 
# this will be equivalent to size of file
print("Size of file is :", file.tell(), "bytes")


# In[ ]:




