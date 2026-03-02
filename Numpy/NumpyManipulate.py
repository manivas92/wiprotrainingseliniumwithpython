import numpy as np
from numpy.ma.core import transpose

#reshape
a = np.arange(1,7)
print("Original array",a)
#reshape the array
reshaped = a.reshape(2,3)
print(reshaped)

#flat
arr = np.array([[1,2],[3,4]])
for x in arr.flat:
    print(x)

#flatten
arr = np.array([[1,2],[3,4]])
print(arr)
at_arr = arr.flatten()
print(at_arr)

#ravel()
arr = np.array([[1,2],[3,4]])
print(arr)
at_arr = arr.ravel()
print(at_arr)

#pad
arr = np.array([1,2,3])
padded = np.pad(arr, 3,mode ='constant')
print(padded)

''' Transpose operations
1   transpose
Permutes the dimensions of an array
2   ndarray.T
 as self.transpose()
3   rollaxis
Rolls the specified axis backwards
4   swapaxes
Interchanges the two axes of an array
5   moveaxis()
Move axes of an array to new positions
'''

#1  transpose
# reorders the dimensions of an array.
# rows will become the columns

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.transpose()
print(transpose)

#2 ndarray.T
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.T
print(transpose)

#rollaxis - Rolls the specified axis backwards

arr = np.zeros((2,3,4))
print(arr)

# 2 is the blocks - axis 0
# 3 - rows - axis 1
# 4 columns - axis 2

#(0,1 ,2) - (2,3,4)
#(2,0,1) - (4,2,3)

#arr[block][row][column]

new_arr = np.rollaxis(arr, 2)
print(new_arr)

#swapaxes() - Interchanges two axes of an array.
#$Axis 0 and Axis 2 swapped.
arr = np.zeros((2,3,4))
print(arr)

new_arr = np.swapaxes(arr, 0 , 2)
print(new_arr)
# (4 3, 2)

#moveaxis() - Moves specified axes to new positions.
arr = np.zeros((2,3,4))
print(arr)
new_arr = np.moveaxis(arr, 0, -1)
print(new_arr)

#joining arrays
#concatenate

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(np.concatenate((a,b),axis = 0))
print(np.concatenate((a,b),axis = 1))

#stack - join the arrays along the new axis

a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.stack((a,b),axis = 0))
print(np.stack((a,b),axis = 1))

#hstack
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(np.hstack((a,b)))
print(np.concatenate((a,b),axis=1))

#vstack
print(np.vstack((a,b)))
print(np.concatenate((a,b),axis=0))

#column stack()
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.column_stack((a,b)))
print(np.vstack((a,b)))

#splitting Arrays

arr = np.array([1,2,3,4,5,6])

result = np.split(arr, 3)
print(result)

import numpy as np

# hsplit() - Splits array horizontally (column-wise)
# Works on 2D arrays.

arr2 = np.array([[1,2,3,4],
                 [5,6,7,8]])

print(np.hsplit(arr2, indices_or_sections=2))


# vsplit() Splits array vertically (row-wise)

arr2 = np.array([[1,2],
                 [3,4],
                 [5,6],
                 [7,8]])

print(np.vsplit(arr2, indices_or_sections=2))

arr = np.array([1,2,3,4,5])
print(np.array_split(arr, 3))

arr = np.array([1,2,3,4])
new_arr = np.resize(arr, (2,3))
print(new_arr)

# Adding / Removing Elements

# resize() - Returns a new array with a specified shape.
arr = np.array([1,2,3,4])
new_arr = np.resize(arr, new_shape=(2,3))
print(new_arr)

# the elements will repeat in the new array
# returns a new array

# append() - Appends values at the end of an array.
arr = np.array([1,2,3])
new_arr = np.append(arr, values=[4,5])
print(new_arr)

# 2D array
a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])
np.append(a, b, axis=0)

# Inserts values before given index.
arr = np.array([10,20,30])
new_arr = np.insert(arr, obj=2, values=15)
print(new_arr)

# Deletes elements along a specified axis.
arr = np.array([10,20,30])
new_arr = np.delete(arr, obj=2)
print(new_arr)

# unique()
arr = np.array([1,2,2,3,4,4,5])
print(np.unique(arr))

# Repeating
# repeat() is used to repeat each element of an array a specified number of times.
# Each element is repeated three times.
arr = np.array([1, 2, 3])
print(np.repeat(arr, repeats=3))

# Different Repeats for Each Element
arr = np.array([10, 20, 30])
print(np.repeat(arr, repeats=[1, 2, 3]))

# Repeat in 2D Array
arr2 = np.array([[1, 2],
                 [3, 4]])

print(np.repeat(arr2, repeats=2, axis=0))

my_array = np.array([1, 2, 3])
tiled_array = np.tile(my_array,2)
print("Original Array:", my_array)
print("Tiled Array:", tiled_array)

import numpy as np

# 1D array flip
arr = np.array([1, 2, 3, 4])
print("Original 1D array:", arr)
print("Flipped 1D array:", np.flip(arr))

# 2D array flip (rows and columns)
arr2 = np.array([[1, 2],
                 [3, 4]])

print("\nOriginal 2D array:\n", arr2)

# Flip rows (up-down)
print("\nFlip rows (axis=0):\n", np.flip(arr2, axis=0))

# Flip columns (left-right)
print("\nFlip columns (axis=1):\n", np.flip(arr2, axis=1))


# fliplr() – Flip left-right (only for 2D or higher)
arr3 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("\nOriginal array for fliplr:\n", arr3)
print("\nfliplr result:\n", np.fliplr(arr3))

# flipud() – Flip up-down
print("\nflipud result:\n", np.flipud(arr3))

# roll() – Rotate elements
print("\nOriginal array for roll:\n", arr3)

# Roll all elements by 2 positions
print("\nRoll with shift=2:\n", np.roll(arr3, shift=2))

# Roll along axis=0 (rows)
print("\nRoll along rows (axis=0):\n", np.roll(arr3, shift=1, axis=0))

# Roll along axis=1 (columns)
print("\nRoll along columns (axis=1):\n", np.roll(arr3, shift=1, axis=1))

#sorting and searching
#sort
arr = np.array([5,2,9,1])
sorted_arr = np.sort(arr)
print(sorted_arr)

#argsort
arr = np.array([5,2,9,1])
sorted_arr = np.sort(arr)
print(sorted_arr)
indices = np.argsort(arr)
print(indices)

# lexsort() – Used for sorting with multiple columns
# Sort by 'a' first
# Then by 'b' (secondary key)

a = np.array([1, 1, 0, 0])
b = np.array([1, 0, 1, 0])

result = np.lexsort((b, a))
print(result)