import numpy as np

arr = np.array([1.1, 2.1, 3.1])
# newarr = arr.astype('i')
# newarr = arr.astype(bool)
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)