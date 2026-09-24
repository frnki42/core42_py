from abc import ABC, abstractmethod
from typing import Any


LOG_LEVEL = "log_level"
LOG_MESSAGE = "log_message"


class ProcessingError(Exception):
    """Base error for all data processor failures."""


class InvalidDataError(ProcessingError):
    """Raised when data does not match the processor's type."""


class EmptyProcessorError(ProcessingError):
    """Raised when output is called with no stored data."""


class DataProcessor(ABC):
    NAME: str

    def __init__(self) -> None:
        self._items: list[tuple[int, str]] = []
        self._count: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def total(self) -> int:
        return self._count

    def remaining(self) -> int:
        return len(self._items)

    def output(self) -> tuple[int, str]:
        if not self._items:
            raise EmptyProcessorError("No data to output")
        return self._items.pop(0)


class NumericProcessor(DataProcessor):
    NAME: str = "Numeric Processor"

    @staticmethod
    def _is_number(x: Any) -> bool:
        return isinstance(x, int | float) and not isinstance(x, bool)

    @classmethod
    def _all_numbers(cls, xs: Any) -> bool:
        if not isinstance(xs, list):
            return False
        return all(cls._is_number(x) for x in xs)

    def validate(self, data: Any) -> bool:
        return self._is_number(data) or self._all_numbers(data)

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise InvalidDataError("Improper numeric data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._items.append((self._count, str(item)))
            self._count += 1


class TextProcessor(DataProcessor):
    NAME: str = "Text Processor"

    @staticmethod
    def _is_text(x: Any) -> bool:
        return isinstance(x, str)

    @classmethod
    def _all_text(cls, xs: Any) -> bool:
        if not isinstance(xs, list):
            return False
        return all(cls._is_text(x) for x in xs)

    def validate(self, data: Any) -> bool:
        return self._is_text(data) or self._all_text(data)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise InvalidDataError("Improper text data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._items.append((self._count, item))
            self._count += 1


class LogProcessor(DataProcessor):
    NAME: str = "Log Processor"

    @staticmethod
    def _is_log(x: Any) -> bool:
        return (
                isinstance(x, dict)
                and LOG_LEVEL in x
                and LOG_MESSAGE in x
                and all(isinstance(k, str) for k in x.keys())
                and all(isinstance(v, str) for v in x.values())
        )

    @classmethod
    def _all_logs(cls, xs: Any) -> bool:
        if not isinstance(xs, list):
            return False
        return all(cls._is_log(x) for x in xs)

    def validate(self, data: Any) -> bool:
        return self._is_log(data) or self._all_logs(data)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise InvalidDataError("Improper log data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            level = item[LOG_LEVEL]
            message = item[LOG_MESSAGE]
            self._items.append((self._count, f"{level}: {message}"))
            self._count += 1


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    break
            else:
                print(f"DataStream error - Can't process element "
                      f"in stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            print(f"{proc.NAME}: total {proc.total()} items processed, "
                  f"remaining {proc.remaining()} on processor")


def consume(proc: DataProcessor, count: int) -> None:
    for _ in range(count):
        proc.output()


def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()
    print("\nRegistering Numeric Processor")
    numeric = NumericProcessor()
    stream.register_processor(numeric)
    first_batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {LOG_LEVEL: "WARNING",
             LOG_MESSAGE: "Telnet access! Use ssh instead"},
            {LOG_LEVEL: "INFO",
             LOG_MESSAGE: "User wil is connected"}
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {first_batch}")
    stream.process_stream(first_batch)
    stream.print_processors_stats()
    print("\nRegistering other data processors")
    text = TextProcessor()
    stream.register_processor(text)
    log = LogProcessor()
    stream.register_processor(log)
    print("Send the same batch again")
    stream.process_stream(first_batch)
    stream.print_processors_stats()
    print("\nConsume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    consume(numeric, 3)
    consume(text, 2)
    consume(log, 1)
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
