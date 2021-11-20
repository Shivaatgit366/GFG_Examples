# write a program to perform vertical concatenation in matrix. If there are strings, then they should be combined.
# solution:-

"""
input_mat = [["Gfg", "good", "geeks"],
             ["is", "for", "best"]]

output = [[0, 0],
          [0, 0],
          [0, 0]]
"""

# we will take the transpose of the matrix.
# for x in range(len(input_mat)):
#     for y in range(len(input_mat[x])):
#         output[y][x] = input_mat[x][y]
# print(output)

# we will add the items inside each matrices.
# concat = []
# for m in range(len(output)):
#     temp = []
#     value = ""
#     for n in range(len(output[m])):
#         value = value + output[m][n]
#     temp.append(value)
#     concat.append(temp)

# print(concat)
# ----------------------------------------------------------------------------------------------------------
