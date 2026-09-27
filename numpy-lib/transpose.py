import numpy as np

arr = np.array([[1,2,3], [4,5,6]])
print(arr)
print(f"{arr.ndim} , {arr.shape}")

new_arr = arr.transpose()
print(new_arr)
print(f"{new_arr.ndim}, {new_arr.shape}")