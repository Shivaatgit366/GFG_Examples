# remove empty list and "None" items from the list.

# method1:- using loop/list comprehension.
# test_list = [5, 6, [], 3, [], [], 9]
# test_list = [x for x in test_list if x != [] and x is not None]
# print(test_list)
# --------------------------------------------------------------------------------------------------------------

# method2:- using filter() function.
# concept:- "None" keyword contains empty lists also. If we filter "None", empty lists will be deleted too.
# Filter function gives object at a location. So, we convert it to a list.
# test_list = [5, 6, [], 3, [], [], 9]  # we use filter method, built in method.
# resultant = list(filter(None, test_list))  # none values include empty lists as well, they will be deleted.
# print(resultant)
# ---------------------------------------------------------------------------------------------------------------