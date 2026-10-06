from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


# --- Família de Cura ---

class Sproutling(Creature, HealCapability):
    """Criatura base com capacidade de cura."""

    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    """Criatura evoluída com capacidade de cura."""

    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self) -> str:
        return "Bloomelle heals itself and others for a large amount"


# --- Família de Transformação ---

class Shiftling(Creature, TransformCapability):
    """Criatura base com capacidade de transformação."""

    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self.is_transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        self.is_transformed = False
        return "Shiftling returns to normal."

    def attack(self) -> str:
        if self.is_transformed:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."


class Morphagon(Creature, TransformCapability):
    """Criatura evoluída com capacidade de transformação."""

    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self.is_transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.is_transformed = False
        return "Morphagon stabilizes its form."

    def attack(self) -> str:
        if self.is_transformed:
            return "Morphagon unleashes a devastating morph strike!"
        return "Morphagon attacks normally."
