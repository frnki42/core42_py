import random


ACHIEVEMENTS = [
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


def gen_player_achievements() -> None:
    amount_avs = len(ACHIEVEMENTS)
    alice = set(random.sample(ACHIEVEMENTS, random.randint(0, amount_avs)))
    bob = set(random.sample(ACHIEVEMENTS, random.randint(0, amount_avs)))
    charlie = set(random.sample(ACHIEVEMENTS, random.randint(0, amount_avs)))
    dylan = set(random.sample(ACHIEVEMENTS, random.randint(0, amount_avs)))
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print(f"\nAll distinct achievements: {ACHIEVEMENTS}\n")


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    gen_player_achievements()


if __name__ == "__main__":
    main()
