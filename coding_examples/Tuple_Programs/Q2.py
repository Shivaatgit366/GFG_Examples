# program to get maximum and minimum "k" elements in a tuple.

"""
test_tup = (3, 7, 1, 18, 9)
k = 2
output = (1, 3, 9, 18)  # here we need 2 minimum and 2 maximum elements.
"""

# solution:-
# method1:- my method.

# def ascending_sort(tup1):
#     x = sorted(tup1)
#     return x

# def descending_sort(tup2):  # this is not required, still I have done because I wanted to learn sort reverse.
#     y = sorted(tup2, reverse=True)
#     return y

# def k_max_min_returner(tup, k):
#     a = ascending_sort(tup)
#     b = descending_sort(tup)
#     output = []
#     for x in a[-k:]:
#         output.append(x)
#     for y in b[-k:]:
#         output.append(y)
#     c = sorted(output)
#     return tuple(c)


# if __name__ == '__main__':
#     test_tup = (3, 7, 1, 18, 9)
#     k = 2
#     test_tup2 = (5, 20, 3, 7, 6, 8)
#     m = 2
#     print(k_max_min_returner(test_tup, k))
#     print(k_max_min_returner(test_tup2, m))
# --------------------------------------------------------------------------------------------------------------

# method2:- using loop and enumerate function.
# test_tup = (3, 7, 1, 18, 9)
# k = 2

# res = []
# test_tup2 = list(sorted(test_tup))

# for index, item in enumerate(test_tup2):
#     if index < k or index >= len(test_tup2) - k:
#         res.append(item)

# req_tuple = tuple(res)
# print(req_tuple)
# ---------------------------------------------------------------------------------------------------------------
