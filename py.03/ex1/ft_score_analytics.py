import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    scores = []
    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if not scores:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
        return
    player_count = len(scores)
    score_total = sum(scores)
    score_average = score_total / player_count
    score_max = max(scores)
    score_min = min(scores)
    print(f"Scores processed: {scores}")
    print(f"Total players: {player_count}")
    print(f"Total score: {score_total}")
    print(f"Average score: {score_average}")
    print(f"High score: {score_max}")
    print(f"Low score: {score_min}")
    print(f"Score range: {score_max - score_min}")


if __name__ == "__main__":
    main()
