from abc import ABC, abstractmethod
from ex0.creature import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    """Fábrica abstrata para criação de famílias de criaturas."""

    @abstractmethod
    def create_base(self) -> Creature:
        """Cria e retorna a criatura em forma base."""
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Cria e retorna a criatura em forma evoluída."""
        pass


class FlameFactory(CreatureFactory):
    """Fábrica concreta para a família de Fogo."""

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    """Fábrica concreta para a família de Água."""

    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
