# find the largest number in given list.
# solution:-

# method1:- use the in built .sort() method. It arranges the items in the ascending order.
# sort() method does not return anything, it changes the original list.
# list1 = [10, 20, 99, 45, 4]
# list1.sort()
# print(f"the largest number in the given list is {list1[-1]}")
# ---------------------------------------------------------------------------------------------------------------

# method2:- using the built in max() method. It gives the maximum value in the given list.
# list1 = [10, 20, 4, 45, 99]
# print("Largest element is:", max(list1))
# ----------------------------------------------------------------------------------------------------------------

# method3:- without using any in built functions.
# def max_returner(list1):
#     max = list1[0]  # assume that the first value of the list is maximum.
#     n = 0
#     for item in list1:
#         if item > max:
#             max = item
#         n = n + 1
#     return max
#
# user_list = [1022, 104, 4, 45, 99]
# print("maximum value of", user_list, "is", max_returner(user_list))
# ---------------------------------------------------------------------------------------------------------------