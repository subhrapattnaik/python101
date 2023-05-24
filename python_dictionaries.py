"""The dictionary is a complex data structure that consists of key-value pairs. 
You can examine each component of a dictionary separately or as key-value pairs (items):"""


dictionary = {'w':'h','o':'e','r':'l','l':'l','d':'o'}

print(dictionary.values())
print(dictionary.keys())
print(dictionary.items())

#------------------------------------
"""output
['h', 'e', 'l', 'l', 'o'] 
['w', 'o', 'r', 'l', 'd'] 
[('w', 'h'), ('o', 'e'), ('r', 'l'), ('l', 'l'), ('d', 'o')] """
#---------------------------------------------

************************************************************
"""Looping

You can loop through a dictionary in multiple ways."""

dictionary = {'w':'h','o':'e','r':'l','l':'l','d':'o'}

values = ""
keys = ""

#Loop though values in dictionary
for i in dictionary.values():
    values+=i

#Loop though keys in dictionary
for j in dictionary.keys():
    keys+=j

print(values+keys)

values = ""
keys = ""

#Loop through both values and keys at the same time with dictionary.items()
for i,j in dictionary.items():
    values+=j
    keys+=i

print(values+keys)

-----------------------------------------------
output
helloworld 
helloworld 

**********************************************************
