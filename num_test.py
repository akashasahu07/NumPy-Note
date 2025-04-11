# Iteration Using Python's Loop

import numpy as np
# 1-D Array
# a = np.arange(10, 51, 10)
# for x in a:
#     print(x)

# 2-D Array
# a = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
# # print(a)
# for x in a: # x is 1-D array but not scalar value
#     # print(x)
#     for y in x: # y is a scalar value present in 1-D array
#         print(y)

# 3-D Array
# a = np.array([[[10, 20], [30, 40]], [[50, 60], [70, 80]]])
# # print(a)
# for x in a: # x is 2-D Array but not scalar value
#     # print(x)
#     for y in x: # y is 1-D Array but not scalar value
#         # print(y)
#         for z in y: # z is a scalar value
#             print(z)

# nditer

# 1-D Array
# a = np.arange(10, 51, 10)
# for x in np.nditer(a):
#     print(x)

# 2-D Array
# a = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
# for x in np.nditer(a):
#     print(x)

# 3-D Array
# a = np.array([[[10, 20], [30, 40]], [[50, 60], [70, 80]]])
# for x in np.nditer(a):
#     print(x)

# Sliced Value
# a = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
# print(a[:,:2])
# for x in np.nditer(a, flags=['buffered'], op_dtypes=['float']): # As required data type
# for x in np.nditer(a[:, :2]): # It is normal type
    # print(x) 


# By using ndenumerate() function:

# 1-D Array
# a = np.array([10, 20, 30, 40, 50])
# for pos, element in np.ndenumerate(a):
#     print(f'{element} element present at index/position: {pos}')

# 2-D Array
# a = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
# for pos, element in np.ndenumerate(a):
#     print(f'{element} element present at index/position: {pos}')

# 3-D Array
# a = np.arange(1, 25).reshape(2, 3,4)
# for pos, element in np.ndenumerate(a):
#     print(f'{element} element present at index/position: {pos}')

# Operators

# Arithmatic Operator

# 1-D Array
# a = np.array([10, 20, 30, 40])
# print(a + 2)
# print(a - 2)
# print(a * 2)
# print(a / 2)
# print(a % 2)
# print(a // 2)

# 2-D Array
# a = np.array([[10, 20, 30], [40, 50, 60]])
# print(a + 2)
# print(a - 2)
# print(a * 2)
# print(a / 2)
# print(a % 2)
# print(a // 2)

# NumPy ZeroDivisionError 
# >>> import numpy as np
# >>> a = np.arange(6)
# >>> a
# array([0, 1, 2, 3, 4, 5])
# >>> a/0
# array([nan, inf, inf, inf, inf, inf])

# >>> a = np.array([10, 20, 30, 40])
# >>> b = np.array([1, 2, 3, 4])
# >>> a.ndim
# 1
# >>> b.ndim
# 1
# >>> a.shape
# (4,)
# >>> b.shape
# (4,)
# >>> a.size
# 4
# >>> b.size
# 4
# >>> b + a
# array([11, 22, 33, 44])
# >>> b - a
# array([ -9, -18, -27, -36])
# >>> a + b
# array([11, 22, 33, 44])
# >>> a - b
# array([ 9, 18, 27, 36])
# >>> a * b
# array([ 10,  40,  90, 160])
# >>> a / b
# array([10., 10., 10., 10.])
# >>> a // b
# array([10, 10, 10, 10])