import numpy as np


# okay numpy is great:
a = np.array([[3,1,2], [-5,4,1], [0,3,-8]])

def inverse_matrix(A):
    mat_inv = np.linalg.inv(A)
    print(mat_inv)

b = np.array([[1., 2.], [3., 4.]])
inverse_matrix(b)


# Just answer using code --> easy stuff!

A = np.array([[3, 0.6, 4, -3],[-1.3,4,0,8.6],[7,0,-8,0.006]])
B = np.array([[3, -5.76, 45, 0],[2, -2, 1.3 , 9],[-9, 0,0,0]])
C = np.array([[0,1009, -66.7849, 90],[0,5,4,-0.07],[-7.7,0,0,0]])


D = A + B - C
print(D[1][2])


AA = np.array([0.6,-15,2,5,98])
BB = np.array([[2,2,-4],[9,-14,0],[13,-0.5,44],[1,9,4],[0,0,5]])

CC = np.dot(AA.T, BB)
print(CC)