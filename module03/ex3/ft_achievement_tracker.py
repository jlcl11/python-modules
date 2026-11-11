#!/usr/bin/env python3
import random

ACHIEVEMENTS: list[str] = [
    "Crafting Genius", "Strategist", "World Savior", "Speed Runner",
    "Survivor", "Master Explorer", "Treasure Hunter", "Unstoppable",
    "First Steps", "Collector Supreme", "Untouchable", "Sharp Mind",
    "Boss Slayer", "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    count: int = random.randint(5, 9)
    return set(random.sample(ACHIEVEMENTS, count))


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()
    players: list[tuple[str, set[str]]] = []
    for name in ["Alice", "Bob", "Charlie", "Dylan"]:
        players.append((name, gen_player_achievements()))
    for name, achievements in players:
        print(f"Player {name}: {achievements}")
    print()

    distinct: set[str] = set()
    common: set[str] = set(ACHIEVEMENTS)
    for _, achievements in players:
        distinct = distinct.union(achievements)
        common = common.intersection(achievements)
    print(f"All distinct achievements: {distinct}")
    print()
    print(f"Common achievements: {common}")
    print()

    for name, achievements in players:
        only: set[str] = achievements
        for other_name, other in players:
            if other_name != name:
                only = only.difference(other)
        print(f"Only {name} has: {only}")
    print()

    for name, achievements in players:
        missing: set[str] = set(ACHIEVEMENTS).difference(achievements)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
