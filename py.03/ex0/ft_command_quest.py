import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    argc = len(sys.argv)
    if argc > 1:
        counter = 1
        print(f"Arguments received: {argc - 1}")
        for arg in sys.argv[1:]:
            print(f"Argument {counter}: {arg}")
            counter += 1
    else:
        print("No arguments provided!")
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    main()
