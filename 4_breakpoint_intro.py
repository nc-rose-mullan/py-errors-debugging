def scale_recipe(recipe, scale):
    scaled = {}
    for ingredient, quantity in recipe.items():
        breakpoint()
        scaled[ingredient] = quantity * scale
    return scaled


print(scale_recipe({"flour": 200, "sugar": 50, "butter": 100}, 2))
