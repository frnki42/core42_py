from abc import ABC, abstractmethod
from typing import Any


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
            raise TypeError("Improper numeric data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._items.append((self._count, str(item)))
            self._count += 1


class TextProcessor(DataProcessor):
    ...


class LogProcessor(DataProcessor):
    ...


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    print(numeric.validate(42))


if __name__ == "__main__":
    main()
