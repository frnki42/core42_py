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


class Flower(Plant):
    def __init__(self, name: str, height: float, age_days: int,
                 daily_growth: float, color: str) -> None:
        super().__init__(name, height, age_days, daily_growth)
        self._color = color
        self._bloomed = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._bloomed:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")

    def bloom(self) -> None:
        self._bloomed = True


class Tree(Plant):
    def __init__(self, name: str, height: float, age_days: int,
                 daily_growth: float, trunk_diameter: float) -> None:
        super().__init__(name, height, age_days, daily_growth)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height}cm long and {self._trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age_days: int,
                 daily_growth: float, harvest_season: str) -> None:
        super().__init__(name, height, age_days, daily_growth)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1

    def grow(self, light_level: int) -> None:
        super().grow(light_level)
        self._nutritional_value += 1


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, 0.4, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, 0.2, 5.0)
    tree.show()
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    print()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, 2.1, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow(42)
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    main()
