# program to sort a list using other list.
# solution:- In this example one list1 will be sorted based on the list2.

# list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
# list2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]  # output we need  ['a', 'd', 'h', 'b', 'c', 'e', 'i', 'f', 'g']


# we use zip() function to map the items with same index in both the variables/containers.
# zipped_pair = list(zip(list2, list1))
# print(zipped_pair)  # by zipping the two variables, an object will be created at certain location.
# [('a', 0), ('b', 1), ('c', 1), ('d', 0), ('e', 1), ('f', 2), ('g', 2), ('h', 0), ('i', 1)] is the result.
# each item in the zipped list will be a tuple with two items.


# items are sorted based on list2 items, also list1 items are sorted based on list2 items.
# sort_list = sorted(zipped_pair)
# print(sort_list)


# using list comprehension, make another list for the output.
# output_list = [y for (x, y) in sort_list]
# print(output_list)
# ----------------------------------------------------------------------------------------------------------------

# Look at the other example, here also we use zip() method.

# a = ("John", "Charles", "Shiva")
# b = ("Jenny", "Christy", "Monica", "Vicky")
# zip_output = list(zip(a, b))  # Unmatched index item in both lists will be left out. Here, "Vicky" is left out.
# print(zip_output)  # [('John', 'Jenny'), ('Charles', 'Christy'), ('Shiva', 'Monica')]
# ----------------------------------------------------------------------------------------------------------------