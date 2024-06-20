import numpy as np

# Generating arrays using built-in NumPy functions
# Create an array of zeros
zeros_arr = np.zeros((2, 3))  # 2x3 array filled with zeros
print("Array of Zeros:")
print(zeros_arr)

# Create an array of ones
ones_arr = np.ones((3, 2))  # 3x2 array filled with ones
print("\nArray of Ones:")
print(ones_arr)

# Create an array filled with a specific value
value_arr = np.full((2, 4), 5)  # 2x4 array filled with value 5
print("\nArray filled with a specific value:")
print(value_arr)

# Create an identity matrix
identity_mat = np.eye(3)  # 3x3 identity matrix
print("\nIdentity Matrix:")
print(identity_mat)

# Reshaping arrays
arr7 = np.arange(1, 10)  # Create an array from 1 to 9
print("Original Array:")
print(arr7)

# Reshape to a 3x3 matrix
reshaped_arr = arr7.reshape(3, 3)
print("\nReshaped to 3x3 Matrix:")
print(reshaped_arr)

# Transpose the matrix
transposed_arr = reshaped_arr.T
print("\nTransposed Matrix:")
print(transposed_arr)

# Random number generation with NumPy
# Generate a random float between 0 and 1
rand_float = np.random.random()
print("Random Float:")
print(rand_float)

# Generate a random integer between a specified range
rand_int = np.random.randint(1, 100)  # Random integer between 1 and 100
print("\nRandom Integer:")
print(rand_int)

# Generate random numbers from a normal distribution
normal_dist = np.random.normal(0, 1, size=(3, 3))  # Mean 0, standard deviation 1
print("\nRandom Numbers from Normal Distribution:")
print(normal_dist)

# Array indexing and slicing
arr5 = np.array([10, 20, 30, 40, 50])

# Accessing elements
print("Array:", arr5)
print("First element:", arr5[0])  # Output: 10
print("Last element:", arr5[-1])  # Output: 50

# Slicing
print("\nSlicing:")
print("First three elements:", arr5[:3])  # Output: [10 20 30]
print("Elements from index 1 to 3:", arr5[1:4])  # Output: [20 30 40]

# Boolean indexing
mask = arr5 > 30
print("\nBoolean indexing (elements > 30):")
print(arr5[mask])  # Output: [40 50]
