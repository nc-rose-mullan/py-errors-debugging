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







def test_missing_ingredient_raises():
    recipe = {"flour": 200, "sugar": 50}
    with pytest.raises(IngredientMissingError) as exc_info:
        scaled_quantity_eafp(recipe, 2, "butter")
    assert str(exc_info.value) == "Missing ingredient: butter"