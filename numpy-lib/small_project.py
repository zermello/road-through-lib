import numpy as np

# finding missing values

arr = np.array([1,2, np.nan , 4])
print(arr)

# np.inf and -np.inf -> postitive and negative infinites

if True in np.isnan(arr):
    print("yes")
else:
    print("no")

new_b = np.nan_to_num(arr)
print(new_b)