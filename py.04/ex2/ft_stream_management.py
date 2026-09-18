import sys


def print_error(message: str) -> None:
    print(f"[STDERR] {message}", file=sys.stderr)


def main() -> None:
    amount_args = len(sys.argv)
    if amount_args != 2:
        print("Usage: ft_stream_management.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")
    try:
        file = open(file_name)
    except OSError as e:
        print_error(f"Error opening file '{file_name}': {e}")
        return
    try:
        content = file.read()
    except UnicodeDecodeError as e:
        print_error(f"Error reading file '{file_name}': {e}")
        return
    else:
        print(f"---\n\n{content}\n---")
    finally:
        file.close()
        print(f"File '{file_name}' closed.")
    print("\nTransform data:")
    lines = [line + "#" for line in content.splitlines()]
    new_content = "\n".join(lines) + "\n"
    print(f"---\n\n{new_content}\n---")
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    input_line = sys.stdin.readline()
    if not input_line:
        print("\nNot saving data.")
        return
    new_name = input_line.strip()
    if not new_name:
        print("Not saving data.")
        return
    print(f"Saving data to '{new_name}'")
    try:
        new_file = open(new_name, "w")
    except OSError as e:
        print_error(f"Error opening file '{new_name}': {e}")
        print("Data not saved.")
        return
    try:
        new_file.write(new_content)
        new_file.close()
    except OSError as e:
        print_error(f"Error writing to file '{new_name}': {e}")
        print("Data not saved.")
        return
    finally:
        new_file.close()
    print(f"Data saved in file '{new_name}'.")


if __name__ == "__main__":
    main()
