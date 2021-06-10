import numpy as np

# Create a 10x10 array with random values and find the minimum and maximum values
ten_by_ten_array = np.random.random((10,10))
min, max = ten_by_ten_array.min(), ten_by_ten_array.max()
print(min, max)

# Create a random vector of size 30 and find the mean value

size_30 = np.random.random(30)
mean_of_size = size_30.mean()
print (mean_of_size)

# Create a 2d array with 1 on the border and 0 inside

D_2 = np.ones((10,10))
D_2[1:-1,1:-1]=0
print(D_2)

a = np.zeros([1,2])
print(a)