from abc import abstractmethod, ABC


class Creature(ABC):
    def __init__(self) -> None:
        self._name: str = ""
        self._type: str = ""

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe_creature(self) -> str:
        return f"{self._name} is a {self._type} type Creature"


class Flameling(Creature):
    def __init__(self) -> None:
        self._name: str = "Flameling"
        self._type: str = "Fire"

    def attack(self) -> str:
        return f"{self._name} uses Ember!"

    def describe_creature(self) -> str:
        return super().describe_creature()


class Pyrodon(Creature):
    def __init__(self) -> None:
        self._name: str = "Pyrodon"
        self._type: str = "Fire/Flying"

    def attack(self) -> str:
        return f"{self._name} uses Flamethrower!"

    def describe_creature(self) -> str:
        return super().describe_creature()


class Aquabub(Creature):
    def __init__(self) -> None:
        self._name: str = "Aquabub"
        self._type: str = "Water"

    def attack(self) -> str:
        return f"{self._name} uses Water Gun!"

    def describe_creature(self) -> str:
        return super().describe_creature()


class Torragon(Creature):
    def __init__(self) -> None:
        self._name: str = "Torragon"
        self._type: str = "Water"

    def attack(self) -> str:
        return f"{self._name} uses Hydro Pump!"

    def describe_creature(self) -> str:
        return super().describe_creature()