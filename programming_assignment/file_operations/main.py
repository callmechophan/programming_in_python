def read_file(filename: str):
    """
    Description:
        1. Open and read file using read() function
        2. Print the contents of the file
        3. Return the contents of the file

    Args:
        filename: the name or the path of file
    
    Returns:
        string: contents of the file
    """

    with open(filename, "r") as file:
        string = file.read()

    return string





def read_file_into_list(filename: str):
    """
    Description:
        1. Open and read file using readlines() function
        2. Print the contents of the file
        3. Return the contents of the file

    Args:
        filename: the name or the path of file
    
    Returns:
        lists: contents of the file into a list
    """

    with open(filename, "r") as file:
        lists = file.readlines()
    
    return lists





def write_first_line_to_file(file_contents: str, output_filename: str):
    """
    Description:
        1. Get the first_line from file_contents
        2. Open and write the first line into output_filename using write() function

    Args:
        file_contents: all contents of the file
        output_filename: name of file will write the first_line
    """

    lists = file_contents.splitlines() # splitlines() method splits a string into a list

    try:
        first_line = lists[0]
    except:
        # if file_contents is null or blank
        first_line = file_contents

    with open(output_filename, "w") as file:
        file.write(first_line)





def read_even_numbered_lines(filename: str):
    """
    Args:
        filename: the name or the path of file
    
    Returns:
        lists: the lists of the even line in file
    """

    with open(filename, "r") as file:
        lines = file.readlines()
        lists = []
        for i in range(0, len(lines)):
            if i % 2 == 0:
                lists.append(lines[i+1])

    return lists





def read_file_in_reverse(filename: str):
    """
    Description:
        1. Open and read the given file into a lists
        2. Read the file in a list in reverse order
        3. Return the lists

    Args:
        filename: the name or the path of file
        
    Returns:
        lists: list of the lines of the file in reverse order.
    """

    with open(filename, "r") as file:
        lines = file.readlines()
        lists = []
        for i in range(len(lines) - 1, -1, -1):
            lists.append(lines[i])

    return lists





def main():
    file_contents = read_file("sampletext.txt")
    print(file_contents)

    # print(read_file_into_list("sampletext.txt"))
    # write_first_line_to_file(file_contents, "output.txt")
    # print(read_even_numbered_lines("sampletext.txt"))
    # print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()
