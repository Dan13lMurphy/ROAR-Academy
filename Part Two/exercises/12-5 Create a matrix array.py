import numpy as np
sample = [1, 2, 3, 4, 5, 6]


def set_array(L, rows, cols, order='C'):

    if len(L) != rows * cols:
        raise ValueError("Length of list L must equal rows * cols")

    return np.array(L).reshape((rows, cols), order=order)


print(set_array(sample, 3, 2))
