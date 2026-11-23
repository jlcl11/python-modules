#!/usr/bin/env python3


def secure_archive(file_name: str, action: str = "r",
                   content: str = "") -> tuple[bool, str]:
    if action not in ("r", "w"):
        return (False, f"Invalid action '{action}': use 'r' or 'w'")
    try:
        with open(file_name, action) as file:
            if action == "r":
                return (True, file.read())
            file.write(content)
            return (True, "Content successfully written to file")
    except (OSError, ValueError) as error:
        return (False, str(error))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    result: tuple[bool, str] = secure_archive("ancient_fragment.txt")
    print(result)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    if result[0]:
        print(secure_archive("new_fragment.txt", "w", result[1]))
    else:
        print("Nothing to write: the file could not be read")


if __name__ == "__main__":
    main()
