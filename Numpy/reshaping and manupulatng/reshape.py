'''
rehsaape(rows , column) specify new shape
if dimension match
'''

import numpy as np

arr = np.array([1,2,3,4,5,5])
reshaped_arr = arr.reshape(2,3)
print(reshaped_arr)