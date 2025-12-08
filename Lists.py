#Creating a List
fruits = ["apple", "banana", "cherry"]
numbers = [5, 4, 3, 2, 1]
mixed = [10, "hello", 2.5, True]
print(fruits, numbers, mixed)

#Accessing elements
print(fruits[0])
print(numbers[2])

#Modifying a List
fruits[1] = "kiwi"
print(fruits)

#List methods
#append() - add at the end
fruits.append("orange")
print(fruits)

#insert() - Add at specific index
fruits.insert(1, "mango")
print(fruits)

#remove() - remove a value
fruits.remove("apple")
print(fruits)

#pop() - remove by index
fruits.pop(2)
print(fruits)

#sort() - sort list
numbers.sort()
print(numbers)

#reverse() - reverse the list
numbers.reverse()
print(numbers)

#Looping through a List
for num in mixed:
    print(num)