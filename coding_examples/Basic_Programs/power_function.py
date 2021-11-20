# Function to calculate x raised to the power y.
# solution:-

def power(x, y):
    if y == 0:
        return 1
    if y % 2 == 0:
        return power(x, y//2) * power(x, y//2)
    if y % 2 != 0:
        return x * power(x, y//2) * power(x, y//2)

print(power(2, 4))
# ----------------------------------------------------------------------------------------------------------------

# to understand the mod operator, these are few examples.
print(1%2)
print(5%7)
print(2%4)
print(2%8)