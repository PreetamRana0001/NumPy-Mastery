# list = [1,2,3]
# list2 = [4,5,6]
# result = [x+y for x,y in zip(list,list2)]
# print(result)

import numpy as np 
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
result = arr1 + arr2
print(result)


arr = np.array([10,20,30,40])
multi = arr + 3
print(multi)