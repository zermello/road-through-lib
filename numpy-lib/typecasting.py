import numpy as np

arr = np.array([1,2,3,4])
arr.dtype

new_arr = arr.astype(np.float64)
print(new_arr)

sec_arr = arr.astype(np.int64)
print(sec_arr)
sec_arr.dtype