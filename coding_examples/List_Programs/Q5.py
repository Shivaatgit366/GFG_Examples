# what are the different ways to clear the list?

# solution:-
# method1: using clear() method, clear function clears the items in the list.
# list1 = [12, 35, 9, 56, 24, 'ab', 23, 'ad']
# list1.clear()
# print(list1)  # we get an empty list as a result. List items will be cleared.
# ----------------------------------------------------------------------------------------------------------------

# method2: re-initialization or assigning new empty value to the list.
# list1 = [12, 35, 9, 56, 24, 'ab', 23, 'ad']
# print(f"list before the reinitialization is {str(list1)}")
# list1 = []  # re assigned list1 as an empty list.
# print(f"list after the reinitialization is {str(list1)}")
# -----------------------------------------------------------------------------------------------------------------

# method3: using "del" keyword. It means delete.
# list2 = [5, 6, 7, "gjgjgh", 45]
# print("list before using the del keyword is {0}" .format(list2))
# del list2[:]
# print("list after the use of del keyword is {0}" .format(list2))
# -----------------------------------------------------------------------------------------------------------------