class Plant:
    name: str
    age_days: int
    height: float
    height_change: float
    daily_growth: float

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
    rose = Plant()
    rose.name = "Rose"
    rose.age_days = 30
    rose.height = 25.0
    rose.height_change = 0.0
    rose.daily_growth = 0.8

    print("=== Garden Plant Growth ===")
    rose.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.age()
        rose.grow(42)
        rose.show()
    print(f"Growth this week: {rose.height_change}cm")


if __name__ == "__main__":
    main()
