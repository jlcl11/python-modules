#!/usr/bin/env python3

import sys
import typing


def recover_text(file_name: str) -> str | None:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")
    try:
        file: typing.IO[str] = open(file_name, "r")
    except OSError as error:
        print(f"Error opening file '{file_name}': {error}")
        return None
    content: str | None = None
    try:
        content = file.read()
        print("---\n")
        print(content)
        print("---")
    except (OSError, UnicodeDecodeError) as error:
        print(f"Error reading file '{file_name}': {error}")
    finally:
        file.close()
    print(f"File '{file_name}' closed.")
    return content


def transform_text(content: str) -> str:
    result: str = ""
    for char in content:
        if char == "\n":
            result += "#"
        result += char
    if len(content) > 0 and content[len(content) - 1] != "\n":
        result += "#"
    return result


def save_text(file_name: str, content: str) -> None:
    print(f"Saving data to '{file_name}'")
    try:
        file: typing.IO[str] = open(file_name, "w")
    except (OSError, ValueError) as error:
        print(f"Error opening file '{file_name}': {error}")
        return
    try:
        try:
            file.write(content)
        finally:
            file.close()
        print(f"Data saved in file '{file_name}'.")
    except OSError as error:
        print(f"Error writing file '{file_name}': {error}")


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    content: str | None = recover_text(sys.argv[1])
    if content is None:
        return
    new_content: str = transform_text(content)
    print("\nTransform data:")
    print("---\n")
    print(new_content)
    print("---")
    new_name: str = ""
    try:
        new_name = input("Enter new file name (or empty): ")
    except (EOFError, KeyboardInterrupt, UnicodeDecodeError):
        print()
    if new_name == "":
        print("Not saving data.")
        return
    save_text(new_name, new_content)


if __name__ == "__main__":
    main()
