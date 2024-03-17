# map
# - take all elements in a list and applies a function
# 
# filter
# - create a new list with the true values

menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]

def find_coffee(lists):
    if lists[0] == 'c':
        return lists

# map
map_coffee = map(find_coffee, menu)

for m in map_coffee:
    print(m)

# filter
filter_coffee = filter(find_coffee, menu)
for f in filter_coffee:
    print(f)
