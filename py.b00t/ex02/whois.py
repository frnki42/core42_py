import sys


def main():
    if len(sys.argv) < 2:
        return
    assert len(sys.argv) == 2, "more than one argument is provided"
    try:
        nbr = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")
    if nbr == 0:
        print("I'm Zero.")
    elif nbr % 2:
        print("I'm Odd.")
    else:
        print("I'm Even.")


main()
