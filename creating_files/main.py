try:
    with open("newfile.txt", mode="w") as file:
        # file.write("This is a new file created!") # write a line
        file.writelines(["This is a new file created!", "\nThis is another line to be added."]) # write multiple line
except FileNotFoundError as e:
    print(e)
