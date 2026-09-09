MIN_TEMP = 0
MAX_TEMP = 40


def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < MIN_TEMP:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    elif temp > MAX_TEMP:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return temp


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
    try_temperature("100")
    try_temperature("-50")


def main() -> None:
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
