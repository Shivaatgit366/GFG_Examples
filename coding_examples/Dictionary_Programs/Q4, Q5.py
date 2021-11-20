# what are the ways of sorting the dictionary by means of values.
# sort by values in a dictionary can be achieved through lambda function and itemgetter function.
# These techniques are helpful for json data related works.

# solution:-

# method1:- Using lambda function.
# Here, I can use inbuilt sorted() function.
# Use "reverse = True" for reversing the sorted items/to sort items in descending order.

# below is the list of dictionaries. 2 items are present in each dictionary.

"""
lis = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]
"""

# Remember:- "key= lambda" is written in order to sort the iterable based on the function.

# sorted_list = sorted(lis, key=lambda dict: dict["age"])  # "Manjeet" is coming after "Nandini".
# print(sorted_list)

# sorted_list2 = sorted(lis, key=lambda dict: (dict["age"], dict["name"]))  # age is sorted, then name is sorted.
# print(sorted_list2)

# sorted_list3 = sorted(lis, key=lambda dict: dict["age"], reverse=True)  # can take 3 arguments also.
# print(sorted_list3)
# --------------------------------------------------------------------------------------------------------------

# method2:- using itemgetter() function. Import operator to run itemgetter() method. It is faster than lambda method.
# itemgetter() function converts items into tuples. Do not forget to put "key=" same as we did for lambda function.

# from operator import itemgetter  # from operator module, we imported itemgetter method.

"""
lis = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]
"""

# sorted_list = sorted(lis, key=itemgetter("age"))  # "Manjeet" is coming after "Nandini".
# print(sorted_list)

# sorted_list2 = sorted(lis, key=itemgetter("age", "name"))  # age is sorted, then name is sorted.
# print(sorted_list2)

# sorted_list3 = sorted(lis, key=itemgetter("age"), reverse=True)  # can take 3 arguments also.
# print(sorted_list3)
# --------------------------------------------------------------------------------------------------------------
