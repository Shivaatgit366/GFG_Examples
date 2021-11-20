# program to find the cumulative sum of a list.
# solution:-

# method1:- using loop and sum() function.
# list1 = [10, 20, 30, 40, 50]
# list_cumulative = []
# i = 0
# while i < len(list1):
#     cumulative = sum(list1[:i+1])
#     list_cumulative.append(cumulative)
#     i = i + 1
# print(list_cumulative)
# ---------------------------------------------------------------------------------------------------------------

# usage of sum function in the case of list slicing.
# list1 = [10, 20, 30, 40, 50]
# sum1 = sum(list1[:8])  # we can write any number greater than the length of the list. Here 8 is written.
# print(sum1)
# ---------------------------------------------------------------------------------------------------------------

# method2:- using loop.
# list1 = [10, 20, 30, 40, 50]
# list2 = []
# sum1 = 0
# for x in list1:
#     sum1 = sum1 + x
#     list2.append(sum1)
# print(list2)
# ---------------------------------------------------------------------------------------------------------------