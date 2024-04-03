# attributes
# - refer to variables declared in a class
# 
# behaviors
# - associated with the methods in a class

class cube:
    # default constructor & custom constructor
    def __init__(self, __length = 1, width = 0):
        self.__length = __length # private
        self.width = width # public

    def get_volume(self):
        return self.__length * self.__length * self.__length
    
    def get_length(self):
        return self.__length
    
    def set_length(self, length):
        self.__length = length
    
c1 = cube(2, 4) # custom constructor
print(c1.get_volume())
# print(c1.__length) cannot access private variable
print(c1.get_length()) # can access through function get
print(c1.width)

print() # end line

c2 = cube() # custom default constructor
print(c2.get_volume())
c2.set_length(2)
print(c2.get_volume())