# Arithmetic operators
a, b = 10, 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# Assignment operators
x = 5
x += 3   # x = 8
print(x)
x -= 2   # x = 6
print(x)
x *= 4   # x = 24
print(x)
x /= 6   # x = 4.0
print(x)
x %= 3   # x = 1.0
print(x)
x **= 5  # x = 1.0
print(x)

#Comparison Operators
a, b = 7, 10

print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True

#Logical Operators
x, y = True, False

print(x and y)  # False
print(x or y)   # True
print(not x)    # False

#Bitwise Operators

a, b = 5, 3  # 5 = 0101, 3 = 0011

print(a & b)   # AND: 1
print(a | b)   # OR: 7
print(a ^ b)   # XOR: 6
print(~a)      # NOT: -6
print(a << 1)  # Left shift: 10
print(a >> 1)  # Right shift: 2

#Membership Operators

items = [1, 2, 3]

print(2 in items)      # True
print(5 not in items)  # True

#Identity Operators

a = [1, 2, 3]
b = a
c = a.copy()

print(a is b)     # True (same object)
print(a is c)     # False (different objects)
print(a == c)     # True (same values)
