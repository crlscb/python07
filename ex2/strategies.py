from abc import ABC, abstractmethod
from ex0.creatures import Creature

from ex1.capabilities import (
    HealCapability,
    TransformCapability
)


class InvalidStrategyError(Exception):
    pass


class ABattleStrategy(ABC):

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(ABattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(ABattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this aggressive strategy"
            )

        assert isinstance(creature, TransformCapability)

        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(ABattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this defensive strategy"
            )

        assert isinstance(creature, HealCapability)

        print(creature.attack())
        print(creature.heal())
