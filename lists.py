empty_list = []
numbers = [2, 3, 5, 2, 6]
large_animals = ["african elephant", "asian elephant", "white rhino", "hippo", "guar", "giraffe", "walrus", "black rhino", "crocodile", "water buffalo"]

a = large_animals[0]
b = large_animals[5]
# get the last animal in list 
c = large_animals[-1]
# return index number
d = large_animals.index('crocodile')
# accessing slices (chunks) of list - (first element, last element)
e = large_animals[0:3]  # returns indices 0, 1, 2
f = large_animals[3] = 'penguin'  # change value
# delete
del large_animals[3]
# find length
g = len(a)
# can have nested lists 
animal_kingdom = [
  ['cat', 'dog'],
  ['turtle', 'lizard'],
  ['eagle', 'robin', 'crow']
]

biggest_bird = animal_kingdom[-1][0]

# strings are also lists of symbols and can be treated as such 

h = 'this is a list of symbols'
i = h[5:7]

j = h.split(' ')
k = h.split('symbols')

print(j)
print(k)