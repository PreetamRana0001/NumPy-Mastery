'''
np.split()
equal
np.hsplit()
np.vsplit()
'''
import numpy as np

arr = np.array([1,2,3,45,4,5])
print(np.split(arr , 2))
print(np.hsplit(arr , 2))
arr_2d = arr.reshape(2,3)
print(arr_2d)
print(np.vsplit(arr_2d,2 ))