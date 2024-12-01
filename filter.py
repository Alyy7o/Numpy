import numpy as np

np1 = np.array([1,2,3,4,5,6,7,8])

# filtered = []
# for things in np1:
#     if things % 2 == 0:
#         filtered.append(True)
#     else:
#         filtered.append(False)

# print(np1)
# print(filtered)
# print(np1[filtered])


# Shoutcut!
filtered = np1 % 2 == 0
print(np1)
print(filtered)
print(np1[filtered])
    