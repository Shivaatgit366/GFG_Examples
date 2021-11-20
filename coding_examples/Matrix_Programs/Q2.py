# program to multiply two matrices.
# solution:-

# method1:- nested loop.

# Input :-

"""
x = [[1, 7, 3],
     [3, 5, 6],
     [6, 8, 9]]

y = [[1, 1, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]
"""


"""
Output : [55, 65, 49, 5]
         [57, 68, 72, 12]
         [90, 107, 111, 21]
"""

# final_list = []
# for i in range(len(x)):  # iterating by row of x  -->  0,1,2
#     temp_list = []
#     for j in range(len(y[i])):  # iterating by column of y  -->  0,1,2,3
#         answer = 0
#         for k in range(len(y)):  # iterating by row of y  -->  0,1,2
#             answer = answer + x[i][k] * y[k][j]
#         temp_list.append(answer)
#     final_list.append(temp_list)

# print(final_list)
# ------------------------------------------------------------------------------------------------------------------

# method2:- using numpy module.
# import numpy as np
# make a result matrix with values full of 0. Values will be replaced later.

# result = [[0, 0, 0, 0],
#           [0, 0, 0, 0],
#           [0, 0, 0, 0]]

# result = np.dot(x, y)
# print(result)  # the required matrix is obtained.
# -----------------------------------------------------------------------------------------------------------------