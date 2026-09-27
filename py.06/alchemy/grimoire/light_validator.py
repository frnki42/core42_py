from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients = light_spell_allowed_ingredients()
    input_ingredients = ingredients.lower().split()
    for allowed_ingredient in allowed_ingredients:
        for input_ingredient in input_ingredients:
            if input_ingredient.strip(",.;:!?") == allowed_ingredient:
                return ingredients + " - VALID"
    return ingredients + " - INVALID"
