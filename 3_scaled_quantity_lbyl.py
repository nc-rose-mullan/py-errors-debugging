import pytest

def scaled_quantity_lbyl(recipe, scale, ingredient):
    if ingredient not in recipe:
        return None
    if not isinstance(recipe[ingredient], (int, float)):
        return None
    if scale <= 0:
        return None
    return recipe[ingredient] * scale

recipe = {"flour": 200, "sugar": 50}
output = scaled_quantity_lbyl(recipe, 2, "sugar")

print(output)





# def test_missing_ingredient_raises():
#     recipe = {"flour": 200, "sugar": 50}
#     with pytest.raises(IngredientMissingError):
#         scaled_quantity_eafp(recipe, scale=2, ingredient="butter")
