import sys

def main():
    try:
        A = int(sys.argv[1])
        B = int(sys.argv[2])
    except ValueError:
        raise AssertionError("only integers")
    print(f"Sum:        {A + B}")
    print(f"Difference: {A - B}")
    print(f"Product:    {A * B}")
    print(f"Quotient:   {A / B}")
    print(f"Remainder:  {A % B}")
