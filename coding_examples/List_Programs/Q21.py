# delete each element in the below list which is divisible by 2 or all the even numbers.
# solution:-

# list1 = [11, 5, 17, 18, 23, 50]
# below code is wrong because we are simply removing the elements, but we are not returning the final list.
# list1 = [list1.remove(x) for x in list1 if x % 2 == 0]  # we can not write like this. This gives "none".

# concept: removing the even numbers is as good as keeping only the odd numbers inside the list.
# list1 = [x for x in list1 if x % 2 != 0]
# print(list1)
# ---------------------------------------------------------------------------------------------------------------

# write a program to remove items from index 1 to 4. Use "del" keyword to delete the particular element/list.
# list1 = [11, 5, 17, 18, 23, 50]
# del list1[1:5]  # 1 included and 5 is excluded.
# print(list1)
# ----------------------------------------------------------------------------------------------------------------

# write a program to remove the items from the list when we know the index elements.
# list1 = [11, 5, 17, 18, 23, 50]  # we need to remove 11, 18, 23.
# unwanted = [0, 4, 3]
# for x in sorted(unwanted, reverse=True):
#     del list1[x]
# print(list1)
# ---------------------------------------------------------------------------------------------------------------
