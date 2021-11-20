# write a program for compound interest:-
# solution:-
# ** operator and the pow() function calculate the power of a number

p = float(input("enter the premium amount\n"))
t = float(input("enter the time in year\n"))
r = float(input("enter the rate of interest per year\n"))

def compound_int_calculator(a, b, c):
    total_amount = a*pow(1+(c/100), t)  # use pow(x, y) to write x raised to power y.
    return (total_amount - a)

print(f"compound interest is {compound_int_calculator(p, t, r)}rs")