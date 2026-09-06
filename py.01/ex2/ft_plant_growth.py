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
    tomato = Plant()
    tomato.name = "Tomato"
    tomato.age_days = 45
    tomato.height = 80.0
    tomato.height_change = 0.0
    tomato.daily_growth = 0.8

    print("=== Garden Plant Growth ===")
    tomato.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        tomato.age()
        tomato.grow(i)
        tomato.show()
    print(f"Growth this week: {tomato.height_change}cm")


if __name__ == "__main__":
    main()
