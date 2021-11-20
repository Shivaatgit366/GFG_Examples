# program to check whether the given array is monotonic.
# monotone means single tone(either ascending or descending).
# check whether the array should be ascending or descending.

# doubt

# solution:-
list1 = [13, 21, 8, 3, 6, 48, 102]
list2 = [13, 21, 38, 43, 46, 48, 148]

def monotone_asc_check(arr):
    max = arr[0]
    for x in arr:
        if x < max:
            break
        else:
            return True

def monotone_desc_check(arr):
    min = arr[0]
    for y in arr:
        if y > min:
            break
        else:
            return True

def monotone_checker(arr):
    if monotone_asc_check(arr) == True or monotone_desc_check(arr) == True:
        return True
    else:
        return False

print(monotone_checker(list1))
print(monotone_checker(list2))
