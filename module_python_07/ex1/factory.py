from ex0.factory import CreatureFactory
from ex0.creature import Creature
from ex1.creature import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    """Fábrica concreta para a família de criaturas de cura."""

    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    """Fábrica concreta para a família de criaturas de transformação."""

    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
