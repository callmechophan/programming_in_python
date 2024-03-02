# - string: 
#   + is a sequence of character
#   + enclosed in single quote or double quote
c = "hello"
print(c)
print(c[1])
print(type(c))

# - list:
#   + are a sequence of (one or more) (different or similar) types
#   + each item can be accessed by its index
d = [1, "hello", 4.5, 'a']
print(d)
print(d[2])
print(type(d))

# - tuples:
#   + are similar to lists
#   + main difference is immutable (the value inside tuples cannot be modified or changed)
e = (1, "hello", 4.5, 'a')
print(e)
print(e[3])
print(type(e))
