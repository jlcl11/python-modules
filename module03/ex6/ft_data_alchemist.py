#!/usr/bin/env python3
import random

def main() -> None:
    print("=== Game Data Alchemist ===")
    print()
    players: list[str] = ["Alice", "bob", "Charlie", "dylan", "Emma",
                          "Gregory", "john", "kevin", "Liam"]
    print(f"Initial list of players: {players}")

    all_cap: list[str] = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_cap}")
    only_cap: list[str] = [n for n in players if n == n.capitalize()]
    print(f"New list of capitalized names only: {only_cap}")
    print()

    scores: dict[str, int] = {n: random.randint(0, 1000) for n in all_cap}
    print(f"Score dict: {scores} \n")
    average: float = sum(scores.values()) / len(scores)
    print(f"Score average is {round(average, 2)}")
    high: dict[str, int] = {n: s for n, s in scores.items() if s > average}
    print(f"High scores: {high}")


if __name__ == "__main__":
    main()
