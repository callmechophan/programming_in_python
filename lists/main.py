list1 = [1, 2, 3, 4, 5]

list2 = ['A', 'B', 'C']

list3 = ["Hello", 1, True, 40.22]

list4 = [1, [2, 3, 4], 5, 6]

# print list
print(*list1)
print(list1)

# insert: add element to list with specific index
list1.insert(0, 10)
print(list1)

# append: add element to last of list
list1.append(6)
print(list1)

# extend: add multiple element to last of list with another array
list1.extend([8, 7, 9])
print(list1)

# pop: remove element of array with specific index
list1.pop(7)
print(list1)

# del: the same pop
del list1[2]
print(list1)

# iterate
for i in list1:
    print(f"Value {i}.")
