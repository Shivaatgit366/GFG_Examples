# write a program to make a copy of the list.
# Remember:- Do not use list2 = list1.copy() function because it takes 1 second extra time from other methods.
# solution:-

# method1: using list comprehension.
# list1 = [4, 8, 2, 10, 15, 18]
# list2 = [x for x in list1]
# print(list2)
# --------------------------------------------------------------------------------------------------------------

# method2:- using list slicing technique.
# list1 = [4, 8, 2, 10, 15, 18]
# list2 = list1[:]
# print(list2)
# ---------------------------------------------------------------------------------------------------------------

# method3:- using list() function.
# li1 = [4, 8, 2, 10, 15, 18]
# li2 = list(li1)
# print(li2)
# ---------------------------------------------------------------------------------------------------------------

# method4:- using extend() function we can append elements of the other list to the original list.
# li1 = [4, 8, 2, 10, 15, 18]
# li2 = []  # an empty list is created so that elements from "li1" will be added to this empty list.
# li2.extend(li1)  # we can add elements of other list using "+" operator also.
# print(li2)
# ---------------------------------------------------------------------------------------------------------------