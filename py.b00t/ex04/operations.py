import sys


def operations():
    if len(sys.argv) < 3:
        print("Usage: python operations.py <number1> <number2>")
        print("Example:")
        print("    python operations.py 10 3")
        return
    assert len(sys.argv) < 4, "too many arguments"
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    except ValueError:
        raise AssertionError("only integers") from None
    print(f"Sum:        {a + b}")
    print(f"Difference: {a - b}")
    print(f"Product:    {a * b}")
    try:
        print(f"Quotient:   {a / b}")
    except ZeroDivisionError:
        print("Quotient:   ERROR (division by zero)")
    try:
        print(f"Remainder:  {a % b}")
    except ZeroDivisionError:
        print("Remainder:  ERROR (modulo by zero)")


if __name__ == "__main__":
    operations()
