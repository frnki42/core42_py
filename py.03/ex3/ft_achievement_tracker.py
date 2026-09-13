import random

PLAYER_NAMES = [
    "Alice",
    "Bob",
    "Charlie",
    "Dylan",
    ]
AVS = [
    "Crafting Genius",
    "Strategist",
    "World Savior",
    "Speed Runner",
    "Survivor",
    "Master Explorer",
    "Treasure Hunter",
    "Unstoppable",
    "First Steps",
    "Collector Supreme",
    "Untouchable",
    "Sharp Mind",
    "Boss Slayer",
    ]
MIN_AVS = 5
MAX_AVS = 9


def gen_player_achievements() -> set[str]:
    random_avs = set(random.sample(AVS, random.randint(MIN_AVS, MAX_AVS)))
    return random_avs


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    players = []
    for name in PLAYER_NAMES:
        players.append((name, gen_player_achievements()))
    for name, achievements in players:
        print(f"Player {name}: {achievements}")
    all_avs = []
    for _, achievement in players:
        all_avs.append(achievement)
    print(f"\nAll distinct achievements: {all_avs[0].union(*all_avs[1:])}\n")
    print(f"Common achievements: {all_avs[0].intersection(*all_avs[1:])}\n")
    for name, avs in players:
        others = []
        for other_name, other_avs in players:
            if other_name != name:
                others.append(other_avs)
        print(f"Only {name} has: {avs.difference(*others)}")
    catalogue = set(AVS)
    print()
    for name, avs in players:
        print(f"{name} is missing: {catalogue.difference(avs)}")


if __name__ == "__main__":
    main()
