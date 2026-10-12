from typing import List


def validate_ingredients(ingredients: str) -> str:
    from alchemy.grimoire.light_spellbook import (
        light_spell_allowed_ingredients,
    )
    allowed: List[str] = light_spell_allowed_ingredients()
    ing_lower: str = ingredients.lower()
    is_valid: bool = any(item in ing_lower for item in allowed)
    status: str = "VALID" if is_valid else "INVALID"
    return f"({ingredients} {status})"
