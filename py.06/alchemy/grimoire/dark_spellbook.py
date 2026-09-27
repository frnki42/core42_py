from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    allowed_ingredients = [
            "bats",
            "frogs",
            "arsenic",
            "eyeball",
            ]
    return allowed_ingredients


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validation_result = validate_ingredients(ingredients)
    if validation_result.endswith("- VALID"):
        return f"Spell recorded: {spell_name} ({validation_result})"
    return f"Spell rejected: {spell_name} ({validation_result})"
