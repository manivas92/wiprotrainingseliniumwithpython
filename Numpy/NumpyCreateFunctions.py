'''
    Using numpy.array() Function
    Using numpy.zeros() Function
    Using numpy.ones() Function
    Using numpy.arange() Function
    Using numpy.linspace() Function
    Using numpy.random.rand() Function
    Using numpy.empty() Function
    Using numpy.full() Function
'''

import numpy as np
from numpy.ma.core import identity

a = np.zeros(5)
print(a)

a = np.ones(5)
print(a)

#2D array of ones
a_2D = np.ones((5,3))
print(a_2D)

#stop
a =np.arange(10)
print(a)

#start , stop
a = np.arange(1,10,3)
print(a)

#linespace
a = np.linspace(0,10,5,endpoint=False)
print(a)

a = np.linspace(0,10,5,endpoint=True)
print(a)

a = np.random.rand(5)
print(a)

a = np.random.rand(5,6)
print(a)

a = np.random.rand(5,4,6)
print(a)

a = np.empty((2,3,))
print(a)

a = np.full((2,3),5)
print(a)

identity_matrix = np.eye((4))
print(identity_matrix)

identity_matrix = np.identity((3))
print(identity_matrix)

matrix = np.array([[10,20,30],[40,50,60],[70,80,90]])
print("Orginal matrix",matrix)
Diagonal_elements = np.diag(matrix)
print("Diagonal elements", Diagonal_elements)


