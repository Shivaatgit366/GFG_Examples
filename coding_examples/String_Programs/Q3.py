# program to reverse the words in a given string.
# solution:-

# method1:- using split(), strip() and list reversal.
# str = "geeks quiz practice code"

# splitted_words = str.split()  # split() function splits the string by white spaces by default.
# reverse = splitted_words[::-1]
# output = ""
# for x in reverse:
#     output = output + x + " "
# print(output.strip())  # strip() removes extra spaces before and after the string.
# --------------------------------------------------------------------------------------------------------------

# concept:- "separator".join(list/tuple/dict)

# join() function adds the elements into a string, output will be a string.
# It takes two inputs, a separator string and a list/tuple/dict whose elements will be joined.
# In the case of a dictionary, only keys will be added with a separator.
# --------------------------------------------------------------------------------------------------------------

# method2:- using split(), join() methods.
# sentence = "geeks quiz practice code"

# word_list = sentence.split(" ")

# reverse_sentence = "#".join(reversed(word_list))  # remember:- .join() method returns the string.
# print(reverse_sentence)  # code#practice#quiz#geeks
# reverse_sentence = " ".join(reversed(word_list))
# print(reverse_sentence)  # code practice quiz geeks
# --------------------------------------------------------------------------------------------------------------