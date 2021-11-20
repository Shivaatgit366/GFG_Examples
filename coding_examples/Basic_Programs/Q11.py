# test whether the given number is a fibonacci number or not.
# Hint:- A number is Fibonacci if and only if one or both of (5*n**2 + 4) or (5*n**2 – 4) is a perfect square.

# solution:-
# from math import sqrt


# def isperfectsqure(s):  # a function which tells whether the given number is a perfect square or not.
#     res = int(sqrt(s))
#     return res * res == s


# for n in range(10, 20):
#     a = 5 * n ** 2 + 4
#     b = 5 * n ** 2 - 4
#     if isperfectsqure(a) or isperfectsqure(b):
#         print(f"{n} is a fibonacci number")
#     else:
#         print(f"{n} is not a fibonacci number")
# ---------------------------------------------------------------------------------------------------------------