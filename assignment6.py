# everything about numpy 
"""
NUMPY COMPLETE STUDY GUIDE


Library: NumPy (Numerical Python)

NumPy is the core library for numerical computing in Python.
It is used heavily in:
- Data Science
- Machine Learning
- Scientific Computing
- AI frameworks

Most Python ML libraries like Pandas, TensorFlow, PyTorch rely on NumPy.

This file demonstrates:
1. Creating arrays
2. Array properties
3. Indexing and slicing
4. Reshaping arrays
5. Mathematical operations
6. Broadcasting
7. Random numbers
8. Aggregations
9. Boolean indexing
10. Linear algebra
11. Stacking arrays

Study this file by running sections one by one.
"""

# Import NumPy
import numpy as np



# 1. CREATING NUMPY ARRAYS


# Creating a 1D array from a Python list
a = np.array([1, 2, 3, 4, 5])

print("1D Array:", a)

# Creating a 2D array (matrix)
b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n2D Array:")
print(b)

# Creating a 3D array
c = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])

print("\n3D Array:")
print(c)



# 2. ARRAY PROPERTIES


# shape -> dimensions of the array
print("\nShape of b:", b.shape)

# ndim -> number of dimensions
print("Number of dimensions:", b.ndim)

# size -> total elements
print("Total elements:", b.size)

# dtype -> data type
print("Data type:", b.dtype)



# 3. SPECIAL ARRAY CREATION FUNCTIONS


# Array filled with zeros
zeros_array = np.zeros((3,3))
print("\nZeros Array:")
print(zeros_array)

# Array filled with ones
ones_array = np.ones((2,4))
print("\nOnes Array:")
print(ones_array)

# Create numbers from 0 to 9
range_array = np.arange(0,10)
print("\nArange:", range_array)

# Evenly spaced numbers between 0 and 1
linspace_array = np.linspace(0,1,5)
print("\nLinspace:", linspace_array)

# Identity matrix
identity_matrix = np.eye(3)
print("\nIdentity Matrix:")
print(identity_matrix)



# 4. RESHAPING ARRAYS


# Create numbers from 0 to 11
arr = np.arange(12)

print("\nOriginal array:")
print(arr)

# Reshape into 3 rows and 4 columns
reshaped = arr.reshape(3,4)

print("\nReshaped (3x4):")
print(reshaped)



# 5. INDEXING AND SLICING


arr = np.array([10,20,30,40,50])

# Access first element
print("\nFirst element:", arr[0])

# Access last element
print("Last element:", arr[-1])

# Slice elements from index 1 to 3
print("Slice 1:4 ->", arr[1:4])


# 2D indexing

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# Row 1 column 2
print("\nMatrix element (row1,col2):", matrix[0,1])

# Entire row
print("First row:", matrix[0])

# Entire column
print("Second column:", matrix[:,1])



# 6. NUMPY MATHEMATICAL OPERATIONS


a = np.array([1,2,3])

print("\nArray:", a)

# Add number
print("Add 5:", a + 5)

# Multiply
print("Multiply by 2:", a * 2)

# Power
print("Square:", a ** 2)


# Operations between arrays

b = np.array([4,5,6])

print("\nArray addition:", a + b)
print("Array multiplication:", a * b)



# 7. NUMPY MATHEMATICAL FUNCTIONS


a = np.array([1,4,9,16])

print("\nSquare root:", np.sqrt(a))

print("Exponential:", np.exp(a))

print("Logarithm:", np.log(a))

print("Sine:", np.sin(a))



# 8. AGGREGATION FUNCTIONS


data = np.array([10,20,30,40])

print("\nSum:", np.sum(data))

print("Mean:", np.mean(data))

print("Minimum:", np.min(data))

print("Maximum:", np.max(data))

print("Standard deviation:", np.std(data))



# 9. AXIS OPERATIONS


matrix = np.array([
    [1,2,3],
    [4,5,6]
])

# Sum of columns
print("\nColumn sum:", np.sum(matrix, axis=0))

# Sum of rows
print("Row sum:", np.sum(matrix, axis=1))



# 10. BROADCASTING


# Broadcasting allows arrays with different shapes to work together

a = np.array([
    [1,2,3],
    [4,5,6]
])

b = np.array([10,20,30])

# NumPy automatically expands b to match a
result = a + b

print("\nBroadcasting result:")
print(result)



# 11. RANDOM NUMBERS
 

# Random numbers between 0 and 1
print("\nRandom matrix:")
print(np.random.rand(3,3))

# Random integers
print("\nRandom integers:")
print(np.random.randint(0,10,(3,3)))

# Normal distribution
print("\nRandom normal distribution:")
print(np.random.randn(3,3))



# 12. BOOLEAN INDEXING


a = np.array([1,2,3,4,5,6])

# Condition
condition = a > 3

print("\nCondition:", condition)

# Filtering using condition
print("Values greater than 3:", a[a > 3])

# 13. STACKING ARRAY


a = np.array([1,2,3])
b = np.array([4,5,6])

# Vertical stack
print("\nVertical stack:")
print(np.vstack((a,b)))

# Horizontal stack
print("\nHorizontal stack:")
print(np.hstack((a,b)))



# 14. LINEAR ALGEBRA


A = np.array([
    [1,2],
    [3,4]
])

B = np.array([
    [5,6],
    [7,8]
])

# Matrix multiplication
print("\nMatrix multiplication:")
print(np.dot(A,B))

# Transpose
print("\nTranspose:")
print(A.T)

# Determinant
print("\nDeterminant:")
print(np.linalg.det(A))

# Inverse
print("\nInverse:")
print(np.linalg.inv(A))



# 15. COPY VS VIEW



original = np.array([1,2,3])

# Copy creates new memory
copy_array = original.copy()

copy_array[0] = 100

print("\nOriginal:", original)
print("Copy:", copy_array)

# View shares memory
view_array = original.view()

view_array[1] = 200

print("\nOriginal after view change:", original)
print("View:", view_array)





