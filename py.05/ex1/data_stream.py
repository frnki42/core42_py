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


def show_validate(proc: DataProcessor, value: Any) -> None:
    print(f" Trying to validate input '{value}': {proc.validate(value)}")


def main() -> None:
    print("=== Code Nexus - Data Stream ===")


if __name__ == "__main__":
    main()
