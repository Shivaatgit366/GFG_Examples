# write a program to check whether the substring is present in a given string or not.
# solution:-

# method1:- using count() function.
# s = "geeks for geeks"
# s2 = input("enter the substring\n")
# x = s.count(s2)
# print(x)
# if x == 0:
#     print(f"the substring \"{s2}\" is not present inside the string \"{s}\"")
# else:
#     print(f"the substring \"{s2}\" exists in the string \"{s}\"")
# --------------------------------------------------------------------------------------------------------------

# method2:- "in" keyword.
# s = "geeks for geeks"
# s2 = input("enter the substring\n")

# if s2 in s:
#     print(f"\"{s2}\" is present in the string \"{s}\"")
# else:
#     print("the substring \"{0}\" is not present inside the string \"{1}\"" .format(s2, s))
# -------------------------------------------------------------------------------------------------------------

# method3:- using regex, and search() method. It gives match object. It means boolean value True/False.
# import re

# s = "geeks for geeks"
# s2 = re.search("j", s)  # if item is not present then, search() returns "None", then bool value is False.
# print(s2)  # <re.Match object; span=(6, 7), match='f'>
# if s2:  # if s2 exists, means it has content, bool value is True.
#     print("substring is present inside the string")
# else:
#     print("substring is not present")
# -------------------------------------------------------------------------------------------------------------