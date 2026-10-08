def scale_recipe(recipe, scale):
    """Scale all quantities in a recipe by a factor."""
    scaled = recipe
    for ingredient in scaled:
        scaled[ingredient] = scaled[ingredient] * scale
    return scaled


original = {"flour": 200, "sugar": 50, "butter": 100}
doubled = scale_recipe(original, 2)
print(doubled)
print(original)
