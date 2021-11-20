# program to print all the prime numbers in an interval.

# solution:-
int1 = int(input("enter the starting number\n"))
int2 = int(input("enter the end number of the interval\n"))
interval = range(int1, int2 + 1)
print("the numbers are in the {0}" .format(interval))

for m in interval:
    if m > 1:
        for n in range(2, m):  # this is the important step, main idea is lying in this step.
            if m % n == 0:
                break
        else:
            print(m)