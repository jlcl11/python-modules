#!/usr/bin/env python3

import sys
import typing


def print_error(message: str) -> None:
    print(f"[STDERR] {message}", file=sys.stderr)


def read_user_input(prompt: str) -> str:
    sys.stdout.write(prompt)
    sys.stdout.flush()
    return sys.stdin.readline().strip()


def recover_text(file_name: str) -> typing.Optional[str]:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")
    try:
        file: typing.IO[str] = open(file_name, "r")
    except OSError as error:
        print_error(f"Error opening file '{file_name}': {error}")
        return None
    content: typing.Optional[str] = None
    try:
        content = file.read()
        print("---\n")
        print(content)
        print("---")
    except (OSError, UnicodeDecodeError) as error:
        print_error(f"Error reading file '{file_name}': {error}")
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


def save_text(file_name: str, content: str) -> bool:
    print(f"Saving data to '{file_name}'")
    try:
        file: typing.IO[str] = open(file_name, "w")
    except OSError as error:
        print_error(f"Error opening file '{file_name}': {error}")
        return False
    saved: bool = False
    try:
        file.write(content)
        print(f"Data saved in file '{file_name}'.")
        saved = True
    except OSError as error:
        print_error(f"Error writing file '{file_name}': {error}")
    finally:
        file.close()
    return saved


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    content: typing.Optional[str] = recover_text(sys.argv[1])
    if content is None:
        return
    new_content: str = transform_text(content)
    print("\nTransform data:")
    print("---\n")
    print(new_content)
    print("---")
    new_name: str = read_user_input("Enter new file name (or empty): ")
    if new_name == "":
        print("Not saving data.")
        return
    if not save_text(new_name, new_content):
        print("Data not saved.")


if __name__ == "__main__":
    main()
