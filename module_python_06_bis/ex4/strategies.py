from abc import ABC, abstractmethod
from ex3.creatures import Creature, TransformCapability
from ex4.exceptions import InvalidEntityStrategyError


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, entity: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, entity: Creature) -> list[str]:
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, entity: Creature) -> bool:
        return True

    def act(self, entity: Creature) -> list[str]:
        return [entity.attack()]


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, entity: Creature) -> bool:
        return isinstance(entity, TransformCapability)

    def act(self, entity: Creature) -> list[str]:
        if not self.is_valid(entity):
            msg = (
                f"Invalid Creature '{entity.name}' "
                "for this aggressive strategy"
            )
            raise InvalidEntityStrategyError(msg)
        transformable: TransformCapability = entity  # type: ignore
        actions = []
        actions.append(transformable.transform())
        actions.append(entity.attack())
        actions.append(transformable.revert())
        return actions
