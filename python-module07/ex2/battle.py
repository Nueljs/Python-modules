from abc import ABC, abstractmethod
from typing import cast
from ex0 import Creature as Creature
from ex1 import HealCapability, TransformCapability


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:    
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise Exception(
                f"Invalid Creature '{creature._name}' for this"
                f" aggressive strategy"
            )
        creature2: TransformCapability = cast(TransformCapability, creature)
        print(creature2.transform())
        print(creature.attack())
        print(creature2.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise Exception(
                f"Invalid Creature '{creature._name}' for this"
                f" defensive strategy"
            )
        creature2: HealCapability = cast(HealCapability, creature)
        print(creature.attack())
        print(creature2.heal())
