def scale_recipe(recipe, scale):
    """Scale all quantities in a recipe by a factor."""
    scaled = recipe.copy()
    for ingredient in scaled:
        scaled[ingredient] = scaled[ingredient] * scale
    return scaled


def test_scale_recipe_does_not_mutate_original():
    original = {"flour": 200}
    doubled = scale_recipe(original, 2)
    assert original == {"flour": 200}
    assert doubled == {"flour": 400}
