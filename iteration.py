import numpy as np

# number of dimentions are equal to number of loops used to iterate each element.

# 1-d array
# np1 = np.array([1,2,3,4,5,6])
# for i in np1:
#     print(i)

# 2-d array
# np1 = np.array([[1,2,3,4,5,6], [7,8,9,10,11,12]])
# for i in np1:
#     for j in i:
#         print(j)

# 3-d array
np1 = np.array([[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]])
# for i in np1:
#     for j in i:
#         for k in j:
#             print(k)


# Use np.nditer() for iterate through n-dim of arr
for i in np.nditer(np1):
    print(i)
