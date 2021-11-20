# extract unique values and make a separate unique values list from dictionary values list.
# solution:-

# method1:- my method.
test_dict = {
    "gfg": [5, 6, 7, 8],
    "is": [10, 11, 7, 5],
    "best": [6, 12, 10, 8],
    "for": [1, 2, 5]
}

print("the original dictionary is {0}" .format(test_dict))

values_list = list(test_dict.values())  # .values()/.keys() functions will give an object. So convert it into a list.

sort_values = sorted(values_list)  # this is the list of values.
print(f"list of sorted values is {sort_values}")

unique_list = []  # if empty set using set() is taken, then it stores only unique values.
for m in range(len(sort_values)):
    for n in range(len(sort_values[m])):
        if sort_values[m].count(sort_values[m][n]) == 1 and sort_values[m][n] not in unique_list:
            unique_list.append(sort_values[m][n])

print(unique_list)
# ------------------------------------------------------------------------------------------------------------------

# How to count the occurrences of an item if it is inside a list of another list.
# solution:-

# fruits = [1, 4, 2, [9, 7, 8, 9], 3, 1]
# x = fruits[3].count(9)  # 3rd index is the list.
# print(x)
# ------------------------------------------------------------------------------------------------------------------
