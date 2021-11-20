# write a program to get the transpose of a matrix (transpose means rows into columns and columns into rows).
# solution:-

# method1:- normal method
#
# m = [[1, 2],
#      [3, 4],
#      [5, 6]]
#
#
# def matrix_rows_count(matrix):
#     val = 0
#     for x in matrix:
#         val = val + 1
#     return val
#
#
# def matrix_column_count(matrix):
#     val = 0
#     for x in matrix[0]:
#         val = val + 1
#     return val
#
#
# def matrix_creator(m, n):  # m x n matrix with every value = 1.
#     output_list = []
#     for x in range(m):
#         list1 = []
#         for y in range(n):
#             value = 1
#             list1.append(value)
#         output_list.append(list1)
#     return output_list
#
#
# def transpose_matrix(matrics):
#     num_rows = matrix_rows_count(matrics)
#     num_column = matrix_column_count(matrics)
#     virtual_matrix = matrix_creator(num_column, num_rows)
#
#     for i in range(len(matrics)):
#         for j in range(len(matrics[i])):
#             virtual_matrix[j][i] = matrics[i][j]
#     return virtual_matrix


# print(transpose_matrix(m))
# -------------------------------------------------------------------------------------------------------------

# method2:- list comprehension.

"""
m = [[1, 2],
     [3, 4],
     [5, 6]]
"""

# for row in m:
#     print(row)
# print("\n")

# rez = [[m[row_val][column_val] for row_val in range(len(m))] for column_val in range(len(m[0]))]
# print(rez)
# -------------------------------------------------------------------------------------------------------------

# method3:- using zip function. Zip function gives the same result, it gives a transpose of a matrix.
# -------------------------------------------------------------------------------------------------------------

# method4:- using numpy module with transpose() method.
# import numpy as np

"""
m = [[1, 2],
     [3, 4],
     [5, 6]]
"""

# trans = np.transpose(m)
# print(trans)
# -------------------------------------------------------------------------------------------------------------