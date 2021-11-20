# find position of maximum, minimum value in a list.
# solution:-

# method1 :- using in built function .index(), max() and min() we can find the required position.

# def minmax(list_input):
#     maxpos = list_input.index(max(list_input))
#     minpos = list_input.index(min(list_input))
#
#     print(f"The maximum is at position {maxpos + 1}")
#     print(f"The minimum is at position {minpos + 1}")
#
# a = [3, 4, 1, 3, 4, 5]
# minmax(a)
# ----------------------------------------------------------------------------------------------------------------

# method2 :- Find only the max and min values, no need of indexes, without using in built function.
# min and max indexes are taken 1st element.

# user_list = [13, 44, 51, 3, 4, 5]
# min = user_list[0]
# max = user_list[0]
# for element in range(len(user_list)):
#     if user_list[element] > max:
#         max = user_list[element]
#     if user_list[element] < min:
#         min = user_list[element]
# print(f"the maximum value is {max}")
# print(f"the minimum value is {min}")
# --------------------------------------------------------------------------------------------------------------