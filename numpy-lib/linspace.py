import numpy as np

list = np.linspace(1,11, 5)
print(list)

another_list = np.arange(0,10)
print(another_list)

np.logspace(1,2,10)
arr = np.zeros(100)
print(arr)

arr2 = np.zeros([2,3], dtype=int)
print(arr2)

tets = np.array([[1,2], [1,3]])
print(tets)

arr = np.ones([2,2], dtype=int)

sm=[]
for i in arr:
    i = i*2
    sm.append(i)
print(sum(i))

test = np.full([3,3], 7)

arr = np.empty([1,1])

rand = np.random.randint(2,3)
rand

randome = np.random.randint(1,10, size=(2,3))