#!/usr/bin/env python3

import sys
import typing


def recover_text(file_name: str) -> None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")
    try:
        file: typing.IO[str] = open(file_name, "r")
    except OSError as error:
        print(f"Error opening file '{file_name}': {error}")
        return
    try:
        content: str = file.read()
        print("---\n")
        print(content)
        print("---")
    except (OSError, UnicodeDecodeError) as error:
        print(f"Error reading file '{file_name}': {error}")
    finally:
        file.close()
    print(f"File '{file_name}' closed.")


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    recover_text(sys.argv[1])


if __name__ == "__main__":
    main()
