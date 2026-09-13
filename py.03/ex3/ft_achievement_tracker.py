# import random


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    alice = {"OG", "World Savior", "Master Explorer", "Unstoppable"}
    bob = {"OG", "Strategist", "World Savior", "Master Explorer"}
    print(alice)
    print(bob)
    print(alice & bob)
    print(alice | bob)
    print(alice ^ bob)
    print(alice - bob)
    print(bob - alice)


if __name__ == "__main__":
    main()
