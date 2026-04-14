from abc import abstractmethod, ABC


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str) -> str:
        ...


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...
