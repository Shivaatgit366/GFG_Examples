# write a program to find the sum of the cubes of first n natural numbers.
# recursion method:-

# def sum_cubes(n):
#     if n <= 0:
#         print("wrong input")
#     elif n == 1:
#         return 1
#     else:
#         sum_num = n**3 + sum_cubes(n - 1)
#         return sum_num

# print(sum_cubes(5))
# ---------------------------------------------------------------------------------------------------------------

# find the sum of the cubes of first "n" natural numbers. Do not use recursion.

# def sum_cubes(n):
#     sum_cubes_num = 0
#     for x in range(1, n + 1):
#         sum_cubes_num = sum_cubes_num + x**3
#     return sum_cubes_num

# print(sum_cubes(5))
# --------------------------------------------------------------------------------------------------------------
