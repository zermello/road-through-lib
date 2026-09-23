import time
import numpy as np

a = [1,2,3,4,5,6,7] * 10000

start = time.time()
for i in range(len(a)):
    a[i] = a[i] * 2
print(time.time() - start)

b = np.array(a)
start2 = time.time()
new_b = b*2
print(time.time() - start2)