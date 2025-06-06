from d1 import Dessert
from Dessert_Dictionary import American, Hispanic, French, Asian, All_Desserts
import test_dessert

#rosa and Blanca
# Prompts the user until a valid response from the options is received.
def get_input(prompt, valid_options, ):
    while True:
        print(prompt)
        answer = input("Your answer: ").lower()
        if answer in valid_options:
            return answer
        else:
            print("Sorry, that is not a valid choice. Try again.")
# Recommends the lowest-calorie dessert that matches the given texture, flavor, and cuisine.
def recommend_dessert(texture, flavor, cuisine):
    matches = []
    for d in All_Desserts:
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
# Runs the full dessert recommendation process by prompting the user and showing the result.
def main():
    print("Welcome to the Dessert Recommender!")
    texture = get_input("Choose a texture (chewy, soft, creamy, crispy, smooth):", ["chewy", "soft", "creamy", "crispy", "smooth"])
    flavor = get_input("Choose a flavor (chocolate, vanilla, fruits, cinnamon, coffee):", ["chocolate", "vanilla", "fruits", "cinnamon", "coffee"])
    cuisine = get_input("Choose a cuisine (American, Hispanic, French, Asian):", ["american", "hispanic", "french", "asian"])
    result = recommend_dessert(texture, flavor, cuisine)
    print(result)

if __name__ == "__main__":
    main()

