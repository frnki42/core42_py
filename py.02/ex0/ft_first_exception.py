def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def try_temperature(temp_str: str) -> None:
    print(f"Input data is '{temp_str}'")
    try:
        temp = input_temperature(temp_str)
        print(f"Temperature is now {temp}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")


def test_temperature() -> None:
    try_temperature("25")
    try_temperature("abc")


def main() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
