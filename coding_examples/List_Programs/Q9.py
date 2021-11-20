# program to find the smallest number in the list.
# solution:-

# method1:- using min() method. It is an in built function.
# list2 = [20, 10, 20, 1, 100]
# x = min(list2)  # min function takes the list as the argument and returns minimum value of the items.
# print(x)
# ----------------------------------------------------------------------------------------------------------------

# method2:- sort the list using in built function sorted(), and return first element in it.
# list2 = [20, 10, 20, 1, 100]
# sort_list = sorted(list2)  # use the command sorted(list2, key=reverse)  for sorting in descending order.
# print(sort_list[0])
# ------------------------------------------------------------------------------------------------------------------

# method3:- using loop, consider first element in the list as minimum.
# list2 = [20, 10, 20, 1, 100]

# min_item = list2[0]
# for i in list2:
#     if i < min_item:
#         min_item = i
# print(f"minimum value in the list is {min_item}")
# -----------------------------------------------------------------------------------------------------------------