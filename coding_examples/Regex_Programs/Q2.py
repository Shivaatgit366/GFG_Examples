# program to find Uppercase, Lowercase, special character, numeric values present in the string.
# solution:-

# import re

# use the in built function re.findall() to return lists of specific characters.
# we get the list with repetitive characters.

# string1 = "ThisIsGeeksforGeeks!, 123??"

# upper_case_list = re.findall(r"[A-Z]", string1)
# lower_case_list = re.findall(r"[a-z]", string1)
# special_chars_list = re.findall(r"[. ,?!]", string1)
# numbers_list = re.findall(r"[0-9]", string1)

# print(f"upper case characters present in the string is {upper_case_list}")
# print(f"lower case characters present in the string is {lower_case_list}")
# print(f"special characters present in the string is {special_chars_list}")
# print(f"numerical values present in the string is {numbers_list}")
# ------------------------------------------------------------------------------------------------------------