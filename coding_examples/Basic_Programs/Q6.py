# program to check the armstrong number:-
# solution:-

# a number with "n" digits is an armstrong number if it follows the below condition
# abcd... = pow(a, n) + pow(b, n) + pow(c, n) + pow(d, n) + ...

# method 1:-

# input_number = int(input("plz enter the number\n"))
# def checker_armstrong(num1):
#     a = str(num1)
#     num2 = 0
#     for item in a:
#         num2 = num2 + pow(int(item), len(a))
#     if num2 == num1:
#         return(f"the given {num1} is an armstrong number")
#     else:
#         return(f"the given {num1} number is not an armstrong number")
#
# print(checker_armstrong(input_number))
# --------------------------------------------------------------------------------------------------------------

def power(x, y):
    if y == 0:
        return 1
    if y % 2 == 0:
        return power(x, y // 2) * power(x, y // 2)
    if y % 2 != 0:
        return x * power(x, y // 2) * power(x, y // 2)


# Function to calculate order of the number
def order(x):
    # Variable to store of the number
    n = 0
    while (x != 0):
        n = n + 1
        x = x // 10
    return n

# Function to check whether the given number is Armstrong number or not.
def isArmstrong(num):
    n = order(num)
    abcd = num
    sum1 = 0

    while (abcd != 0):
        r = abcd % 10  # it gives the unit place digit in every iteration.
        sum1 = sum1 + power(r, n)
        abcd = abcd // 10  # it keeps dividing the number by tens place.
    return (sum1 == num)

x = int(input("enter the number\n"))
print(isArmstrong(x))
# ----------------------------------------------------------------------------------------------------------------