
class Dessert:
    def __init__(self, name, calories, flavor, cuisine, texture, type):
        self.name= name
        self.calories = calories
        self.flavor= flavor
        self.cuisine=  cuisine
        self.texture = texture
        self.type = type


    def __eq__(self, other):
        return(self.name == other.name and
               self.cuisine== other.cuisineself.type ===)
    def __repr__(self):
