import sys


def main() -> None:
    amount_args = len(sys.argv)
    if amount_args != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")
    try:
        file = open(file_name)
    except OSError as e:
        print(f"Error opening file '{file_name}': {e}")
        return
    try:
        content = file.read()
    except UnicodeDecodeError as e:
        print(f"Error reading file '{file_name}': {e}")
    else:
        print(f"---\n\n{content}\n---")
    finally:
        file.close()
        print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    main()
