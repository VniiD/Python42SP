from alchemy.grimoire.dark_validator import (
    validate_ingredients,
)


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    status: str = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({ingredients} {status})"
