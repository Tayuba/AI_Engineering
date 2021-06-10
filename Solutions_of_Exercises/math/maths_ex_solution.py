import numpy as np
from numpy.polynomial import polynomial as P

# Polynomial derivatives
fun1 = np.poly1d([1, 2, 1])
der_fun1 = np.polyder(fun1)
print(der_fun1)

fun2 = np.poly1d([1/2, -5, 1])
der_fun2 = np.polyder(fun2)
print(der_fun2)

fun3 = np.poly1d([1])
der_fun3 = np.polyder(fun3)
print(der_fun3)

fun4 = np.poly1d([6/4, -9/7, 0,0,2,0,0])
der_fun4 = np.polyder(fun4)
print(der_fun4)

fun5= np.poly1d([1/2,-1, 0,1])
der_fun5 = np.polyder(fun5)
print(der_fun5)

