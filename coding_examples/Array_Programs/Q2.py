# write a program to find the largest element in an array.

# solution:-
# method1:- using in built function max() and min(). Put the variable/values inside the function for max/min values.
# list1 = [12, 3, 4, 15]
# set1 = {20, 10, 20, 4, 100}
# max_value = max(list1)
# min_value2 = min(set1)
# print(max_value)
# print(min_value2)
# -------------------------------------------------------------------------------------------------------------

# method2:- using loop. Take first element as maximum, then compare every item in the array with maximum value.
# list2 = [20, 10, 20, 4, 100]

# def max_finder(arr):
#     maximum_value = arr[0]
#     for x in arr:
#         if x > maximum_value:
#             maximum_value = x
#     return maximum_value

# print(max_finder(list2))
# -------------------------------------------------------------------------------------------------------------