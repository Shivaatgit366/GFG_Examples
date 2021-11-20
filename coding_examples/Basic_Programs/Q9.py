# program to find whether the given number is prime number or not.

# solution:-  # my method.
int1 = 1031
if int1 > 1:
    for n in range(2, int1):  # this is the important step, main idea is lying in this step.
        if int1 % n == 0:
            print(f"{int1} is not a prime number")
            break
    else:
        print(f"{int1} is a prime number")
# -------------------------------------------------------------------------------------------------------------
