import numpy as np


def plane(a, b, c):
    # returns false if the vectors do define a plane and returns which are those vectors if true

    matrix = np.stack((a, b, c))

    lambdas, V = np.linalg.eig(matrix.T)

    e = 0.000000001

    plane_test = abs(lambdas) > e

    if plane_test.sum() >= 2:

        print('Vectors form a plane!')

        vectors = matrix[plane_test]
        print(vectors)
    else:
        print('Vectors are all linearly dependent. No plane exists.')

a = np.array([1,2,3])
b = np.array([2,2,2])
c = np.array([8,8,8])

plane(a,b,c)


# Harder exercise

def complete_plane(*args):
    # returns the first set of vectors to complete a plane, false otherwise

    np_arrays = []

    for arg in args:
        np_arrays.append(arg)

    matrix = np.stack(np_arrays)

    rows = matrix.shape[0]
    columns = matrix.shape[1]

    if rows == columns:

        lambdas, V = np.linalg.eig(matrix.T)

        e = 0.000000001
        plane_test = abs(lambdas) > e

        if plane_test.sum() >= 2:
            print('True')

            index = np.argwhere(plane_test == True)

            vectors = matrix[index]
            print(vectors)
        else:
            print('False')




    elif rows != columns:

        U, eigvals, d = np.linalg.svd(matrix.T)

        e = 0.000000001
        plane_test = abs(eigvals) > e

        if plane_test.sum() >= 2:
            print('True')

            index = np.argwhere(plane_test == True)

            vectors = matrix[index][:2]

            return vectors

        else:
            print('False')
a = np.array([1,2,3])
b = np.array([2,4,6])
c = np.array([3,2,1])
d = np.array([6,4,2])
e = np.array([1,5,8])

complete_plane(a,c,d,e)