# How to find the ASCII value of a given string?
# ord(): It converts the given string of length one.
# The function returns an integer representing the Unicode code point of the character.
# For example, ord(‘a’) returns the integer 97.

print("Enter the string: ", end="")
name = input()
for x in name:
    unicode = ord(x)
    print("unicode code of {0} is {1}" .format(x, unicode))
# ---------------------------------------------------------------------------------------------------------------