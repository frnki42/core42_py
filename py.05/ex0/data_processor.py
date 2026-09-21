from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        return True

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        ...


class NumericProcessor(DataProcessor):
    ...


class TextProcessor(DataProcessor):
    ...


class LogProcessor(DataProcessor):
    ...


def main() -> None:
    print("=== Code Nexus - Data Processor ===")


if __name__ == "__main__":
    main()
