# write a program to interchange the first and last elements in a list.

# solution:-
# method1: just swapping the elements

# list1 = [12, 35, 9, 56, 24, "ab", 23, "ad"]

# def swapper(arr):
#     temp = arr[-1]
#     arr[-1] = arr[0]
#     arr[0] = temp    # this can be written in a single line     arr[0], arr[-1] = arr[-1], arr[0]
#     return arr

# print(swapper(list1))
# ---------------------------------------------------------------------------------------------------------------

# method2: using in built functions like pop function, insert function and append function.
# pop function takes the index value of the list, and removes the item at that index value.

# def swapper(arr):
#     first = arr.pop(0)  # pop the values and store them inside variables.
#     last = arr.pop(-1)
#     arr.insert(0, last)  # for 0th index, "last" variable value will be inserted.
#     arr.append(first)
#     return arr

# print(swapper([12, 35, 9, 56, 24, "ab", 23, "ad"]))
# ----------------------------------------------------------------------------------------------------------------