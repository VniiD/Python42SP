from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Interface abstrata para criaturas capazes de curar."""

    @abstractmethod
    def heal(self) -> str:
        """Executa a habilidade de cura e retorna a descrição da ação."""
        pass


class TransformCapability(ABC):
    """Interface abstrata para criaturas capazes de se transformar."""

    def __init__(self) -> None:
        self.is_transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        """Transforma a criatura alterando seu estado interno."""
        pass

    @abstractmethod
    def revert(self) -> str:
        """Restaura a criatura à sua forma original."""
        pass
