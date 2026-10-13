import numpy as np 
a=np.array([[1,2,3]])
a

import numpy as np
b=np.array([[1,2,3],[1.2,3,5,]])
b

import numpy as np
b=np.array([[1,2,3],[1.2,3,5,],[4,5,6]])
b

import numpy as np
np.zeros([1,1,2,5,9])

a = np.zeros([1, 2, 3, 1, 4])

print(a.shape)
print(a.ndim)
print(a.size)

e=np.full((1,1),7)
e

import numpy as np
a = np.arange(10,50,5)
a

import numpy as np
a = np.eye(4)
a

import numpy as np

a = np.random.randint(1, 9)

print(a)

import numpy as np
a = np.empty((2,3))
a

import numpy as np

a = np.array([10, 20, 30, 40, 50])

print(a)

import numpy as np

a = np.arange(1, 11)

print(a)

import numpy as np

a = np.array([15, 8, 25, 10, 30])

print("Maximum:", np.max(a))
print("Minimum:", np.min(a))

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = a + b

print(c)

import numpy as np

a = np.array([1, 2, 3, 4])
print(a)

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)

import numpy as np

import numpy as np

a = np.array([1, 2])
b = np.array([3, 4])
print(a + b)
a = np.zeros(3)
print(a)

import numpy as np

a = np.array([10, 25, 5, 30])
print(a.max())

import numpy as np

a = np.array([1, 2, 3, 4])
print(a)

import numpy as np

a = np.zeros(3)
print(a)

import numpy as np

a = np.ones(3)
print(a)

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr)

import numpy as np

arr = np.array([10, 20, 30, 40])

print(np.sum(arr))

import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr)

import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr)

import numpy as np

arr = np.arange(1, 11)

print(arr)

import numpy as np

a = np.array([10, 20, 30, 40])
print(np.mean(a))

import numpy as np

a = np.array([5, 10, 15])
print(np.sum(a))

import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
print(a.reshape(2, 3))

import numpy as np

a = np.ones((2, 3))
print(a)

import numpy as np
a = np.zeros((2,3)) #creates a 2D array filled with zeros
print(a)

import numpy as np
a = np.eye(4) #creates a 2D array with ones on the diagonal and zeros elsewhere
print(a)

import numpy as np
a = np.arange(1,10,2) #srtart, stop, step
print(a)

import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a.shape) #number of rows and columns
print(a.size) #total number of elements
print(a.ndim) #number of dimensions or 2D array

#Division
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
div = arr1 / arr2
print(div)  

#Multiplication
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
mul = arr1 * arr2
print(mul)

#Subtraction
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
sub = arr1 - arr2
print(sub)

#Addition
import numpy as np
arr1 = [1,2,3]
arr2 = [4,5,6]
sum = arr1 + arr2
print(sum)

import numpy as np
a = np.array([[1,2,3],[4,5,6]])
b = a.astype(int) #convert the data type of the array elements to int
print(b)

import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a.astype(float)) #convert the data type of the array elements to float

import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a.dtype) #data type of the array elements

import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(len(a)) #number of rows

import numpy as np
a = np.empty((2,3)) #2 rows and 3 column
print(a)

arr = [10, 20, 30, 40, 50]

print(arr[0])
