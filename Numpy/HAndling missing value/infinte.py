# np.isinf() 10*1000
# 1/0
import numpy as np 
arr  = np. array ([1,12,np.inf,4,-np.inf,6])
print(np.isinf(arr))
cleaned_arr = np.nan_to_num(arr, posinf=1000, neginf=-1000)
print(cleaned_arr)