# write a program to add two matrices.
# solution:-

# method1:- my method.

"""
# Input:
list1 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

list2 = [[9, 8, 7],
         [6, 5, 4],
         [3, 2, 1]]

# Output:
result = [[10, 10, 10],
          [10, 10, 10],
          [10, 10, 10]]
"""

# final_output = []
# for m in range(len(list1)):  # m value will be 0, 1, 2 and there will be three iterations.
#     temp_output = []  # for every iteration, this list starts from empty.
#     for x in range(len(list1[m])):
#         sum_row = list1[m][x] + list2[m][x]
#         temp_output.append(sum_row)
#     final_output.append(temp_output)

# print(final_output)
# ---------------------------------------------------------------------------------------------------------------

# method2:- initialize a list with all items as zero. Later, those values will be replaced with other values.

"""
list1 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

list2 = [[9, 8, 7],
         [6, 5, 4],
         [3, 2, 1]]

output_list = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]
"""

# for m in range(len(list1)):
#     for n in range(len(list1[m])):
#         output_list[m][n] = list1[m][n] + list2[m][n]

# print(output_list)  # output_list items will be updated directly by this method.
# ---------------------------------------------------------------------------------------------------------------
