def validate_ingredients(ingredients: str) -> str:
    from .dark_spellbook import dark_spell_allowed_ingredients

    allowed: list[str] = dark_spell_allowed_ingredients()

    for item in allowed:
        if item in ingredients.lower():
            return "VALID"

    return "INVALID"
