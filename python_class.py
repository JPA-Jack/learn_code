# Initialise Class
class Archer:
    # Define Properties of the class in name/value pairs
    health = 40
    arrows = 10

    # Add methods which are related to the class
    def take_damage(self, damage):
        self.health -= damage
    
    def health_kit_check(self, health_kit_count):
        answer = ""
        if self.health < 20:
            if health_kit_count >= 1:
                answer = "Health Kit available"
            else:
                answer = "Once this fight is over, you must go shopping"
        else:
            answer = "Yo, do some fighting first"
        return answer
        


# Assign istances of the class
legolas = Archer()
bard = Archer()

# Print Properties for each instance
print(legolas.health)
print(bard.arrows)

# Apply the method, providing appropriate args
legolas.take_damage(20)
print(legolas.health)
print(legolas.health_kit_check(1))
