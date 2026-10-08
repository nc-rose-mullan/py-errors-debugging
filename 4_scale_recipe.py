def scale_recipe(recipe, servings_from, servings_to):
    factor = servings_to // servings_from
    scaled = {}
    for ingredient, quantity in recipe.items():
        scaled[ingredient] = quantity * factor
    return scaled

recipe = {"flour": 200, "sugar": 50}
print(scale_recipe(recipe, 4, 8))  # Expected: {'flour': 400, 'sugar': 100}
print(scale_recipe(recipe, 4, 6))  # Expected{'flour': 300, 'sugar': 75}

def test_scale_recipe_non_whole_factor():
    recipe = {"flour": 200}
    assert scale_recipe(recipe, 4, 6) == {"flour": 300}