from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    ingredients: list[str] = ["earth", "air", "fire", "water"]
    return ingredients


def light_spell_record(spell_name: str, ingredients: str) -> str:
    result: str = validate_ingredients(ingredients)
    if result == "VALID":
        return "The spell is recorded"
    return "The spell is rejected"
