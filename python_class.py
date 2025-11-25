# Initialise Class
class Archer:
    # Define the constructor for the class
    def __init__(self, name, armor, num_weapons):
        self.name = name
        self.armor = armor
        self.num_weapons = num_weapons

soldier_1 = Archer("Legolas", 10, 2)

print(soldier_1.name)
print(soldier_1.armor)
print(soldier_1.num_weapons)