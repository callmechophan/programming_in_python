data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# updating the list
data = [x + 3 for x in data]
print(data)

# creating new list
new_data = [x * 2 for x in data]
print(new_data)

# with if
four_data = [x for x in new_data if x % 4 == 0]
print(four_data)

# with range
range_data = [x for x in range(100) if x % 9 == 0]
print(range_data)
