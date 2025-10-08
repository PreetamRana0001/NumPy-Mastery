'''
np.isert(array,index, value,asix=none)
array = original array
index -
value -
axis = 0,row-wise
1 column wise

'''

import numpy as np

arr = np.array([10,20,30,40,50,60,70])
print(arr)
new_arr = np.insert(arr , 2 , 100)
print(new_arr)