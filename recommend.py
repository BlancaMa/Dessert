import dessert
import data
import test_dessert

def ask_question(prompt, options):
    print(prompt)
    for i in range(len(options)):
        print(str(i + 1) + ". " + options[i])
    while True:
        choice = input("Enter number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        else:
            print("Invalid input. Try again.")

def recommend_dessert(preferences):
    candidates = []
    for d in desserts:
        match_flavor = preferences["flavor"] in d["flavor"] if type(d["flavor"]) == list else preferences["flavor"] == d["flavor"]
        if (d["type"] == preferences["type"] and d["texture"] == preferences["texture"] and d["cuisine"] == preferences["cuisine"] and match_flavor):
            candidates.append(d)
    if len(candidates) == 0:
        return "Sorry, no dessert matches your choices."
    best = candidates[0]
    for c in candidates:
        if c["calories"] < best["calories"]:
            best = c
    return "We recommend: " + best["name"].replace("_", " ").title() + " (" + str(best["calories"]) + " calories)"

def main():
    print("Dessert Finder Quiz")
    dessert_type = ask_question("Choose dessert type:", ["cake", "cookies", "ice cream", "pastries", "non_baked", "pies", "beverages"])
    flavor = ask_question("Choose a flavor:", ["vanilla", "chocolate", "fruits", "cinnamon", "coffee"])
    texture = ask_question("Choose a texture:", ["soft", "chewy", "crispy", "creamy", "smooth"])
    cuisine = ask_question("Choose a cuisine:", ["American", "Hispanic", "French", "Asian"])
    preferences = {"type": dessert_type, "flavor": flavor, "texture": texture, "cuisine": cuisine}
    result = recommend_dessert(preferences)
    print(result)

if __name__ == "__main__":
    main()



# The function filters desserts based on a target flavor
# flavor[str]: the flavor to filter by
# desserts[list]: list of Dessert objects
# Returns a list of desserts matching the flavor
#def filter_by_flavor(flavor: str, desserts: list) -> list:
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