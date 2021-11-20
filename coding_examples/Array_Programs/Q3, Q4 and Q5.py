# write a program for array rotation.
# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.

# solution:-
# method1 :- my method
# list1 = [14, 6, 7, "abc", 28, 6, 18, 102]

# rotated_list = []

# def rotate(arr, d, n):
#     for x in range(d, n):
#         rotated_list.append(arr[x])
#     for y in range(0, d):
#         rotated_list.append(arr[y])
#     return rotated_list

# print(rotate(list1, 5, len(list1)))  # result will be   [6, 18, 102, 14, 6, 7, 'abc', 28]
# ----------------------------------------------------------------------------------------------------------------

# method2 :- list slicing.
# list1 = [14, 6, 7, "abc", 28, 6, 18, 102]

# def rotated_list(arr, d, n):
#     rotate_list = list1[d:n] + list1[0:d]
#     return rotate_list

# print(rotated_list(list1, 5, len(list1)))
# -------------------------------------------------------------------------------------------------------------