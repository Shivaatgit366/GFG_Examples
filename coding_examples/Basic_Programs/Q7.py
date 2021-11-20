# concept:-

# b = "Hello, World!"
# print(b[18:])  # for non existing index, we get empty string as the output.
# c = [12, 3, "ash", 54, "gjghty", "gh"]
# print(c[8:0])  # for non existing index, we get empty list as the output.
# ----------------------------------------------------------------------------------------------------------------

# write a program to calculate the area of a circle.

# pi = 22/7
# radius = int(input("enter the radius of the circle\n"))
# area = pi * pow(radius, 2)
# print(f"area of the circle is {area}")
# ----------------------------------------------------------------------------------------------------------------

# write a program to sort the items in the list in ascending order.
# user_list = [1022, 1045, 4, 45585, 99]

# list_len = len(user_list)  # this gives the length of the list
# for x in range(list_len):
#     for j in range(x+1, list_len): # range(len(list)) results in descending order, bigger replace left side smaller.
#         if user_list[x] > user_list[j]:
#             temp = user_list[x]
#             user_list[x] = user_list[j]  # this can be written in one step as below comment.
#             user_list[j] = temp  # user_list[x], user_list[j] = user_list[j], user_list[x]
# print(user_list)
# ----------------------------------------------------------------------------------------------------------------

# write a program to sort the items in the list in ascending order using while loop.
user_list = [1022, 1045, 4, 45585, 99]

i = 0
len_of_list = len(user_list)
while i < len_of_list:
    j = i + 1  # defined the "j" value.
    while j < len_of_list:
        if user_list[i] > user_list[j]:
            temp = user_list[i]
            user_list[i] = user_list[j]
            user_list[j] = temp  # user_list[i], user_list[j] = user_list[j], user_list[i]
        j = j + 1
    i = i + 1
print(user_list)