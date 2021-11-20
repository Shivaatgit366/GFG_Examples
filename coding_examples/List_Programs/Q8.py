# multiply all the numbers in the list.
# solution:-

# method1: using loop.
# list1 = [1, 2, 3, 5, 66, 21]
#
# i = 0
# product = 1
# while i < len(list1):
#     product = product * list1[i]
#     i = i + 1
#
# print("the product of the items in the list is:", product, end="")
# ---------------------------------------------------------------------------------------------------------------

# method2: using prod() method from math module.

# import math
# list1 = [1, 2, 3, 5, 66, 21]
# list_product = math.prod(list1)  # prod() function gives the product of the items in the list.
# print(list_product)
# ---------------------------------------------------------------------------------------------------------------