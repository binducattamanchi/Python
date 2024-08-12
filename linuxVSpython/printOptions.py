#!/usr/bin/env python
# coding: utf-8

# In[69]:


#Print options in python
#Print list in 6 ways

#1: using star
print("\nusing Star *: ")
sampleList =[1,2,3,4,5]
print(*sampleList,sep=" ")
#2: using for loop

print("\nusing for Loop : ")
for i in range(len(sampleList)):
    print (sampleList[i])

print("\nusing for Loop : ")
for i in sampleList:
    print(i)
#3: using join

print("\nusing Join : ")
a=['a','b','c','d','e']
print(''.join(a))

#4: using str

print("\nusing str : ")
print(str(sampleList)[1:-1])

#5: using map

print("\nusing map : ")
print('|'.join(map(str,sampleList)))

#6: List comprehension

print("\nusing List : ")
[print(i,end=' ') for i in sampleList]

#7: Nested List

print("\nNested List : ")
nested_list = [[101, 102, 103], [104, 105, 106], [107, 108, 109]]

for subList in nested_list:
    for items in subList:
        print(items,end=" ")
    print()
    
#8: Adding index to my list

print("\nIndexing to List : ")
my_list = ["apple", "banana", "orange"]

# Using enumerate to print list with index numbers
for index, value in enumerate(my_list):
    print(f"{index}: {value}")
    

#string print option
#1: format()

print("\nString printing 1: ")
name = "bindu"
gpa = 75
print("Name: {}, GPA: {}".format(name, gpa))
#2: printf

print("\nString printing 2: ")
print(f"Name:",name,"GPA:",gpa)
#3: using %

print("\nString printing 3: ")
print("Name: %s, GPA: %d" % (name, gpa))


# In[ ]:




