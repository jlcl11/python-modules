#!/usr/bin/env python3

import sys

def parse_scores(args: list[str]) -> list[int]:
    scores: list[int] = []
    for arg in args:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return scores


def main() -> None:
    print("=== Player Score Analytics ===")
    scores: list[int] = parse_scores(sys.argv[1:])
    if len(scores) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...")
        return
    total: int = sum(scores)
    high: int = max(scores)
    low: int = min(scores)
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {total / len(scores)}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {high - low}")


if __name__ == "__main__":
    main()
