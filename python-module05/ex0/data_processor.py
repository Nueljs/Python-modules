from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return (self._storage.pop(0))


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        if data is True or data is False:
            return (False)
        elif isinstance(data, int) or isinstance(data, float):
            return True
        elif isinstance(data, list):
            for i in data:
                if i is True or i is False:
                    return (False)
            return (all(isinstance(i, (int, float)) for i in data))
        return (False)

    def ingest(self, data: Any) -> None:
        if self.validate(data):
            if isinstance(data, list):
                self._storage.append((len(self._storage), i) for i in data)
            else:
                self._storage.append((len(self._storage), data))


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()


def data_processor() -> None:
    np: NumericProcessor = NumericProcessor()
    print(np.validate(31))
    print(np.validate(True))
    print(np.validate([1, 2, 3, 4]))
    print(np.validate([1, False, 3, 4]))


if __name__ == "__main__":
    data_processor()