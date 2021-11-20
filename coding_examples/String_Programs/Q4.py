# write a program to remove ith character in a string.
# Remember:- String is immutable. "Del" keyword can not be used to delete the character of a string.
# If we use replace('e', '')  function, it will replace all the other duplicate characters also.
# Remove method also can not be used to remove the character of a string. We can not use fruits.remove("banana").
# Even string object does not support assignment of values. We can not write string[k - 1] = ""

# solution:-
# method1:- using string slicing.
# test_str = "GeeksForGeeks"  # we want to remove "F", using slicing take words before and after "F".

# def character_remover(k, string):
#     val = string[:k - 1] + string[k:]
#     return val
# print(character_remover(6, test_str))
# ---------------------------------------------------------------------------------------------------------------

# method2:- using loop, appending the elements except for the ith index.
# test_str = "GeeksForGeeks"
# output = ""
# val = 1
# k = 6
# for x in range(len(test_str)):
#     if val != k:  # we can write single line code instead of all this, if x != k - 1:
#         output = output + test_str[x]
#     elif val == k:
#         val = k + 1
#         continue  # before the execution of "continue", fix the value for val. Otherwise, loop will start as it is.
#     val = val + 1
# if the "continue" word is executed, then computer won't check for the below codes. Below written codes are ignored.
# print(output)
# print(val)
# -------------------------------------------------------------------------------------------------------------
