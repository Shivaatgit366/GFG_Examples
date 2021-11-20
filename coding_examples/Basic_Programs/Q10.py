# Python Program for n-th Fibonacci number.
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation
# Fn = F<n-1> + F<n-2>  # here "n" is the place value of the number.
# F1 is the starting number in the Fibonacci series and it's value is 0.
# ---------------------------------------------------------------------------------------------------------------

# method1:- recursion.
# def Fibonacci(n):
#
#     if n <= 0:
#         print("Incorrect input")
#     elif n == 1:  # First Fibonacci number is considered 0
#         return 0
#     elif n == 2:  # Second Fibonacci number is 1
#         return 1
#     else:
#         y = Fibonacci(n - 1) + Fibonacci(n - 2)
#         return y
# print(Fibonacci(10))
# ----------------------------------------------------------------------------------------------------------------

# method2:- recursion with list and append technique.
# concept:- take first two FIXED fibonacci numbers (0 & 1) inside a list. Then append the other items by recursion.

# fib_array = [0, 1]

# def fibonacci(n):
#     if n <= 0:
#         print("incorrect input")
#     elif n == 1:
#         return fib_array[n - 1]
#     elif n == 2:
#         return fib_array[n - 1]
#     else:
#         fib_number = fibonacci(n - 1) + fibonacci(n - 2)
#         fib_array.append(fib_number)
#         return fib_number

# print(fibonacci(10))
# --------------------------------------------------------------------------------------------------------------

# method3:- space optimization technique.

# def fibonacci(n):

# a = 0
# b = 1

# if n <= 0:
#     print("not valid input")
# elif n == 1:
#     return a
# elif n == 2:
#     return b
# else:
#     for i in range(3, n + 1):
#         c = a + b
#         a = b
#         b = c  # this step can be written in one line as a, b = b, c.
#     return b

# print(fibonacci(3))
# ---------------------------------------------------------------------------------------------------------------

# method4:- create a list using the recursion technique and append function. Find the last item.

# def fibonacci(n):
#     fib_list = [0, 1]
#     if n <= 0:
#         print("invalid input")
#     elif n == 1:
#         return fib_list[n - 1]
#     elif n == 2:
#         return fib_list[n - 1]
#     else:
#         for i in range(2, n):
#             fib_list.append(fib_list[i - 1] + fib_list[i - 2])
#         print(fib_list)
#         return fib_list[-1]

# print(fibonacci(10))
# -------------------------------------------------------------------------------------------------------------

# method5: math module and sqrt. Direct formula.

from math import sqrt


def fibonacci(n):  # remember, here fibonacci of 1st number is 1. It starts from 1 directly.
    res = (((1 + sqrt(5)) ** n) - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5))
    return res


print(fibonacci(3))
# --------------------------------------------------------------------------------------------------------------