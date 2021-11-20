# write a program to delete the key from the dictionary. If a key gets deleted, automatically value will be deleted.
# solution:-

# method1:- using "del" keyword.
# test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}
# del test_dict["Anuradha"]
# print(test_dict)
# -------------------------------------------------------------------------------------------------------------

# method2:- using pop() function. By default, it removes the last item from the dictionary.
# pop() function takes "item" as the input and removes that item from the iterable.
# test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}
# test_dict.pop("Anuradha")
# print(test_dict)
# -------------------------------------------------------------------------------------------------------------

# method3:- using loop and .items() function. Remember that dict.items() will return an object with tuple items.
# test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}
#
# val = 0
# k = 2
# new_dict = []
# for x, y in list(test_dict.items()):
#     if val != k - 1:  # we can even write in one line as    if list.index(x,y) != k - 1:
#         new_dict = new_dict + [(x, y)]
#     elif val == k - 1:
#         val = val + 1
#         continue
#     val = val + 1
#
#
# m = (new_dict)  # this is the list with items as tuples. When we convert it using dict(), it becomes the dictionary.
# print(m)
# n = dict(m)
# print(n)
# ---------------------------------------------------------------------------------------------------------------

# method4:- same above method written in a single line.
# test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}

# k = 2
# new_dict = []
# for x in list(test_dict.items()):
#     if list(test_dict.items()).index(x) != k - 1: # index() takes one variable, don't take index(x,y),it gives error.
#         new_dict = new_dict + [x]

# m = (new_dict)  # this is the list with items as tuples. When we convert it using dict(), it becomes the dictionary.
# print(m)
# n = dict(m)
# print(n)
# ------------------------------------------------------------------------------------------------------------

# concept:- After converting dictionary to an object using dict.items(), we can still update the keys and values.
"""
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
"""
# x = car.items()

# car["year"] = 2018  # the key "year" will be updated even after using dict.items().

# print(x)
# --------------------------------------------------------------------------------------------------------------