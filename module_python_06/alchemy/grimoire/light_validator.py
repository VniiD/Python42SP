from alchemy.grimoire.light_spellbook import (
    light_spell_allowed_ingredients,
)


def validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = light_spell_allowed_ingredients()
    ing_list: list[str] = [i.strip().lower() for i in ingredients.split(",")]
    for ing in ing_list:
        if ing in allowed:
            return "VALID"
    return "INVALID"
