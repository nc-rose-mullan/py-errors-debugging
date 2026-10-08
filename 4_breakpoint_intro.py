def scale_recipe(recipe, scale):
    scaled = {}
    for ingredient, quantity in recipe.items():
        breakpoint()
        scaled[ingredient] = quantity * scale
    return scaled


print(scale_recipe({"flour": 200, "sugar": 50, "butter": 100}, 2))

# n  - run the next line
# s  - step into a function call
# p  - print a value (p factor)
# c  - continue to the end (or next breakpoint)
# q  - quit
