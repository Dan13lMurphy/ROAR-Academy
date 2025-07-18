import numpy as np

v = np.array([2., 2., 4.])

e0 = np.array([1, 0, 0])
e1 = np.array([0, 1, 0])
e2 = np.array([0, 0, 1])

print(np.dot(v, e0))
print(np.dot(v, e1))
print(np.dot(v, e2))
