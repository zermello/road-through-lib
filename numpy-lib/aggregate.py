import numpy as np

arr = np.array([60,70,80,90])
arr2 = np.array([60,70,80,90])

sum= np.sum(arr)
print(sum)

arr = np.max(arr)
print(arr)
arr = np.min(arr)
print(arr)

arr = np.mean(arr)
print(arr)

arr = np.median(arr)
print(arr)

new_arr = np.sort(arr2, descending=True)
print(new_arr)

cumsum = np.cumulative_sum(arr2)
print(cumsum)

cumsum = np.cumsum(arr2)
print(cumsum)

print(np.cumprod(arr2))