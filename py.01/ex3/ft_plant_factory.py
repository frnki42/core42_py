class Plant:
    name: str
    height: float
    age_days: int
    daily_growth: float
    height_change: float

    def __init__(self, name: str, height: float, age_days: int,
                 daily_growth: float) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days
        self.daily_growth = daily_growth
        self.height_change = 0.0
        print("Created: ", end="")
        self.show()

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")

    def age(self) -> None:
        self.age_days += 1

    def grow(self, light_level: int) -> None:
        if light_level > 3:
            increment = self.daily_growth
        else:
            increment = self.daily_growth / 2
        self.height = round(self.height + increment, 1)
        self.height_change = round(self.height_change + increment, 1)


def main() -> None:
    print("=== Plant Factory Output ===")
    Plant("Rose", 25.0, 30, 0.4)
    Plant("Oak", 200.0, 365, 0.2)
    Plant("Cactus", 5.0, 90, 0.2)
    Plant("Sunflower", 80.0, 45, 0.6)
    Plant("Fern", 15.0, 120, 0.8)


if __name__ == "__main__":
    main()
