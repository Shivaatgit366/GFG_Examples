# program to check whether the element exists or not.

# solution:-
# method1: use in keyword.
# list1 = [12, 35, 9, 56, 24, "ab", 23, "ad"]
# x = str(list1)
# print(x)  # list items converted into string, result is    [12, 35, 9, 56, 24, 'ab', 23, 'ad']
# print("12 in list1")  # it gives the string "12 in list1"
# print(12 in list1)  # it gives the boolean value True
# -----------------------------------------------------------------------------------------------------------------

# method2: using loop.
# list1 = [12, 35, 9, 56, 24, 'ab', 23, 'ad']
# for x in list1:
#     if x == "ab":
#         print("the item exists in the list")
# -----------------------------------------------------------------------------------------------------------------

# method3: using count(), count function gives the number of occurrences of an item in the list.
# list1 = [12, 35, 9, 56, 24, 'ab', 23, 'ad']
# counter = list1.count("ad")
# if counter >= 1:
#     print(f"\"ad\" is present in the list")
# else:
#     print(f"\"ad\" is not present inside the list")
# ------------------------------------------------------------------------------------------------------------------