from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    ingredients: list[str] = ["bats", "frogs", "arsenic", "eyeball"]
    return ingredients


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    result: str = validate_ingredients(ingredients)
    if result == "VALID":
        raise Exception("KABOOM! Laboratory exploded!")
    return "The spell is rejected"
