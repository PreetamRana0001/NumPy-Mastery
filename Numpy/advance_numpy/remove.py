'''
np.delete(array,  indexing, axis = none)

'''

import numpy as np

arr = np.array([10,20,30,4,50,60])
print(arr)
new_arr = np.delete(arr,5)
print(new_arr)