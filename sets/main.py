# don't allow duplicate values
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9}

print(set1)
print(set2)

# add: add element to set
set1.add(6)
print(set1)

# remove: remove element of set
set1.remove(2)
print(set1)

# discard: the same remove
set1.discard(3)
print(set1)

# union or |: merge two sets
print(set1.union(set2))
print(set1 | set2)

# intersection or &: intersection of two sets
print(set1.intersection(set2))
print(set1 & set2)

# difference or -: difference of set with another set
print(set1.difference(set2))
print(set1 - set2)

# symmetric_difference or ^: common of two sets
print(set1.symmetric_difference(set2))
print(set1 ^ set2)
