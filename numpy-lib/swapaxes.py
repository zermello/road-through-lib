import numpy as np

arr = np.array([[1,2,3], [1,3,3]])
# print(arr)
# arr.shape
# arr.size
# arr.ndim

new_arr = arr.swapaxes(0, 1)
print(new_arr)
print(new_arr.shape)