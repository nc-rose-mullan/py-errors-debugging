import pytest


class RecipeError(Exception):
    """Base exception for recipe operations."""
    pass


class IngredientMissingError(RecipeError):
    def __init__(self, ingredient):
        self.ingredient = ingredient
        super().__init__(f"Missing ingredient: {ingredient}")


def scaled_quantity(recipe, scale, ingredient):
    if scale <= 0:
        raise RecipeError(f"Invalid scale: {scale}. Must be positive.")
    try:
        return recipe[ingredient] * scale
    except KeyError:
        raise IngredientMissingError(ingredient)


def test_missing_ingredient_raises():
    recipe = {"flour": 200, "sugar": 50}
    with pytest.raises(IngredientMissingError) as exc_info:
        scaled_quantity(recipe, scale=2, ingredient="butter")
    assert exc_info.value.ingredient == "butter"
