# write a program to find the size of the tuple object.
# solution:-
"""
Tuple1 = ("A", 1, "B", 2, "C", 3)
Tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")
Tuple3 = ((1, "Lion"), (2, "Tiger"), (3, "Fox"), (4, "Wolf"))
"""

# method1:- using the in built __sizeof__() function. The size will be obtained in "bytes".
# tuple1 = ("A", 1, "B", 2, "C", 3)
# tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")
# print("the size of the tuple is {0} bytes" .format(tuple1.__sizeof__()))
# ----------------------------------------------------------------------------------------------------------------

# method2:- using the "sys" module and getsizeof() function. The size will be obtained in "bytes".
# import sys
# tuple1 = ("A", 1, "B", 2, "C", 3)
# tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")
# print(f"the size of the tuple1 is {sys.getsizeof(tuple1)} bytes")
# print(f"the size of the tuple2 is {sys.getsizeof(tuple2)} bytes")
# ----------------------------------------------------------------------------------------------------------------
