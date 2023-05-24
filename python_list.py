list = ['h','e','l','l','o']

for i in list:
    print(i)
\
--------------------------------
\
#To add more items to the list, you can use the list.append() method. Check it out:
list = ['h','e','l','l','o']
list.append('w')
list.append('o')
list.append('r')
list.append('l')
list.append('d')

for i in list:
    print(i)
    
    
#    \
#--------------------------------
#\
"""Another important method is insert(). 
It lets you insert an entry at any index in a list. 
Any entries at that location or after it will be pushed up one index."""

list = ['h','e','l','l','o']
print(list)
print(list[1])

list.insert(1,'X')
print(list)
print(list[1])
print(list[2])

#\

#------------------------------------

#\
#Pop() removes an entry at any index on the list. It returns the value at the entry it removes.
\
list = ['h','e','l','l','o']
print(list)
print(list[1])

val = list.pop(1)
print(list)
print(list[1])

list.insert(1,val)
print(list)

#----------------------------------------------
\
"""

in is another useful tool when you're using lists. It checks if an element is currently in a list and returns True or False.
"""
list = ['h','e','l','l','o']
print('h is in list?: ' + str('h' in list))
print('x is in list?: ' + str('x' in list))

\
#-------------------------------------------






   
