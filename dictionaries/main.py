# key : value pair
# - values can be changed or updated

dict1 = {1: "Coffee", 2: "Tea", 3: "Juice"}

# access item in dict
print(dict1[1])
print(dict1.get(1))

# update item in dict
dict1[3] = "Mint Tea"
print(dict1)

# add item to dict
dict1[4] = "Milk"
dict1.update({5: "Milk Tea"})
print(dict1)

# delete item in dict
del dict1[1]
print(dict1)

# iterate
for key, value in dict1.items():
    print(f"{str(key)} : {value}")
