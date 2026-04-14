from ex0 import Creature
from .capability import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        self._name: str = "Sproutling"
        self._type: str = "Grass"

    def heal(self, target: str) -> str:
        return f"{self._name} heals itself for a small amount"

    def attack(self) -> str:
        return f"{self._name} uses VInes Whip!"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        self._name: str = "Bloomelle"
        self._type: str = "Grass/Fairy"

    def heal(self, target: str) -> str:
        return f"{self._name} heals itself and others for a large amount"

    def attack(self) -> str:
        return f"{self._name} uses Petal Dance!"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        self._name: str = "Shiftling"
        self._type: str = "Normal"

    def transform(self) -> str:
        return f"{self._name} shifts into a sharper form!"

    def revert(self) -> str:
        return f"{self._name} return to normal."

    def attack(self) -> str:
        return f"{self._name} attacks normally."