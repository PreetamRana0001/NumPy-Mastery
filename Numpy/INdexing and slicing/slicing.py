'''
slicing
array = (start:stop:step)
'''
import numpy as np
arr = np.array([1,2,3,4,5,67,8,8,9,0,6,3,2,34,5,6,6])
print(arr[1:19:2]) 
print(arr[1::2])
print(arr[1::-1])