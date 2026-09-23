
import numpy as np

list = [1,2.44,3,4]
list = np.array(list, dtype=int)

list.dtype

list = [1,2.55,3,4]
list = np.array(list, dtype=np.int64)
print(list)