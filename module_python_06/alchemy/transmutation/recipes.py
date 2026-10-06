from elements import create_fire
from alchemy.elements import create_air
from ..potions import strength_potion


def lead_to_gold() -> str:
    air: str = create_air()
    fire: str = create_fire()
    potion: str = strength_potion()
    return (
        f"Recipe transmuting Lead to Gold: brew '{air}' and '{potion}' "
        f"mixed with '{fire}'"
    )
