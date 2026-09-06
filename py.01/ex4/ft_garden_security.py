class Plant:
    def __init__(self, name: str, height: float, age_days: int,
                 daily_growth: float) -> None:
        self._name = name
        self._height = 0.0
        self.set_height(height)
        self._height_change = 0.0
        self._age_days = 0
        self.set_age(age_days)
        self._daily_growth = daily_growth
        print("Plant created: ", end="")
        self.show()

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age_days} days old")

    def age(self) -> None:
        self._age_days += 1

    def grow(self, light_level: int) -> None:
        if light_level > 3:
            increment = self._daily_growth
        else:
            increment = self._daily_growth / 2
        self._height = round(self._height + increment, 1)
        self._height_change = round(self._height_change + increment, 1)

    def set_height(self, new_height: float) -> bool:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            return False
        self._height = float(new_height)
        return True

    def get_height(self) -> float:
        return self._height

    def set_age(self, new_age: int) -> bool:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            return False
        self._age_days = new_age
        return True

    def get_age(self) -> int:
        return self._age_days


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10, 0.4)
    print()
    if rose.set_height(25.0):
        print(f"Height updated: {rose.get_height():.0f}cm")
    if rose.set_age(30):
        print(f"Age updated: {rose.get_age()} days")
    print()
    if not rose.set_height(-42):
        print("Height update rejected")
    if not rose.set_age(-42):
        print("Age update rejected")
    print()
    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
