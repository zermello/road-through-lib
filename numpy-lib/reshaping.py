import numpy as np

arr = np.array([1,2,3,4,5,6])
reshape  = arr.reshape(2,3)
print(reshape)

new_arr = np.ravel(reshape)
print(new_arr)

another_arr = reshape.flatten()
print(another_arr)

print(reshape)

new_arr[0] = 100
print(new_arr)
print(reshape)

another_arr[0] = 100
print(another_arr)
another_arr[0] = 1
print(reshape)

