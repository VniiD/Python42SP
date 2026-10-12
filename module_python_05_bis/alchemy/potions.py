from elements import create_fire, create_water
from alchemy.elements import create_earth, create_air


def healing_potion() -> str:
    earth_el: str = create_earth()
    air_el: str = create_air()
    return (
        f"Healing potion brewed with '{earth_el}' "
        f"and '{air_el}'"
    )


def strength_potion() -> str:
    fire_el: str = create_fire()
    water_el: str = create_water()
    return (
        f"Strength potion brewed with '{fire_el}' "
        f"and '{water_el}'"
    )
