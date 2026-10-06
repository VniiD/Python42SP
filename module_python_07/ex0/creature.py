from abc import ABC, abstractmethod


class Creature(ABC):
    """Classe base abstrata para todas as criaturas."""

    def __init__(self, name: str, type_: str) -> None:
        self.name: str = name
        self.type_: str = type_

    @abstractmethod
    def attack(self) -> str:
        """Retorna a mensagem do ataque da criatura."""
        pass

    def describe(self) -> str:
        """Retorna a descrição padronizada da criatura."""
        return f"{self.name} is a {self.type_} type Creature"


class Flameling(Creature):
    """Criatura base de Fogo."""

    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    """Criatura evoluída de Fogo."""

    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    """Criatura base de Água."""

    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    """Criatura evoluída de Água."""

    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        return "Torragon uses Hydro Pump!"
