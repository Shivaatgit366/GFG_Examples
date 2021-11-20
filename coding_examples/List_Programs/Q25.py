# remove empty tuples from a list.
# solution:-

# method1:- using list comprehension.
# list_of_tuples = [(), ('laxman', '15', '8'), (), ('ram', 'sita'), ('krishna', 'aakash', '45'), ('', ''), ()]
# list_of_tuples2 = [('', '', '8'), (), ('0', '00', '000'), ('barbel', '', '45'), (''), (), ('', ''), ()]
# lst = [x for x in list_of_tuples if x is not None and x != ()]  # "if x", it means x is not None and x != ()
# lst2 = [x for x in list_of_tuples2 if x]  # "if x" means if x is not none, x exists.
# print(lst)
# print(lst2)
# ----------------------------------------------------------------------------------------------------------------

# method2:- using filter() function.
# list_of_tuples = [(), ('laxman', '15', '8'), (), ('ram', 'sita'), ('krishna', 'aakash', '45'), ('', ''), ()]
# list_of_tuples2 = [('', '', '8'), (), ('0', '00', '000'), ('barbel', '', '45'), (''), (), ('', ''), ()]
# lst = list(filter(None, list_of_tuples))  # filter function removes "None" which includes empty tuples as well.
# lst2 = list(filter(None, list_of_tuples2))  # filter() creates object after removing None and empty tuples/lists.
# print(lst)
# print(lst2)
# -----------------------------------------------------------------------------------------------------------------