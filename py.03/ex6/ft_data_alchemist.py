import random


MIN_SCORE = 0
MAX_SCORE = 1000
PLAYER_NAMES = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
        ]


def main() -> None:
    print("=== Game Data Alchemist ===\n")
    capitalized = [name.capitalize() for name in PLAYER_NAMES]
    already_capitalized = [name for name in PLAYER_NAMES if name.istitle()]
    print(f"Initial list of players: {PLAYER_NAMES}")
    print(f"New list with all names capitalized: {capitalized}")
    print(f"New list of capitalized names only: {already_capitalized}\n")
    score_dict = {name: random.randint(MIN_SCORE, MAX_SCORE)
                  for name in capitalized}
    print(f"Score dict: {score_dict}")
    average = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {round(average, 2)}")
    high_scores = {name: score for name, score in score_dict.items()
                   if score > average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
