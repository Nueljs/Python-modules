from abc import ABC, abstractmethod
import typing
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._count: int = 0
        self._name: str = ""

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self, nb: int) -> list[tuple[int, str]]:
        output: list = self._storage[:nb]
        self._storage = self._storage[nb:]
        return (output)


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        self._name = "Numeric Processor"

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
                self._count += len(data)
            else:
                self._storage.append((len(self._storage), str(data)))
                self._count += 1
        else:
            raise ValueError("Improper numeric data")


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        self._name = "Text Processor"

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
                self._count += len(data)
            else:
                self._storage.append((len(self._storage), data))
                self._count += 1
        else:
            raise ValueError("Improper text data")


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        self._name = "Log Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            bool_list: list = []
            for ob in data:
                if isinstance(ob, dict):
                    keys: bool = all(isinstance(x, str) for x in ob.keys())
                    values: bool = all(isinstance(y, str) for y in ob.values())
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
                self._count += len(data)
            else:
                result2: str = data["log_level"] + ": " + data["log_message"]
                self._storage.append((len(self._storage), result2))
                self._count += 1
        else:
            raise ValueError("Improper log data")


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values: list = [value for _, value in data]
        line = ",".join(values)
        if not data:
            return
        print("CSV Output:")
        print(line)


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values: list = [f'"item_{key}": "{value}"' for key, value in data]
        json_str: str = "{" + ", ".join(values) + "}"
        if not data:
            return
        print("JSON Output:")
        print(json_str)


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for data in stream:
            found: bool = False
            for process in self._processors:
                if process.validate(data):
                    process.ingest(data)
                    found = True
                    break
            if not found:
                print("DataStream error - Can't process element in stream:"
                      f" {data}")

    def print_procesors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data\n")
        else:
            for process in self._processors:
                print(f"{process._name}: total "
                      f"{process._count} items processed, remaining"
                      f" {len(process._storage)} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self._processors:
            plugin.process_output(processor.output(nb))


def data_pipeline() -> None:
    np: NumericProcessor = NumericProcessor()
    tp: TextProcessor = TextProcessor()
    lp: LogProcessor = LogProcessor()
    ds: DataStream = DataStream()
    jsonp: JSONExportPlugin = JSONExportPlugin()
    csvp: CSVExportPlugin = CSVExportPlugin()
    data1: list = [
        "Hello world", [3.14, -1, 2.71],
        [{"log_level": "WARNING",
         "log_message": "Telnet access! Use ssh instead"},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42, ['Hi', 'five']
        ]
    data2: list = [
        21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},
         {'log_level': 'NOTICE', 'log_message': 'Certificate expires in'
          ' 10 days'}], [32, 42, 64, 84, 128, 168], 'World hello']

    print("Initialize Data Stream...\n")
    ds.print_procesors_stats()

    print("Registering Processors\n")
    ds.register_processor(np)
    ds.register_processor(tp)
    ds.register_processor(lp)

    print(f"Send first batch of data on stream: {data1}\n")
    ds.process_stream(data1)
    ds.print_procesors_stats()
    print("")

    print("Send 3 processed data from each processor to a CSV plugin:")
    ds.output_pipeline(3, csvp)
    print("")

    ds.print_procesors_stats()

    print("")
    print(f"Send another batch of data: {data2}\n")
    ds.process_stream(data2)

    ds.print_procesors_stats()
    print("")

    print("Send 5 processed data from each processor to a JSON plugin:")
    ds.output_pipeline(5, jsonp)

    print("")
    ds.print_procesors_stats()


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")
    data_pipeline()
