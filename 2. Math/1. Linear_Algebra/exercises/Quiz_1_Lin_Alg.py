import numpy as np

# type a function that given a 3_dimensional vector it is able to calculate its magnitude
def magnitude_3(a, b, c):
    vector = [a, b, c]
    mag_3D_vector = np.linalg.norm(vector)
    print(mag_3D_vector)


magnitude_3(8,7,5)


def magnitude_complete(*args):  # inputs
    X = []
    for arg in args:
        X.append(arg)
    n_dire = np.linalg.norm(X)
    print(n_dire)

magnitude_complete(1,2,3,4,5)

# checks that size is equal if x and y are equal

def magnitude_vectors(a, b):
    a_size = a.size
    b_size = b.size
    try:
        a_size == b_size
        a_b_sum = a + b
        equal_vector = np.linalg.norm(a_b_sum)
        print(equal_vector)
    except:
        print('Vectors are different dimensions {} and {}'.format(a_size, b_size))

a = np.array([5, 1])
b = np.array([-4,-1])
magnitude_vectors(a, b)


# checks that size is equal if x and y are equal and direction
def direction_vectors(a, b):
    a_size = a.size
    b_size = b.size
    try:
        a_size == b_size
        a_b_sum = a + b
        print(a_b_sum)
    except:
        print('Vectors are different dimensions {} and {}'.format(a_size, b_size))

a = np.array([5, 1])
b = np.array([-4,-1])
direction_vectors(a, b)

# returns the resulting magnitude, if the direction has changed and what has happened to the vector
def alpha_magnitude(alpha, b):
    b = np.array(b)
    vector = alpha * b
    if np.sign(b[0]) == np.sign(vector[0]):
        print('No directional change')
    else:
        print('The direction has changed 180 degrees')
    print(vector,  np.linalg.norm(vector))

alpha_magnitude(-8, [1,1])


