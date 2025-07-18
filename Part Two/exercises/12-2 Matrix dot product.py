import numpy as np

a = np.array([[6, -9, 1],
              [4, 24, 8]])

b = np.array([[1, 0],
              [0, 1]])

c = np.array([[4, 3],
              [3, 2]])

d = np.array([[-2, 3],
              [3, -4]])

print(2 * a)
print(b @ a)
print(c @ d)
