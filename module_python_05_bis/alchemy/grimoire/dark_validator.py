from alchemy.grimoire.dark_spellbook import (
    dark_spell_allowed_ingredients,
)


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    is_valid = any(item in ingredients.lower() for item in allowed)
    status = "VALID" if is_valid else "INVALID"
    return f"({ingredients} {status})"
