#!/usr/bin/env python3
import math

def get_player_pos() -> tuple[float, float, float]:
    """Ask for coordinates 'x,y,z' until a valid set is entered."""
    while True:
        try:
            raw: str = input(
                "Enter new coordinates as floats in format 'x,y,z': ")
        except EOFError:
            raise SystemExit("\nNo more input, exiting.")
        parts: list[str] = raw.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        values: list[float] = []
        valid: bool = True
        for part in parts:
            try:
                values.append(float(part))
            except ValueError as e:
                print(f"Error on parameter '{part.strip()}': {e}")
                valid = False
                break
        if valid:
            return (values[0], values[1], values[2])


def distance(a: tuple[float, float, float],
             b: tuple[float, float, float]) -> float:
    x1, y1, z1 = a
    x2, y2, z2 = b
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def main() -> None:
    """Get two positions and compute distances between them."""
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    first: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {first}")
    x, y, z = first
    print(f"It includes: X={x}, Y={y}, Z={z}")
    center: tuple[float, float, float] = (0.0, 0.0, 0.0)
    print(f"Distance to center: {round(distance(center, first), 4)}")
    print()
    print("Get a second set of coordinates")
    second: tuple[float, float, float] = get_player_pos()
    print("Distance between the 2 sets of coordinates: "
          f"{round(distance(first, second), 4)}")


if __name__ == "__main__":
    main()
