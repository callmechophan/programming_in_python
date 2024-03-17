# using range()
data = {x: x*2 for x in range(12)}
print(data)

months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = list(range(1, 13, 1))

# using one input list
num_dict = {x : x**2 for x in number}
print(num_dict)

# using two input lists
months_dict = {key: value for (key, value) in zip(number, months)}
print(months_dict)
