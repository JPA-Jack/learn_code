#class variables
class wall:
    height = 10

#instance variables
class wall:
    def __init__(self):
        self.height = 10

#public members
class wall:
    def __init__(self, height):
        self.height = height

#private members
class wall:
    def __init__(self, height):
        self.__height = height

# Use Insatnace not class variables as they are easier to maintain and localise for modularity.

# Public members are callable outside of the class constructor, Private members are not.