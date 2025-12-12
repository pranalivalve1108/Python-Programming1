'''
#Creating arrays
import numpy as np

arr1 = np.array([1, 2, 3]) # 1D array
arr2 = np.array([[1, 2], [3, 4]]) # 2D array
arr3 = np.zeros((2, 3)) # Array of zeros
arr4 = np.ones((3, 3)) # Array of ones
arr5 = np.arange(0, 10, 2) # Range array
arr6 = np.linspace(0, 1, 5) # Evenly spaced values

#Array operations
#1. Arithmetic
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)   # [5 7 9]
print(a - b)   # [-3 -3 -3]
print(a * b)   # [4 10 18]
print(a / b)   # [0.25 0.4  0.5 ]

#2. Scalar
print(a * 2)     # [2 4 6]
print(a + 10)    # [11 12 13]

#3. Mathematical
print(np.sqrt(a))    # Square root
print(np.exp(a))     # Exponential
print(np.log(a))     # Logarithm

#4. Aggregation
print(a.sum())       # 6
print(a.mean())      # 2.0
print(a.max())       # 3
print(a.min())       # 1

#5. Matrix
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(np.dot(A, B))       # Matrix multiplication
print(A.T)                # Transpose

#Indexing in NumPy
#1D Array Indexing
import numpy as np
arr = np.array([10, 20, 30, 40])
print(arr[0])   # 10
print(arr[2])   # 30

#2D Array Indexing
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr[0, 1])  # 2 (row 0, col 1)
print(arr[1, 2])  # 6 (row 1, col 2)

#Slicing in NumPy
#1D Array Slicing
arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])    # [20 30 40]
print(arr[:3])     # [10 20 30]
print(arr[::2])    # [10 30 50]

#2D Array Slicing
arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print(arr[0:2, 1:3])

#Mathematical Functions Using NumPy
#1.Basic math functions
#Square Root
import numpy as np
arr = np.array([1, 4, 9, 16])
print(np.sqrt(arr))     # [1. 2. 3. 4.]
#Exponential
print(np.exp(arr))     # e^x for each element
#Logarithm
print(np.log(arr))      # natural log

#2. Trigonometric Functions
angles = np.array([0, np.pi/2, np.pi])
np.sin(angles)
np.cos(angles)
np.tan(angles)

#3.Rounding Functions
vals = np.array([1.1, 2.5, 3.8])
np.floor(vals)   # [1. 2. 3.]
np.ceil(vals)    # [2. 3. 4.]
np.round(vals)   # [1. 2. 4.]

#4.Aggregation functions
arr = np.array([10, 20, 30])
arr.sum()      # 60
arr.mean()     # 20.0
arr.min()      # 10
arr.max()      # 30
arr.std()      # standard deviation

#5. Vectorized function
arr = np.array([1, 2, 3])
print(arr * 10)    # [10 20 30]
print(arr + 5)     # [6 7 8] '''





''' #Reshape a 1D array to 2D
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
new_arr = arr.reshape(2, 3)
print(new_arr) 

#Reshape into 3D
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
new_arr = arr.reshape(2, 2, 2)
print(new_arr) 

#Using -1 (NumPy auto-calculates dimension)
import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60])
new_arr = arr.reshape(3, -1)
print(new_arr) 

#Flatten an array (convert 2D → 1D)
import numpy as np
arr = np.array([[1, 2], [3, 4]])
flat = arr.flatten()
print(flat)   # [1 2 3 4] '''

#Reshape using ravel() (returns a view when possible)
import numpy as np
arr = np.array([[1, 2], [3, 4]])
print(arr.ravel())   # [1 2 3 4]



















