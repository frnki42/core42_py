def test_error_types() -> None:
    for i in range(5):
        try:
            garden_operations(i)
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, TypeError) as e:
            print(f"Caught {e.__class__.__name__}: {e}")
        else:
            print("Operation completed successfully")


def garden_operations(operation_number: int) -> None:
    print(f"Testing operation {operation_number}...")
    match operation_number:
        case 0:
            int("abc")
        case 1:
            420 / 0
        case 2:
            open("/non/existent/file")
        case 3:
            "abc" + 420  # type: ignore
        case _:
            return


def main() -> None:
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    main()
