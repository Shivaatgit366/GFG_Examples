# Find the factorial of a number.
# solution:-

# method1 :- recursion method, it means defining a function using the same function inside it.
# num1 = int(input("enter the integer\n"))
#
# def factorial(a):
#     return (1 if a==1 or a==0 else a*factorial(a-1))
#
# print("the factorial of {0} is {1}" .format(num1, factorial(num1)))
# ----------------------------------------------------------------------------------------------------------------

# method2 :- iterative method/using loops.
# num = int(input("enter the integer\n"))

# def factorial(n):
#     if n < 0:
#         return 0
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         fact = 1
#         while (n > 1):
#             fact = fact * n
#             n = n - 1
#         return fact
#
# print("the factorial of {0} is {1}" .format(num, factorial(num)))
# ----------------------------------------------------------------------------------------------------------------

# using the for loop:-

# num1 = int(input("enter the number\n"))
#
# def factorial(n):
#     fact = 1
#     for item in range(1, n+1):
#         fact = fact * item
#     return fact
# print("the factorial of", num1, "is", factorial(num1))
# ----------------------------------------------------------------------------------------------------------------

# method 3:- using in built math.factorial() method.

# import math
# num1 = int(input("enter the integer\n"))
#
# def fact_finder(n):
#     return math.factorial(n)
#
# print(f"the factorial of {num1} is {fact_finder(num1)}")
# ----------------------------------------------------------------------------------------------------------------
