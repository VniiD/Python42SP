from abc import ABC, abstractmethod
from typing import Any, Union


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[str] = []
        self._total_processed: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data available to output.")
        item = self._storage.pop(0)
        rank = self._total_processed - len(self._storage) - 1
        return rank, item

    @property
    def total_processed(self) -> int:
        return self._total_processed

    @property
    def remaining(self) -> int:
        return len(self._storage)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list) and data:
            return all(
                isinstance(x, (int, float)) and not isinstance(x, bool)
                for x in data
            )
        return False

    def ingest(self, data: Union[int, float, list[Union[int, float]]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._storage.append(str(item))
                self._total_processed += 1
        else:
            self._storage.append(str(data))
            self._total_processed += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and data:
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: Union[str, list[str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._storage.append(item)
                self._total_processed += 1
        else:
            self._storage.append(data)
            self._total_processed += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def is_valid_log(d: Any) -> bool:
            return (
                isinstance(d, dict)
                and "log_level" in d
                and "log_message" in d
                and isinstance(d["log_level"], str)
                and isinstance(d["log_message"], str)
            )

        if is_valid_log(data):
            return True
        if isinstance(data, list) and data:
            return all(is_valid_log(x) for x in data)
        return False

    def ingest(
        self,
        data: Union[dict[str, str], list[dict[str, str]]]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        def format_log(log_dict: dict[str, str]) -> str:
            return f"{log_dict['log_level']}: {log_dict['log_message']}"

        if isinstance(data, list):
            for entry in data:
                self._storage.append(format_log(entry))
                self._total_processed += 1
        else:
            self._storage.append(format_log(data))
            self._total_processed += 1


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print(f"DataStream error Can't process in stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            print(
                f"{name}: total {proc.total_processed} items processed, "
                f"remaining {proc.remaining} on processor"
            )


if __name__ == "__main__":
    print("=== Code Nexus Data Stream ===")
    print("\nInitialize Data Stream...")
    stream_engine = DataStream()
    stream_engine.print_processors_stats()

    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()

    print("\nRegistering Numeric Processor")
    stream_engine.register_processor(num_proc)

    batch = [
        "Hello world",
        [3.14, 1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected"
            }
        ],
        42,
        ["Hi", "five"]
    ]

    print("\nSend first batch of data on stream:", batch)
    stream_engine.process_stream(batch)
    stream_engine.print_processors_stats()

    print("\nRegistering other data processors")
    stream_engine.register_processor(text_proc)
    stream_engine.register_processor(log_proc)

    print("\nSend the same batch again")
    stream_engine.process_stream(batch)
    stream_engine.print_processors_stats()

    print("\nConsume some from data process: Numeric 3, Text 2, Log 1")
    for _ in range(3):
        num_proc.output()
    for _ in range(2):
        text_proc.output()
    for _ in range(1):
        log_proc.output()

    stream_engine.print_processors_stats()
