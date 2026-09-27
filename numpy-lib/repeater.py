import numpy as np

arr = np.array([1,2,3])

#repeat per element
new_arr = np.repeat(arr, 10)
print(new_arr)

# repeat completely
other_arr = np.tile(arr, 3)
print(other_arr)