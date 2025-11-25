# Initialise Class
class Archer:
    # Define Properties of the class in name/value pairs
    health = 40
    arrows = 10

    # Add methods which are related to the class
    def take_damage(self, damage):
        self.health -= damage

# Assign istances of the class
legolas = Archer()
bard = Archer()

# Print Properties for each instance
print(legolas.health)
print(bard.arrows)

# Apply the method, providing appropriate args
legolas.take_damage(10)
print(legolas.health)