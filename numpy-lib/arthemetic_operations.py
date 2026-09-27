import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

list = [a+b]
print(a+b)
print(list)

print(a-b)
print(a/b)
print(a*b)

print(b//a)
print(b%a)

print(a**b)

a = np.sqrt(a)
b = np.sqrt(b)

print((np.sqrt(100)))
print(a+b)

#exponential

print(np.exp(a[0:2]))

angles = np.array([0, np.pi, np.pi/2])
print(np.sin(angles))