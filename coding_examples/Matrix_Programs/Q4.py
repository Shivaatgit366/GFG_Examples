# adding and subtracting matrices in python.
"""
Suppose we have two matrices A and B.
A = [[1,2],
     [3,4]]

B = [[4,5],
     [6,7]]

then we get
A+B = [[5,7],[9,11]]
A-B = [[-3,-3],[-3,-3]]
"""

# solution:-
# method1:- normal method.

A = [[1, 2],
     [3, 4]]

B = [[4, 5],
     [6, 7]]

# for subtraction, I am keeping a list with initial values as 1. These values will be replaced by later.
#
# C = [[1, 1],
#      [1, 1]]
#

# def addition_matrix(a, b):
#     fin_list = []
#     for m in range(len(a)):
#         rows = []
#         for n in range(len(a[m])):
#             sum = a[m][n] + b[m][n]
#             rows.append(sum)
#         fin_list.append(rows)
#     return fin_list
#
#
# def subtraction_matrix(a, b):
#     for m in range(len(a)):
#         for n in range(len(a[m])):
#             C[m][n] = a[m][n] - b[m][n]
#     return C
#
#
# print(addition_matrix(A, B))
# print(subtraction_matrix(A, B))
# ------------------------------------------------------------------------------------------------------------

# method2:- using numpy module. Inbuilt add() and subtract() methods.
# import numpy as np

# subtraction_result = np.subtract(A, B)
# print(subtraction_result)

# addition_result = np.add(A, B)
# print(addition_result)
# -------------------------------------------------------------------------------------------------------------