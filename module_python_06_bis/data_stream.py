from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data available")
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):

    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._counter: int = 0
        self._total_processed: int = 0

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(
                isinstance(x, (int, float)) for x in data
            )
        return False

    def ingest(
        self, data: int | float | list[int | float]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append(
                (self._counter, str(item))
            )
            self._counter += 1
            self._total_processed += 1

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data available")
        return self._storage.pop(0)


class TextProcessor(DataProcessor):

    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._counter: int = 0
        self._total_processed: int = 0

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append((self._counter, item))
            self._counter += 1
            self._total_processed += 1

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data available")
        return self._storage.pop(0)


class LogProcessor(DataProcessor):

    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._counter: int = 0
        self._total_processed: int = 0

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(k, str)
                and isinstance(v, str)
                for k, v in data.items()
            )
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    return False
                if not all(
                    isinstance(k, str)
                    and isinstance(v, str)
                    for k, v in item.items()
                ):
                    return False
            return True
        return False

    def ingest(
        self,
        data: dict[str, str] | list[dict[str, str]],
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            lvl = item.get("log_level", "")
            msg = item.get("log_message", "")
            formatted = f"{lvl}: {msg}"
            self._storage.append(
                (self._counter, formatted)
            )
            self._counter += 1
            self._total_processed += 1

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data available")
        return self._storage.pop(0)


class DataStream:

    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(
        self, proc: DataProcessor
    ) -> None:
        self.processors.append(proc)

    def process_stream(
        self, stream: list[Any]
    ) -> None:
        for element in stream:
            handled = False
            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print("DataStream error")
                print(
                    "Can't process element in stream: "
                    f"{element}"
                )

    def print_processors_stats(self) -> None:
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            name = proc.__class__.__name__
            name_formatted = name.replace(
                "Processor", " Processor"
            )
            total = proc._total_processed
            rem = len(proc._storage)
            print(
                f"{name_formatted}: total {total} "
                f"items processed, remaining "
                f"{rem} on processor"
            )


if __name__ == "__main__":
    print("=== Code Nexus Data Stream ===")
    print("Initialize Data Stream..")
    stream = DataStream()
    print("DataStream statistics")
    stream.print_processors_stats()

    print("Registering Numeric Processor")
    num_proc = NumericProcessor()
    stream.register_processor(num_proc)

    batch_1 = [
        "Hello world",
        [3.14, 1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {batch_1}")
    stream.process_stream(batch_1)

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("Registering other data processors")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    stream.register_processor(text_proc)
    stream.register_processor(log_proc)

    print("Send the same batch again")
    stream.process_stream(batch_1)

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print(
        "Consume some elements from the data "
        "processors: Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        num_proc.output()
    for _ in range(2):
        text_proc.output()
    for _ in range(1):
        log_proc.output()

    print("== DataStream statistics ==")
    stream.print_processors_stats()
