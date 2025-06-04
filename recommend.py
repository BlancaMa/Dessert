import dessert
import data
import test_dessert

def get_input(prompt, valid_options):
    while True:
        print(prompt)
        answer = input("Your answer: ").lower()
        if answer in valid_options:
            return answer
        else:
            print("Sorry, that is not a valid choice. Try again.")

def recommend_dessert(texture, flavor, cuisine):
    matches = []
    for d in dessert:
        match_flavor = flavor in d["flavor"] if type(d["flavor"]) == list else flavor == d["flavor"]
        if d["texture"] == texture and match_flavor and d["cuisine"].lower() == cuisine:
            matches.append(d)
    if len(matches) == 0:
        return "Sorry, no desserts match your choices."
    best = matches[0]
    for d in matches:
        if d["calories"] < best["calories"]:
            best = d
    return "We recommend: " + best["name"].title() + " with " + str(best["calories"]) + " calories."

def main():
    print("Welcome to the Dessert Recommender!")
    texture = get_input("Choose a texture (chewy, soft, creamy, crispy, smooth):", ["chewy", "soft", "creamy", "crispy", "smooth"])
    flavor = get_input("Choose a flavor (chocolate, vanilla, fruits, cinnamon, coffee):", ["chocolate", "vanilla", "fruits", "cinnamon", "coffee"])
    cuisine = get_input("Choose a cuisine (American, Hispanic, French, Asian):", ["american", "hispanic", "french", "asian"])
    result = recommend_dessert(texture, flavor, cuisine)
    print(result)

if __name__ == "__main__":
    main()


# The function filters desserts based on a target flavor
# flavor[str]: the flavor to filter by
# desserts[list]: list of Dessert objects
# Returns a list of desserts matching the flavor
#def find_by_flavor(flavor: str, desserts: list) -> list:
    #return [d for d in desserts if flavor in d.flavor]

# The function returns all desserts under a given calorie count
# limit[int]: calorie limit
# desserts[list]: list of Dessert objects
# Returns a list of desserts with calories less than or equal to limit
#def filter_by_calories(limit: int, desserts: list) -> list:
    #return [d for d in desserts if d.calories <= limit]

# The function filters desserts based on cuisine
# cuisine[str]: the cuisine to filter by
# desserts[list]: list of Dessert objects
# Returns a list of desserts matching the given cuisine
#def filter_by_cuisine(cuisine: str, desserts: list) -> list:
    #return [d for d in desserts if d.cuisine.lower() == cuisine.lower()]

# The function filters desserts by texture
# texture[str]: the texture to filter by
# desserts[list]: list of Dessert objects
# Returns a list of desserts with the specified texture
#def filter_by_texture(texture: str, desserts: list) -> list:
    #return [d for d in desserts if d.texture.lower() == texture.lower()]

# The function adds a new dessert to the dessert manager
# dessert[Dessert]: a Dessert object to add
# manager[DessertManager]: the dessert manager instance
# Returns nothing, modifies dessert list in place
#def add_dessert(dessert: 'Dessert', manager: 'DessertManager') -> None:
    #manager.desserts.append(dessert)




def find_by_flavor(dessert, flavor):
    return [d for d in dessert if d["flavor"] == flavor]


# Function to find desserts by texture
def find_by_texture(dessert, texture):
    return [d for d in dessert if d["texture"] == texture]


# Function to find desserts by cuisine
def find_by_cuisine(dessert, cuisine):
    return [d for d in dessert if d["cuisine"] == cuisine]