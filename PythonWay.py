#Lambda Function

def old_add(a,b):
    return a + b

new_add = lambda a,b: a+ b

print(old_add(2,4))
print(new_add(2,4))

unsorted = [('b', 6), ('a', 10), ('d', 0), ('c', 4)]
# Sort on the second tuple value (the integer).
print(sorted(unsorted, key=lambda x: x[1]))


#First Class Functions - ability to pass in functions as arguments
#functions take in a Python iterable, and, like sorted, apply a function for each element in the list

# 1. Map Function
#map() to add 10 or 20 to every element in a list:
values = [1, 2, 3, 4, 5]
add_10 = list(map(lambda x : x+10, values))
print(add_10)

print([x + 10 for x in values])

# 2. Filter Function
#filter odd or even values from a list:
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x: x % 2 == 0 , values))
print(even)
print([x for x in values if x % 2 == 0])

#3. Reduce Function
from functools import reduce
values = [1, 2, 3, 4]
summed = reduce(lambda x,y : x + y, values)
print(summed)
print(x for x in values)

#Rewriting List Comprehension

