# open() function

# mode sets
# - r: open and read (text format)
# - rb: open and read (binary format)
# - r+: open for reading and writing
# - w: open for writing
# - a: open for editing or appending data

# close() function

# with open() function: no close function needed

with open("test.txt", mode="r") as file:
    data = file.readline()
    print(data)
