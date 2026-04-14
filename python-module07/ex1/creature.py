from ex0 import Creature
from .capability import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        self._name: str = "Sproutling"
        self._type: str = "Grass"

    def heal(self) -> str:
        return f"{self._name} heals itself for a small amount"

    def attack(self) -> str:
        return f"{self._name} uses Vines Whip!"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        self._name: str = "Bloomelle"
        self._type: str = "Grass/Fairy"

    def heal(self) -> str:
        return f"{self._name} heals itself and others for a large amount"

    def attack(self) -> str:
        return f"{self._name} uses Petal Dance!"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        self._name: str = "Shiftling"
        self._type: str = "Normal"
        self._transformed: bool = False

    def transform(self) -> str:
        self._transformed = True
        return f"{self._name} shifts into a sharper form!"

    def revert(self) -> str:
        self._transformed = False
        return f"{self._name} returns to normal."

    def attack(self) -> str:
        if self._transformed:
            return f"{self._name} performs a boosted strike!"
        return f"{self._name} attacks normally."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        self._name: str = "Morphagon"
        self._type: str = "Normal/Dragon"
        self._transformed: bool = False

    def transform(self) -> str:
        self._transformed = True
        return f"{self._name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._transformed = False
        return f"{self._name} stabilizes its form"

    def attack(self) -> str:
        if self._transformed:
            return f"{self._name} unleashes a devastating morph strike!"
        return f"{self._name} attacks normally."
