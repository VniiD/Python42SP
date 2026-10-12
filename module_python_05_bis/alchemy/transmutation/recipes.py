from alchemy.elements import create_air
from alchemy.potions import strength_potion
from elements import create_fire


def lead_to_gold() -> str:
    air_el: str = create_air()
    strength_pot: str = strength_potion()
    fire_el: str = create_fire()
    return (
        "Recipe transmuting Lead to Gold: "
        f"brew '{air_el}' and '{strength_pot}' "
        f"mixed with '{fire_el}'"
    )
