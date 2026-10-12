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

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data available")
        return self._storage.pop(0)


class TextProcessor(DataProcessor):

    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._counter: int = 0

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

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data available")
        return self._storage.pop(0)


class LogProcessor(DataProcessor):

    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._counter: int = 0

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

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data available")
        return self._storage.pop(0)


if __name__ == "__main__":
    print("=== Code Nexus Data Processor ===")
    print("Testing Numeric Processor.")
    num_proc = NumericProcessor()
    val_42 = num_proc.validate(42)
    print(f"Trying to validate input '42': {val_42}")
    val_hello = num_proc.validate("Hello")
    print(
        "Trying to validate input "
        f"'Hello': {val_hello}"
    )
    try:
        print(
            "Test invalid ingestion of string 'foo' "
            "without prior validation:"
        )
        num_proc.ingest("foo")  # type: ignore
    except ValueError as e:
        print(f"Got exception: {e}")

    print("Processing data: [1, 2, 3, 4, 5]")
    num_proc.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for i in range(3):
        rank, val = num_proc.output()
        print(f"Numeric value {i}:")
        print(val)

    print("Testing Text Processor")
    text_proc = TextProcessor()
    val_t42 = text_proc.validate(42)
    print(f"Trying to validate input '42': {val_t42}")
    print(
        "Processing data: "
        "['Hello', 'Nexus', 'World']"
    )
    text_proc.ingest(["Hello", "Nexus", "World"])
    print("Extracting 1 value...")
    rank, val = text_proc.output()
    print(f"Text value 0: {val}")

    print("Testing Log Processor.")
    log_proc = LogProcessor()
    val_l_hello = log_proc.validate("Hello")
    print(
        "Trying to validate input "
        f"'Hello': {val_l_hello}"
    )
    log_data = [
        {
            "log_level": "NOTICE",
            "log_message": "Connection to server",
        },
        {
            "log_level": "ERROR",
            "log_message": "Unauthorized access!!",
        },
    ]
    print(f"Processing data: {log_data}")
    log_proc.ingest(log_data)
    print("Extracting 2 values...")
    for i in range(2):
        rank, val = log_proc.output()
        print(f"Log entry {i}: {val}")
