READ = "r"
WRITE = "w"


def secure_archive(file_name: str, action: str = READ,
                   content: str = "") -> tuple[bool, str]:
    if action == READ:
        try:
            with open(file_name, READ) as file:
                file_content = file.read()
        except (OSError, UnicodeDecodeError) as e:
            return (False, str(e))
        return (True, file_content)
    if action == WRITE:
        try:
            with open(file_name, WRITE) as file:
                file.write(content)
        except OSError as e:
            return (False, str(e))
        return (True, "Content successfully written to file")
    return (False, "Unknown action")


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", READ))
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("inaccessible_file", READ))
    print("\nUsing 'secure_archive' to read from a regular file:")
    result = secure_archive("regular_file", READ)
    print(result)
    _, content = result
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file", WRITE, content))


if __name__ == "__main__":
    main()
