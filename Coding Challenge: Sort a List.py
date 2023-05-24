"""

Can you use all the list methods you just learned to sort a list of numbers from least to greatest?

Here are the steps:

    You must loop through each index of the list. For each index:
        Loop through all earlier indices.
        If the value at an earlier index is greater than the value at the current index:
            Pop the value at the current index
            Insert the popped value into the earlier index
            Stop looking though the earlier indexes

""""
import random

list = []

for i in range(10):
    list.append(random.randint(-10,10))

print("unsorted list: " + str(list))

# Use len(list) to get the length of a list
# Use ‘for index in range(len(list))’ to loop over the indexes of a list
"""If the value at an earlier index is greater than the value at the current index:

    Pop the value at the current index
    Insert the popped value into the earlier index
    Stop looking though the earlier indexes
"""
for i in range(len(list)): # i is the CURRENT INDEX
    for j in range(i):     # j is the EARLIER INDEX
        if(list[ j] > list[ i ]):
            list.insert( j , list.pop( i ))
            break
#list.sort()
print("sorted list: " + str(list))
