from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    """Exception raised when a strategy is applied to an incompatible."""
    pass


class BattleStrategy(ABC):
    """Abstract interface for battle strategies."""

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Check if the creature is compatible with this strategy."""
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        """Execute the action sequence of the strategy for the given."""
        pass


class NormalStrategy(BattleStrategy):
    """Standard strategy suitable for any creature."""

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this normal strategy"
            )
        print(creature.attack())


class DefensiveStrategy(BattleStrategy):
    """Defensive strategy designed for creatures with healing capabilities."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this defensive strategy"
            )
        print(creature.attack())
        # Since is_valid guarantees it is a HealCapability:
        heal_ability: HealCapability = creature  # type: ignore
        print(heal_ability.heal())


class AggressiveStrategy(BattleStrategy):
    """Aggressive strategy for creatures with transform capabilities."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this aggressive strategy"
            )
        transform_ability: TransformCapability = creature  # type: ignore
        print(transform_ability.transform())
        print(creature.attack())
        print(transform_ability.revert())
