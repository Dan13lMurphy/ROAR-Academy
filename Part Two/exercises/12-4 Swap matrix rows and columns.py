import numpy as np

sampleMatrix = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])


def swap_rows(M, a, b):
    M[[a, b], :] = M[[b, a], :]
    return M


def swap_cols(M, a, b):
    M[:, [a, b]] = M[:, [b, a]]
    return M


print(swap_rows(sampleMatrix, 1, 3))
print("\n")
print(swap_cols(sampleMatrix, 2, 4))
