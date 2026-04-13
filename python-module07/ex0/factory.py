from abc import ABC, abstractmethod


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> str:
        ...

    @abstractmethod
    def create_evolve(self) -> str:
        ...


class FlameFactory(CreatureFactory):



class WaterFactory(CreatureFactory):
    