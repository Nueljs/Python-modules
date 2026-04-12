def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    ingredients_lower: str = ingredients.lower()
    allowed: list = light_spell_allowed_ingredients()

    is_valid: bool = any(elem in ingredients_lower for elem in allowed)

    if is_valid:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
