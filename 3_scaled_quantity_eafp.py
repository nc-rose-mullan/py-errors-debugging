import pytest

def scaled_quantity_eafp(recipe, scale, ingredient):
    try:
        return recipe[ingredient] * scale
    except KeyError:
        return None
    except TypeError:
        return None

recipe = {"flour": 200, "sugar": 50}
output = scaled_quantity_eafp(recipe, 2, "sugar")

print(output)







# def test_missing_ingredient_raises():
#     recipe = {"flour": 200, "sugar": 50}
#     with pytest.raises(IngredientMissingError):
#         scaled_quantity_eafp(recipe, scale=2, ingredient="butter")