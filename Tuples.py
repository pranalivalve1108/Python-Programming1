#Creating a Tuple
fruits = ("apple", "banana", "cherry")
numbers = (5, 4, 3, 2, 1)
mixed = (10, "hello", 2.5, True)
print(fruits, numbers, mixed)

#Accessing elements
print(fruits[0])
print(numbers[2])

#Immutability example
#fruits[1] = "mango"
#Error tuples cannot be modified

#Tuple methods
#count() - count occurrences of a value
t = (1, 2, 2, 3)
print(t.count(2))

#index() - return index of a value
print(t.index(1))

#Counter function without using count function
from collections import Counter
t1 = (1, 1, 1, 2, 2, 2, 3, 3, 3, 4)
counter = Counter(t1)
print(counter)