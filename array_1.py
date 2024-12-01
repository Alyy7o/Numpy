import numpy as np

l = []
for i in range( 1,3):
    a = int(input("Enter a number: "))
    l.append(a)

a = np.array(l)
print(a)