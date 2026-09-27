import numpy as np

a = np.array([1,2])
b = np.array([2,3])

new_arr = np.concatenate((a,b))
print(new_arr)

# vertical stack

arr = np.array([[1,2], [3,4]]) 
arr2 = np.array([[6,7], [8,9]])

new_arr = np.vstack((arr, arr2))
print(new_arr)

# horizontal stack

new_arr = np.hstack((arr,arr2))
print(new_arr)