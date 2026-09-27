import numpy as np

#multidimensional slicing

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [6,7,8]
])

print(matrix[::2])

print(matrix[1: , :2])

arr = np.array([1,2,3,4,5,6,7,8,9,0])
ind = [0,2]

print(np.take(arr, ind))

arr = np.array([[1,2,3], [4,5,6]])

for i in np.nditer(arr):
    print(i, end = " ")

for ind, i in np.ndenumerate(arr):
    print(ind, i)