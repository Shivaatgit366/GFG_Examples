# write a program to reverse the list.
# solution:-

# method1:- using list slicing technique.
# list1 = [10, 11, 12, 13, 14, 15]
# l1 = list1[::-1]
# print(l1)
# ---------------------------------------------------------------------------------------------------------------

# method2:- using a built in reversed() method, this function reverses the list.
# list1 = [10, 11, 12, 13, 14, 15]
# l1 = reversed(list1)  # an object is created using reversed class. If we print, we only get the object's location.
# print(l1)  # <list_reverseiterator object at 0x00000222E4529AC0>
# reversed() method creates an object at some location. Using for loop we can get those elements.
# l2 = [x for x in l1]
# print(l2)
# ----------------------------------------------------------------------------------------------------------------