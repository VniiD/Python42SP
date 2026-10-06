from abc import ABC, abstractmethod
import json
from typing import Any, Protocol, Union


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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        formatted = ", ".join(item for _, item in data)
        print(f"CSV Output:\n{formatted}")


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        data_dict = {f"item_{rank}": item for rank, item in data}
        print(f"JSON Output:\n{json.dumps(data_dict)}")


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            extracted_data: list[tuple[int, str]] = []
            for _ in range(nb):
                if proc.remaining > 0:
                    extracted_data.append(proc.output())
                else:
                    break
            if extracted_data:
                plugin.process_output(extracted_data)

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
    print("=== Code Nexus Data Pipeline ===")
    print("\nInitialize Data Stream")
    stream_engine = DataStream()
    stream_engine.print_processors_stats()

    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()

    print("\nRegistering Processors")
    stream_engine.register_processor(num_proc)
    stream_engine.register_processor(text_proc)
    stream_engine.register_processor(log_proc)

    batch1 = [
        "Hello world",
        [3.14, 1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"
            },
            {"log_level": "INFO", "log_message": "User wil is connected"}
        ],
        42,
        ["Hi", "five"]
    ]

    print("\nSend first batch of data on stream:", batch1)
    stream_engine.process_stream(batch1)
    stream_engine.print_processors_stats()

    csv_plugin = CSVExportPlugin()
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream_engine.output_pipeline(3, csv_plugin)
    stream_engine.print_processors_stats()

    batch2 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days"
            }
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello"
    ]

    print("\nSend another batch of data:", batch2)
    stream_engine.process_stream(batch2)
    stream_engine.print_processors_stats()

    json_plugin = JSONExportPlugin()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream_engine.output_pipeline(5, json_plugin)
    stream_engine.print_processors_stats()
