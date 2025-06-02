
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
               self.calories== other.calories and
               self.flavor == other.flavor and
               self.cuisine == other.cusine and
               self.texture == other.texture and
               self.type == other.type)

    def __str__(self):
        return "name: {}, calories: {}, flavor:{}, cuisine:{}, texture:{], type:{}".format(
            self.name, self.calories, self.flavor, self.cuisine, self.texture, self.type )

    def __repr__(self):
        return "name: {}, calories: {}, flavor:{}, cuisine:{}, texture:{], type:{}".format(
            self.name, self.calories, self.flavor, self.cuisine, self.texture, self.type )

    def display(self):
        print("Name: {}".format(self.name))
        print("Calories: {}".format(self.calories))
        print("Flavor: {}".format(self.flavor))
        print("Cuisine: {}".format(self.cuisine))
        print("Type: {}".format(self.type))
        print("Texture: {}".format(self.texture))

class DessertManager:
    def __init__(self):
        self.desserts = []

    def add_dessert(self, dessert):
        self.desserts.append(dessert)

    def find_by_flavor(self, flavor: str) -> list:
        return [d for d in self.desserts if flavor.lower() in d.flavor.lower()]



