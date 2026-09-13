import random


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
    avs = set(random.sample(AVS, random.randint(MIN_AVS, MAX_AVS)))
    return avs


def main() -> None:
    amount_avs = len(AVS)
    print("=== Achievement Tracker System ===\n")
    alice = gen_player_achievements()
    print(f"Player Alice: {alice}")
    bob = gen_player_achievements()
    print(f"Player Bob: {bob}")
    print(f"\nAll distinct achievements: {AVS}\n")

if __name__ == "__main__":
    main()
