import numpy as np

np1 = np.array([1,2,3,4,5,6,7])
print(np1)
# print(np.where(np1 == 3))
# For even no
print(np.where(np1 % 2 == 0)) # return index
print(np1[np.where(np1 % 2 == 0)]) # return values

# For odd no
print(np.where(np1 % 2 == 1)) # return index
print(np1[np.where(np1 % 2 == 1)]) # return values