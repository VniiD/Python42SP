from abc import ABC, abstractmethod
from typing import Any, Protocol


class ExportPlugin(Protocol):

    def process_output(
        self, data: list[tuple[int, str]]
    ) -> None:
        ...


class CsvExportPlugin:

    def process_output(
        self, data: list[tuple[int, str]]
    ) -> None:
        values = [val for _, val in data]
        print(f"CSV Output:\n{','.join(values)}")


class JsonExportPlugin:

    def process_output(
        self, data: list[tuple[int, str]]
    ) -> None:
        items_str = []
        for i, (rank, val) in enumerate(data):
            items_str.append(f'"item_{rank}": "{val}"')
        joined = ", ".join(items_str)
        print(f"JSON Output:\n{{{joined}}}")


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

    def output_pipeline(
        self, nb: int, plugin: ExportPlugin
    ) -> None:
        for proc in self.processors:
            extracted: list[tuple[int, str]] = []
            count = min(nb, len(proc._storage))
            for _ in range(count):
                extracted.append(proc.output())
            if extracted:
                plugin.process_output(extracted)


if __name__ == "__main__":
    print("=== Code Nexus Data Pipeline ===")
    print("Initialize Data Stream..")
    stream = DataStream()
    print("DataStream statistics")
    stream.print_processors_stats()

    print("Registering Processors")
    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    stream.register_processor(num_proc)
    stream.register_processor(text_proc)
    stream.register_processor(log_proc)

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

    print(
        "Send 3 processed data from each "
        "processor to a CSV plugin:"
    )
    csv_plugin = CsvExportPlugin()
    stream.output_pipeline(3, csv_plugin)

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    batch_2 = [
        21,
        [
            "I love AI",
            "LLMs are wonderful",
            "Stay healthy",
        ],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash",
            },
            {
                "log_level": "NOTICE",
                "log_message": "Expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    print(f"Send another batch of data: {batch_2}")
    stream.process_stream(batch_2)

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print(
        "Send 5 processed data from each "
        "processor to a JSON plugin:"
    )
    json_plugin = JsonExportPlugin()
    stream.output_pipeline(5, json_plugin)

    print("== DataStream statistics ==")
    stream.print_processors_stats()
