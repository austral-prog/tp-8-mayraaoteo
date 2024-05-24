from sets_categories_data import (ALCOHOLS)


def clean_ingredients(dish_name, dish_ingredients):
    unique_set = set()
    for elem in dish_ingredients:
        if elem not in unique_set:
            unique_set.add(elem)
    return dish_name, unique_set


def check_drinks(drink_name, drink_ingredients):
    for elem in drink_ingredients:
        if elem in ALCOHOLS:
            return f"{drink_name} Cocktail"
    return f"{drink_name} Mocktail"
