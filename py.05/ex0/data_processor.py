from abc import ABC, abstractmethod
from typing import Any


class ProcessingError(Exception):
    """Base error for all data processor failures."""


class InvalidDataError(ProcessingError):
    """Raised when data does not match the processor's type."""


class EmptyProcessorError(ProcessingError):
    """Raised when output is called with no stored data."""


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._items: list[tuple[int, str]] = []
        self._count: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        if not self._items:
            raise EmptyProcessorError("No data to output")
        return self._items.pop(0)


class NumericProcessor(DataProcessor):
    @staticmethod
    def is_number(x: Any) -> bool:
        return isinstance(x, int | float) and not isinstance(x, bool)

    @staticmethod
    def all_numbers(xs: Any) -> bool:
        if not isinstance(xs, list):
            return False
        return all(NumericProcessor.is_number(x) for x in xs)

    def validate(self, data: Any) -> bool:
        return self.is_number(data) or self.all_numbers(data)

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise InvalidDataError("Improper numeric data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._items.append((self._count, str(item)))
            self._count += 1


class TextProcessor(DataProcessor):
    ...


class LogProcessor(DataProcessor):
    ...


def show_validate(proc: DataProcessor, value: Any) -> None:
    print(f" Trying to validate input '{value}': {proc.validate(value)}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    show_validate(numeric, 42)
    show_validate(numeric, "Hello")


if __name__ == "__main__":
    main()
