
# The function filters desserts based on a target flavor
# flavor[str]: the flavor to filter by
# desserts[list]: list of Dessert objects
# Returns a list of desserts matching the flavor
def filter_by_flavor(flavor: str, desserts: list) -> list:
    return [d for d in desserts if flavor in d.flavor]

# The function returns all desserts under a given calorie count
# limit[int]: calorie limit
# desserts[list]: list of Dessert objects
# Returns a list of desserts with calories less than or equal to limit
def filter_by_calories(limit: int, desserts: list) -> list:
    return [d for d in desserts if d.calories <= limit]

# The function filters desserts based on cuisine
# cuisine[str]: the cuisine to filter by
# desserts[list]: list of Dessert objects
# Returns a list of desserts matching the given cuisine
def filter_by_cuisine(cuisine: str, desserts: list) -> list:
    return [d for d in desserts if d.cuisine.lower() == cuisine.lower()]

# The function filters desserts by texture
# texture[str]: the texture to filter by
# desserts[list]: list of Dessert objects
# Returns a list of desserts with the specified texture
def filter_by_texture(texture: str, desserts: list) -> list:
    return [d for d in desserts if d.texture.lower() == texture.lower()]

# The function adds a new dessert to the dessert manager
# dessert[Dessert]: a Dessert object to add
# manager[DessertManager]: the dessert manager instance
# Returns nothing, modifies dessert list in place
def add_dessert(dessert: 'Dessert', manager: 'DessertManager') -> None:
    manager.desserts.append(dessert)