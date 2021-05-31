import numpy as np
import time

# How to get all the dates corresponding to the month of July 2016?
print(np.arange('2016-07', '2016-08', dtype='datetime64[D]'))

# How to compute ((A+B)*(-A/2)) in place (without copy)?
A = np.ones(3) * 1
B = np.ones(3) * 2
np.add(A, B, out=B)
np.divide(A, 2, out=A)
np.negative(A, out=A)
print(np.multiply(A, B, out=A))
print("\n")

#Extract the integer part of a random array using 5 different methods
int_of_five = np.random.uniform(5,-5,5)
print(int_of_five.astype(np.int64))
print(np.trunc(int_of_five))
print(np.ceil(int_of_five))
print("\n")

#Create a 5x5 matrix with row values ranging from 0 to 4
five_by_five = np.zeros((5, 5))
five_by_five += np.arange(5)
print(five_by_five)
print("\n")

# Consider a generator function that generates 10 integers and use it to build an array
def func_generator():
    for x in range(10):
        yield x

array_func = np.fromiter(func_generator(), dtype=float, count=-1)
print(array_func)
print("\n")

# Create a vector of size 10 with values ranging from 0 to 1, both excluded
exluded_0_1 = np.linspace(0, 1, 12, endpoint=True)[1:-1]
print(exluded_0_1)
print("\n")

# Create a random vector of size 10 and sort it
sorted_rand = np.random.random(10)
sorted_rand.sort()
print(sorted_rand)
print("\n")

# How to sum a small array faster than np.sum?
# Not recommended for small data
# L = [1,2,3,4,5]
# start_time1 = time.time()
# x = np.arange(L)
# np.sum(x)
# finish_time1 = time.time()
# print((finish_time1 - start_time1))
#
# # Fast method for small data
# start_time2 = time.time()
# for x in [1,2,3,4,5]:
#     x += x
# finish_time2 = time.time()
# print(finish_time2 - start_time2)
# print("\n")

# Consider two random array A and B, check if they are equal
# Note this code only runs if the code for checking fast method is commented out
A = np.random.randint(0, 2, 5)
print(A)
B = np.random.randint(0, 2, 5)
print(B)
equal_or_not = np.allclose(A, B)
# equal_or_not = np.allclose(A, B)
print(equal_or_not)