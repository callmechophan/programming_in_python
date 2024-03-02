# comma separated
print(1, 2, 3)

# arithmetic
print(1 + 4)

# string concatenation
name = "Cho"
print("Hello " + name)

# parameter: sep, end...
print("Hello", "Cho", sep=', ', end='!\n')

# formatting
a = 1
b = 3
sum = a + b
print(f"{a} + {b} = {sum}")

# direct formatting
print("{} + {} = {}".format(a, b, sum))

# output formatting
print("{1} - {2} = {0}".format(a, sum, b))
