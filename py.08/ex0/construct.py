import sys


def is_in_venv() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    if is_in_venv():
        print("MATRIX STATUS: Welcome to the construct")
    else:
        print("MATRIX STATUS: You're still plugged in")


if __name__ == "__main__":
    main()
