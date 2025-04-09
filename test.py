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