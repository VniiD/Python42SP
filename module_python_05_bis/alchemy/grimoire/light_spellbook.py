from typing import List
from alchemy.grimoire.light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> List[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    validation_result: str = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} {validation_result}"
