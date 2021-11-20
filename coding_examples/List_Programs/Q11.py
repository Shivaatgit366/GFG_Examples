# write a program to find the second largest number in the list.
# solution:-

# method1:- using sorted() method.
# list2 = [20, 10, 20, 1, 100]
# sort_list = sorted(list2)
# print(sort_list[-2])
# ---------------------------------------------------------------------------------------------------------------

# method2:- using loop and remove method. Remove function removes that particular item from the list.
# list1 = [20, 10, 20, 1, 100]
# list2 = [x for x in list1]
# for i in range(len(list2)):
#     for j in range(i+1, len(list2)):
#         if list2[i] > list2[j]:
#             list2[i], list2[j] = list2[j], list2[i]
# print(list2)
# list2.remove(list2[-1])  # maximum item is removed from the list.
# print(list2[-1])  # now we get second maximum item in the list.
# -----------------------------------------------------------------------------------------------------------------

# method3: using loop.
# user_list = [13, 44, 51, 3, 4, 5]
# largest = user_list[0]
# second_largest = user_list[0]

# for item in user_list:
#     if item > largest:
#         largest = item

# for j in user_list:
#     if j > second_largest and j != largest:
#         second_largest = j

# print(largest)
# print(second_largest)
# ---------------------------------------------------------------------------------------------------------------