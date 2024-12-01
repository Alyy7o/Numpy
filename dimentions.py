import numpy as np 

a = np.array([1,2,3,4,5,6])
print(a.ndim)
print(a.shape)
print(a.reshape(3,2,1))
print(a.reshape(-1))
print(a)
print(a.ndim)

b = np.array([[1,2,3,4,5],
              [6,7,8,9,10]])
print(b.ndim)
print(b.shape)

c = np.array([[[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]]])
print(c.ndim)
print(c.shape)


