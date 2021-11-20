# Given a text file and the task is to read the information from file word by word.

"""
Input:
I am R2J!

Output:
I
am
R2J!
"""

# solution:-
# A file will be opened in read mode. Using for loop, every line will be selected. Again put for loop for that line.
# We get the word by word in every line with double for loop. Use split function.
# A text file "shiva.txt" is available for the execution.

# with open("shiva.txt", "r") as f:  # rt mode is default mode, it should be written inside the quotes.
#     for line in f:
#         for word in line.split():  # split() gives a list after splitting the string, by default it splits spaces.
#             print(word)
# --------------------------------------------------------------------------------------------------------------