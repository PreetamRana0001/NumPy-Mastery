import  numpy as np

arr_2d = np.array([[4,5,6],[7,8,5]])
print(arr_2d)
new_arr_2d= np.insert(arr_2d , 1, [5,6,8], axis = 0)
print(new_arr_2d)