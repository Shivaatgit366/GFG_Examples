# Write a program for simple interest.
# solution:-

p = float(input("enter the premium amount\n"))
t = float(input("enter the time in year\n"))
r = float(input("enter the rate of interest per year\n"))
def simp_int_calculator(a, b, c):
    interest = float(a*b*c)/100
    return interest

print("simple interest for {0}rs premium with {1}% interest rate in {2} years is {3}" .format(p, r, t, simp_int_calculator(p,t,r)))