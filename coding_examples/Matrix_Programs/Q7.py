# find the kth column in the matrix.
# solution:-

"""
test_list = [[4, 5, 6],
             [8, 1, 10],
             [7, 12, 5]]
"""

# method1:- using normal method.

# def kth_column(k, matrics):
#     output = []
#     for x in range(len(matrics)):
#         value = matrics[x][k - 1]
#         output.append(value)
#     return output

# print(kth_column(3, test_list))
# ------------------------------------------------------------------------------------------------------------

# method2:- using zip() function. Since the variable has many lists inside it, we can use zip function to combine.
# This method can be used for finding the transpose of a matrix also.
# ------------------------------------------------------------------------------------------------------------