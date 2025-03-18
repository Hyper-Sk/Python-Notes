import numpy as np

# 0d array :
arr1 = np.array(42)
print(arr1)

# 1d array :
arr2 = np.array([1, 2, 3, 4, 5])
print(arr2)

# 2d array :
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr3)

# 3d array :
arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr4)

# higher dimension array : 
arr5 = np.array([1, 2, 3, 4], ndmin=5)
print(arr5)
print('number of dimensions :', arr5.ndim)


# check dimension :
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)