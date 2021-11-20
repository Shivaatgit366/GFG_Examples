# without using the sum function, find the sum of the items in the list.
# solution:-

# method1:- recursion method.
# list1 = [11, 5, 17, 18, 23]

# arr_len = len(list1)  # do not include this step inside the recursion.

# Remember: Do not get confused between looping and recursion. Recursion does not require looping.

# def sum_returner(arr_length, arr):
#     if arr_length == 0:
#         print("it is an empty list")  # give return 0, then next line of code <arr_length == 1> can be avoided.
#     elif arr_length == 1:
#         return arr[arr_length - 1]
#     else:
#         sum = arr[arr_length - 1] + sum_returner(arr_length - 1, arr)
#         return sum

# print(sum_returner(arr_len, list1))
# ---------------------------------------------------------------------------------------------------------------

# method2:- using while loop.
# list1 = [11, 5, 17, 18, 23]
# arr_len = len(list1)

# def sum_returner(len_arr, arr):
#     i = 0
#     sum = 0
#     while i < len_arr:
#         sum = sum + arr[i]
#         i = i + 1
#     return sum

# print(sum_returner(arr_len, list1))
# ----------------------------------------------------------------------------------------------------------------
