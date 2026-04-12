from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ingredients_lower: str = ingredients.lower()
    allowed: list = dark_spell_allowed_ingredients()

    is_valid: bool = any(elem in ingredients_lower for elem in allowed)

    if is_valid:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"