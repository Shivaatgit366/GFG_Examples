# Function to calculate order of the number.
# solution:-

# Function to calculate order of the number
def order(x):
    # Variable to store of the number
    n = 0
    while (x != 0):
        x = x // 10
        n = n + 1  # this increment statement can be even written above also. No problem.
    return n

print(order(4))
print(order(456))