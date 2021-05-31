import numpy as np

# How to swap two rows of an array?
To_swap = np.arange(81).reshape(9, 9)
To_swap[[0, 1]] = To_swap[[1, 0]]
print(To_swap)

# Consider a set of 10 triplets describing 10 triangles (with shared vertices),
# find the set of unique line segments composing all the triangles
face_side = np.random.randint(0, 100, (10, 3))
turn_F = np.roll(face_side.repeat(2, axis=1), -1, axis=1)
turn_F = turn_F.reshape(len(turn_F) * 3, 2)
turn_F = np.sort(turn_F, axis=1)
View_tr = turn_F.view(dtype=[('p0', turn_F.dtype), ('p1', turn_F.dtype)])
View_tr = np.unique(View_tr)
print(View_tr)
print("\n")


# Given an array C that is a bincount, how to produce an array A such that np.bincount(A) == C?
C = np.bincount([1,1,2,3,4,4,6,7,9,10,11,12,13,14,15])
A = np.repeat(np.arange(len(C)), C)
print(A)
print("\n")

# How to compute averages using a sliding window over an array?
def average_slice(num, int_1= 10):
    ret = np.cumsum(num, dtype=float)
    ret[int_1:] = ret[int_1:] - ret[:-int_1]
    return ret[int_1 - 1:] / int_1
range_to_use = np.arange(30)
print(average_slice(range_to_use, int_1=3))