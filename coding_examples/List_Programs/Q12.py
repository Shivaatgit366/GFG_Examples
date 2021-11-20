# write a program to find N largest elements in a list.
# solution:-

# method1:- using in built sorted function and list slicing technique.
# list1 = [81, 52, 45, 10, 3, 2, 96]

# def large_returner(n, arr):
#     arr2 = sorted(arr)
#     return arr2[-n:]

# print(large_returner(4, list1))
# print(large_returner(2, list1))
# -----------------------------------------------------------------------------------------------------------------

# method2:- using loop.
# list1 = [81, 52, 45, 10, 3, 2, 96]

# def large_items_returner(arr, n):
#     final_list = []  # n largest elements will be added into the list.
#     for i in range(n):  # this is how we execute the repeated loop processes inside the other loop.
#         max_item = arr[0]  # assume first element is the maximum item.
#         for item in arr:  # till the completion of this loop, computer won't go to the next step.
#             if item > max_item:
#                 max_item = item
#         arr.remove(max_item)  # we remove the largest element from the list and append it in the empty list.
#         final_list.append(max_item)
#     return final_list

# print(large_items_returner(list1, 4))
# -----------------------------------------------------------------------------------------------------------------

# Execution of the above method using while loop.
# list1 = [81, 52, 45, 10, 3, 2, 96]


# def large_items_returner(arr, n):
#     final_list = []
#     i = 0
#     while i < n:  # to execute the repeated loop processes inside the other loop.
#         max_item = arr[0]  # assume first element is the maximum item.
#         j = 0
#         while j < len(arr):  # this loop will be completed first, then only computer goes to the next step.
#             if arr[j] > max_item:
#                 max_item = arr[j]
#             j = j + 1  # put this increment statement outside the if statement, otherwise loop will not stop.
#         arr.remove(max_item)  # we remove the largest element from the list and append it in the empty list.
#         final_list.append(max_item)
#         i = i + 1
#     return final_list

# print(large_items_returner(list1, 4))
# ----------------------------------------------------------------------------------------------------------------
