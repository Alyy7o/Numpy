import numpy as np

#  range
arr = np.arange(10)

print(arr)

# step
arr = np.arange(0,10, 2)
print(arr)

# full
arr2 = np.full((10), 8)
print(arr2)

# covert python list to np
py_list = [1,2,5,3,7]
print(type(py_list))
py_arr = np.array(py_list)
print(type(py_arr))