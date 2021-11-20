# program to check whether the string is Symmetrical or Palindrome.
# solution:-

"""
Input: khokho
Output:
The entered string is symmetrical
The entered string is not palindrome
"""


# method1:- my method.

# def symmetrical_checker(s):
#     l = len(s) // 2
#     if len(s) % 2 == 0 and s[:l] == s[l:]:
#         return True
#     else:
#         return False
#
# def palindrome_checker(stringg):
#     if stringg == stringg[::-1]:
#         return True
#     else:
#         return False
#
# def sym_or_palin_checker(abc):
#     if symmetrical_checker(abc):
#         print(f"{abc} is a symmetrical string")
#     elif not symmetrical_checker(abc):
#         print(f"{abc} is not a symmetrical string")
#
#     if palindrome_checker(abc):  # even we can check for palindromic string.
#         print(f"{abc} is a palindromic string")
#     elif not palindrome_checker(abc):
#         print(f"{abc} is not a palindromic string")
#
# sym_or_palin_checker("khokhokhokho")
# sym_or_palin_checker("khooohk")
# sym_or_palin_checker("amaama")
# ---------------------------------------------------------------------------------------------------------------
