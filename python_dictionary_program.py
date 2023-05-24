import random

names = ['John', 'Jimmy', 'James', 'May', 'Vince']
scores = []
for i in range(5):
    scores.append(random.randint(50,100))

print("names : " + str(names))
print("scores : " + str(scores))


dictionary = {}

for key in names:
    for value in scores:
        dictionary[key] = value
        scores.remove(value)
        break
       
print("Resultant dictionary is : " + str(dictionary))
#---------------------------------

# Loop through both values and keys at the same time
for i,j in dictionary.items():
    print(i,j)
    
# Loop through values in dictionary
for i in dictionary.values():
    print(i)

# Loop through keys in dictionary
for j in dictionary.keys():
    print(j)
