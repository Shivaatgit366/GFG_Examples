# generate a list which contains only the duplicates from the original list.
# solution:-

# method1:- using loop and count method.
# list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# list_of_duplicates = []

# i = 0
# while i < len(list1):
#     if list1.count(list1[i]) > 1 and list1[i] not in list_of_duplicates:  # important step.
#         list_of_duplicates.append(list1[i])
#     i = i + 1

# print(list_of_duplicates)
# -------------------------------------------------------------------------------------------------------------

# method2: using double loop and checking one by one.
# list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# list_of_duplicates = []

# for x in range(len(list1)):
#     for y in range(x + 1, len(list1)):
#         if list1[x] == list1[y] and list1[x] not in list_of_duplicates:
#             list_of_duplicates.append(list1[x])
# print(list_of_duplicates)
# ---------------------------------------------------------------------------------------------------------------

# program to write the unique values of the list using above double loop technique.

# lst = [15, 6, 7, 15, 25, 25, 25]
# final = []
# for m in range(len(lst)):
#     for n in range(len(lst)):
#         if lst[m] != lst[n] and lst[m] not in final:
#             final.append(lst[m])
#
# print(final)
# ----------------------------------------------------------------------------------------------------------------
