# read(): returns a string that contains all the characters
# read(n): returns a string that contains with n characters

# readline(): returns a single line as a string
# readline(n): returns a single line as a string with a character on a line

# readlines(): returns ordered list

import random

with open("petnames.txt", "r") as file:
    lines = file.read()
    arr_petnames = lines.split("\n") # used to split the text where a new line is found

    print(arr_petnames)

print(random.choice(arr_petnames))
