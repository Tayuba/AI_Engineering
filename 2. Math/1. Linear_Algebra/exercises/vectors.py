import numpy as np

# Write a function add_vectors(u, v) that takes two lists of numbers of the same length, and returns
# a new list containing the sums of the corresponding elements of each
def add_vectors(u, v):
    additions = np.add(u, v)
    print(additions)


add_vectors([1, 2], [1, 1])


# Write a function scalar_mult(s, v) that takes a number, s, and a list, v and returns the scalar multiple of v by s
def scalar_mult(s, v):
    s_multipy = np.multiply(s,v)
    print(s_multipy)


scalar_mult(3, [1, 0, -1])


# Write a function dot_product(u, v) that takes two lists of numbers of the same length,
# and returns the sum of the products of the corresponding elements of each (the dot_product.
def dot_product(u, v):
    dot_s = np.dot(u,v)
    print(dot_s)


dot_product([2, 0, -1, 1], [1, 5, 2, 0])


# Create a new module named matrices.py or use the Jupyter notebook provided and add the following function,
# which returns a copy of nested lists of numbers such that the lists are not aliases:
def copy_matrix(matrix):
    original_matrix = np.array(matrix, order='F')
    copy_matrix = original_matrix.copy()
    print(copy_matrix)


copy_matrix([[1, 2], [3, 4]])
print("\n")


def add_row(matrix):
    add_new_row = np.r_[matrix,[[np.multiply(0,i) for i in range(len(np.column_stack(matrix)))]]]
    print(add_new_row)


m = [[3, 2, 5], [1, 4, 7]]
add_row(m)
print("\n")


def add_column(matrix):
    add_new_column = np.c_[matrix, [np.multiply(0,i) for i in range(len(matrix))]]
    print(add_new_column)


m = [[3, 2], [5, 1], [4, 7]]
add_column(m)
print("\n")

# Write a function add_matrices(m1, m2) that adds m1 and m2 and returns a new matrix containing their sum.
# You can assume that m1 and m2 are the same size. You add two matrices by adding their corresponding values.
def add_matrices(m1, m2):
    additions = [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m2))]
    print(additions)


a = [[8, 2], [3, 4], [5, 7]]
b = [[3, 2], [9, 2], [10, 12]]

add_matrices(a, b)
print("\n")

# Write a function scalar_mult(s, m) that multiplies a matrix, m, by a scalar, s.
def scalar_mult(s, m):
    s_matrix = np.multiply(s,m)
    print(s_matrix)


a = [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
scalar_mult(10, a)
print("\n")

# Write functions row_times_column and matrix_mult:
def row_times_column(m1, row, m2, column):
    multy_matrix = np.matmul(m1, m2)
    r_c_m = multy_matrix[row][column]
    print(r_c_m)


row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 0)
print("\n")

def matrix_mult(m1, m2):
   matrix_r_c = np.matmul(m1, m2)
   print(matrix_r_c)


matrix_mult([[1, 2], [3,  4]], [[5, 6], [7, 8]])

# Write a function transpose that takes a matrix as an argument and returns is transpose
def transpose(m):
   trans_matrix = np.transpose(m)
   print(trans_matrix)

m = [[3, 4, 6], [1, 5, 9]]
transpose(m)