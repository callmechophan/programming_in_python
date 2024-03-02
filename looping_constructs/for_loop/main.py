# used to iterate through the sequence and access each item inside the sequence
a = "for loop"

for i in a:
    print(i)

for i in range(10):
    print("Looping ... ", i)

favorites = ["Creme Brule", "Apple Pie", "Churros", "Tiramisu", "Chocolate Cake"]
for i in favorites:
    print(f"I like the desert {i}.")

# index & value
for index, value in enumerate(favorites):
    print(index, value)    
