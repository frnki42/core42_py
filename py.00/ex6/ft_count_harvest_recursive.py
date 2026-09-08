def count_harvest(start: int, days: int) -> None:
    if start <= days:
        print(f"Day {start}")
        count_harvest(start + 1, days)


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    count_harvest(1, days)
    print("Harvest time!")
