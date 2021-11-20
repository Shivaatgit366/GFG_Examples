# program to check whether the string is palindrome or not.
# solution:-

# method1:- list slicing. Just check whether the reversed string also matches with the given string.
# def str_palindrome_check(str1):
#     if str1[::-1] == str1:
#         return True
#     else:
#         return False

# print(str_palindrome_check("kkrkkrkk"))
# print(str_palindrome_check("malayalamalala"))
# ----------------------------------------------------------------------------------------------------------------------

# method2:- iterative method. Here half of the string length is taken, first half is compared with other half.
# def is_palindrome(str1):
#     a = len(str1)//2
#     for x in range(a):
#         if str1[x] != str1[-x -1]:
#             return False
#     return True

# s = "malayalaam"
# ans = is_palindrome(s)

# if ans:
#     print("yes it is palindrome")
# else:
#     print("it is not palindrome")
# --------------------------------------------------------------------------------------------------------------------

# method3:- using an extra variable "flag". Keep on looping if the condition is not satisfied , flag becomes 1.

# def is_palindrome(str1):
#     flag = 0  # the value of flag set to zero.
#     for x in range(len(str1)):
#         if str1[x] != str1[-x -1]:  # j = j - 1 can also be taken. Initial value of j can be given -1.
#             flag = 1
#             break

# if flag == 1:
#     return "string is not palindromic"
# elif flag == 0:
#     return "string is a palindromic"

# print(is_palindrome("malayalaam"))
# --------------------------------------------------------------------------------------------------------------------

# method4:- recursion method to find the bool value.
# Boolean values can also be used for recursion method.
# If the final Bool value is True, then final function is True. We write the condition according to that.

# def isPalindrome(s):
#     s = s.lower()  # .lower() function converts the string characters to small letter.
#     l = len(s)

    # if l < 2:
    #     return True

    # in recursion, no need to use the loop. Function itself does the iterations.
    # elif s[0] == s[l - 1]:  # if first and last characters are matched, continue the process.
    #     return isPalindrome(s[1: l - 1])  # string slicing, here 1 included and l - 1 not included.
    # else:
    #     return False

# if __name__ == '__main__':

    # s = "MalaYaLam"
    # ans = isPalindrome(s)

    # if ans:
    #     print("Yes")
    # else:
    #     print("No")
# --------------------------------------------------------------------------------------------------------------------