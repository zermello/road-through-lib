import numpy as np

# vectorization
# np.vectorize()


arr = np.array([1,2,3,4,5])

def func(x):
    i = np.square(x)
    return i

vfunc = np.vectorize(func)
vfunc(arr)