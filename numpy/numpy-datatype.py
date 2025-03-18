import numpy as np

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

arr = np.array([1, 2, 3, 4])
print(arr.dtype)

# Creating Arrays With a Defined Data Type

arr2 = np.array([1, 2, 3, 4], dtype='S')
print(arr2)
print(arr2.dtype)


# For i, u, f, S and U we can define size as well.
# Example
# Create an array with data type 4 bytes integer:

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)