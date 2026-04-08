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
            return (True)
        elif isinstance(data, list):
            for i in data:
                if i is True or i is False:
                    return (False)
            return (all(isinstance(i, (int, float)) for i in data))
        return (False)

    def ingest(self, data: Any) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for i in data:
                    self._storage.append((len(self._storage), str(i)))
            else:
                self._storage.append((len(self._storage), str(data)))
        else:
            raise ValueError("Improper numeric data")


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return (True)
        elif isinstance(data, list):
            return all(isinstance(i, str) for i in data)
        return False

    def ingest(self, data: Any) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for i in data:
                    self._storage.append((len(self._storage), i))
            else:
                self._storage.append((len(self._storage), data))
        else:
            raise ValueError("Improper text data")


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            bool_list: list = []
            for obj in data:
                if isinstance(obj, dict):
                    keys: bool = all(isinstance(x, str) for x in obj.keys())
                    values: bool = all(isinstance(y, str) for y in obj.values())
                    bool_list.append(keys)
                    bool_list.append(values)
                else:
                    return (False)
            return all(bool_list)
        elif isinstance(data, dict):
            keys_ok: bool = all(isinstance(i, str) for i in data.keys())
            values_ok: bool = all(isinstance(j, str) for j in data.values())
            return (keys_ok and values_ok)
        return (False)

    def ingest(self, data: Any) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for dic in data:
                    result: str = dic["log_level"] + ": " + dic["log_message"]
                    self._storage.append((len(self._storage), result))
            else:
                result2: str = data["log_level"] + ": " + data["log_message"]
                self._storage.append((len(self._storage), result2))
        else:
            raise ValueError("Improper log data")


def data_processor() -> None:
    np: NumericProcessor = NumericProcessor()
    tp: TextProcessor = TextProcessor()
    lp: LogProcessor = LogProcessor()
    print("Testing NUmeric Processor...")
    try:
        print(f"Trying to validate input '42': {np.validate(42)}")
        print(f"Trying to validate input 'Hello': {np.validate("Hello")}")

    except ValueError as e:
        print(f"Got exception: {e}")


if __name__ == "__main__":
    print("=== COde Nexus - DAta Processor ===\n")
    data_processor()
