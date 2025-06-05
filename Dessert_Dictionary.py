#rosa
# Dictionaries

American = {
    "brownies": {
        "name": "brownie",
        "calories": 132,
        "flavor": "chocolate",
        "cuisine": "American",
        "texture": "chewy",
        "dessert_type": "cake"
    },

    "banana_split": {
        "name": "banana_split",
        "calories": 700,
        "flavor": ["chocolate", "fruits", "vanilla"],
        "cuisine": "American",
        "texture": "smooth",
        "dessert_type": "ice_cream"
    },

    "chocolate_cookies": {
        "name": "chocolate_cookies",
        "calories": 100,
        "flavor": "chocolate",
        "cuisine": "American",
        "texture": "soft",
        "dessert_type": "cookies"
    },

    "key_lime_pie": {
        "name": "key_lime_pie",
        "calories": 400,
        "flavor": "fruits",
        "cuisine": "American",
        "texture": "soft",
        "dessert_type": "pies"
    },

    "cookies_and_cream": {
        "name": "cookies_n_cream",
        "calories": 700,
        "flavor": "cookies and cream",
        "cuisine": "American",
        "texture": "creamy",
        "dessert_type": "beverages"
    },
}

Hispanic = {
    "churros": {
        "name": "churros",
        "calories": 350,
        "flavor": "cinnamon",
        "cuisine": "Hispanic",
        "texture": "crispy",
        "dessert_type": "pastries"
    },

    "flan": {
        "name": "flan",
        "calories": 250,
        "flavor": "vanilla",
        "cuisine": "Hispanic",
        "texture": "smooth",
        "dessert_type": "non_baked"
    },

    "turron": {
        "name": "turron",
        "calories": 300,
        "flavor": "fruit",
        "cuisine": "Hispanic",
        "texture": "hard",
        "dessert_type": "candy"
    },

    "polvoron": {
        "name": "polvoron",
        "calories": 200,
        "flavor": "vanilla",
        "cuisine": "Hispanic",
        "texture": "soft",
        "dessert_type": "cookies"
    },

    "arroz_con_leche": {
        "name": "arroz_con_leche",
        "calories": 280,
        "flavor": "cinnamon",
        "cuisine": "Hispanic",
        "texture": "creamy",
        "dessert_type": "non_baked"
    },
}

French = {
    "macaron": {
        "name": "macaron",
        "calories": 150,
        "flavor": "fruits",
        "cuisine": "French",
        "texture": "crispy",
        "dessert_type": "cookies"
    },

    "creme_brulee": {
        "name": "creme_brulee",
        "calories": 300,
        "flavor": "vanilla",
        "cuisine": "French",
        "texture": "creamy",
        "dessert_type": "non_baked"
    },

    "eclair": {
        "name": "eclair",
        "calories": 320,
        "flavor": "chocolate",
        "cuisine": "French",
        "texture": "smooth",
        "dessert_type": "pastries"
    },

    "tarte_aux_fruits": {
        "name": "tarte_aux_fruits",
        "calories": 350,
        "flavor": "fruits",
        "cuisine": "French",
        "texture": "chewy",
        "dessert_type": "pies"
    },

    "opera_cake": {
        "name": "opera_cake",
        "calories": 400,
        "flavor": "coffee",
        "cuisine": "French",
        "texture": "soft",
        "dessert_type": "cake"
    },
}

Asian = {
    "egg_tart": {
        "name": "egg_tart",
        "calories": 280,
        "flavor": "vanilla",
        "cuisine": "Asian",
        "texture": "crispy",
        "dessert_type": "pies"
    },

    "milk_tea": {
        "name": "milk_tea",
        "calories": 180,
        "flavor": "coffee",
        "cuisine": "Asian",
        "texture": "creamy",
        "dessert_type": "beverages"
    },

    "buko_pandan": {
        "name": "buko_pandan",
        "calories": 290,
        "flavor": "vanilla",
        "cuisine": "Asian",
        "texture": "creamy",
        "dessert_type": "non_baked"
    },

    "halo_halo": {
        "name": "halo_halo",
        "calories": 350,
        "flavor": "fruits",
        "cuisine": "Asian",
        "texture": "chewy",
        "dessert_type": "ice cream"
    },

    "daifuku": {
        "name": "daifuku",
        "calories": 250,
        "flavor": "fruits",
        "cuisine": "Asian",
        "texture": "chewy",
        "dessert_type": "candy"
    },
}

# Combine all dictionaries into a single list
All_Desserts = []

for cuisine_dict in (American, Hispanic, French, Asian):
    All_Desserts.extend(cuisine_dict.values())