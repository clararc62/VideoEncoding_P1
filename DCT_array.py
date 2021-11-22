#EXERCISE 5 ARRAY

import numpy
from scipy.fftpack import dct, idct

#ask for the array to the user, first the length and then the elements
my_array = []
a = int(input("Size of array:"))
for i in range(a):
    my_array. append(float(input("Element:")))
my_array = numpy. array(my_array)


def DCT(array):
    return(dct(array, 1))

def IDCT(array):
    return(idct(array,1)/6)

print("The original array is: ", my_array)

h=DCT(my_array)
print("The DCT is", h)

n=IDCT(h)
print("The IDCT is", n)



