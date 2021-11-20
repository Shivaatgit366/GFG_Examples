# Regular expression is a special pattern of characters.
# It can be used to match and find other characters in the strings.

# write a program to check whether the pattern/set of characters is present in the string or not.
# solution:-

# import re  # importing regular expressions module. We can use search() function to check whether that pattern exists.

# def check(str, pattern):
#     if re.search(pattern, str):  # takes pattern as 1st argument, string as 2nd argument.
#         print("It is a valid string, pattern is present inside the string")
#     else:  # re.search() function gives the boolean value.
#         print("It is not a valid string, pattern is not present inside the string")

# pattern = re.compile("^[1234]+$")  # compile() creates an object for the pattern. It is called pattern object.

# check("2134", pattern)
# check("349", pattern)
# --------------------------------------------------------------------------------------------------------------
