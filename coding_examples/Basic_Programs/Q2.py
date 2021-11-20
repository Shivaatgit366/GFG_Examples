# Find the maximum of two numbers
# solution:-

# method1:-

# num1 = int(input("enter the first number\n"))
# num2 = int(input("enter the second number\n"))
#
# if num1 > num2:
#     print("the number {0} is bigger than {1}" .format(num1, num2))
# else:
#     print("the number {0} is smaller than {1}" .format(num1, num2))
# -----------------------------------------------------------------------------------------------------------------

# method 2:-

# num1 = int(input("enter the first number\n"))
# num2 = int(input("enter the second number\n"))
#
# def maxima_finder(a, b):
#     if a > b:
#         return ("the number {0} is greater than {1}" .format(a, b))
#     else:
#         return ("the number {0} is smaller than {1}" .format(a, b))
#
# print(maxima_finder(num1, num2))
# ---------------------------------------------------------------------------------------------------------------

# method 3:- using max function

# num1 = int(input("enter the first number\n"))
# num2 = int(input("enter the second number\n"))
# maximum_num = max(num1, num2)  # this max() returns the maximum value of the input values.
# print("the greater number among {0} and {1} is {2}" .format(num1, num2, maximum_num))
# ----------------------------------------------------------------------------------------------------------------