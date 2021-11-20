# write a program to find the sum of first n natural numbers.

# recursion method is very useful.

# def sum_finder(n):
#         if n <= 0:
#             print("wrong input")
#         elif n == 1:
#             return 1
#         else:
#             sum = n + sum_finder(n - 1)
#             return sum

# print(sum_finder(5))
# --------------------------------------------------------------------------------------------------------------

# program to find the sum of the squares of first "n" natural numbers.
# recursion method:-

# def sum_squares(n):
#     if n <= 0:
#         print("wrong input")
#     elif n == 1:
#         return 1
#     else:
#         sum_num = n**2 + sum_squares(n - 1)
#         return sum_num

# print(sum_squares(5))
# ---------------------------------------------------------------------------------------------------------------

# find the sum of first n natural numbers with loop method and don't use recursion technique.

# def sum_numbers(n):
#     sum_num = 0
#     for x in range(1, n + 1):
#         sum_num = sum_num + x
#     return sum_num

# print(sum_numbers(5))
# -----------------------------------------------------------------------------------------------------------------

# find the sum of the squares of first "n" natural numbers. Do not use recursion.

# def sum_squares(n):
#     sum_square_num = 0
#     for x in range(1, n + 1):
#         sum_square_num = sum_square_num + x**2
#     return sum_square_num

# print(sum_squares(5))
# --------------------------------------------------------------------------------------------------------------
