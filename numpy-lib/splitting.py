import numpy as np

arr = np.array([[1,2], [3,4]])
arr2 = np.array([[4,5],[6,8]])

new_arr = np.concatenate((arr, arr2))
print(new_arr)

print(np.vstack((arr,arr2)))
print(np.hstack((arr,arr2)))

split = np.split(new_arr, 4)
print(split)
print(np.hsplit(new_arr, 2))
print(np.vsplit(new_arr, 4))

split = np.array_split(new_arr, 3)
print(split)

