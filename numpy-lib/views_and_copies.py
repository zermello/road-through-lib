import numpy as np

arr = np.array([1,2,3,4,5,6])
view = arr[0:3]

view[0] = 100
print(arr)
print(view)

new_arr = view.copy()
new_arr[0] = 10

print(view)
print(new_arr)