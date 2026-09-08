class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_count} grow, "
                  f"{self._age_count} age, {self._show_count} show")

        def record_grow(self) -> None:
            self._grow_count += 1

        def record_age(self) -> None:
            self._age_count += 1

        def record_show(self) -> None:
            self._show_count += 1

    def __init__(self, name: str, height: float, age_days: int,
                 daily_growth: float) -> None:
        self._name = name
        self._height = 0.0
        self.set_height(height)
        self._height_change = 0.0
        self._age_days = 0
        self.set_age(age_days)
        self._daily_growth = daily_growth
        self._stats = self.Stats()

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0, 0.0)

    @staticmethod
    def is_older_than_year(age_days: int) -> bool:
        return age_days > 365

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age_days} days old")
        self._stats.record_show()

    def age(self, days: int = 1) -> None:
        self._age_days += days
        self._stats.record_age()

    def grow(self, light_level: int) -> None:
        if light_level > 3:
            increment = self._daily_growth
        else:
            increment = self._daily_growth / 2
        self._height = round(self._height + increment, 1)
        self._height_change = round(self._height_change + increment, 1)
        self._stats.record_grow()

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

    def get_stats(self) -> "Plant.Stats":
        return self._stats


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
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def display(self) -> None:
            super().display()
            print(f" {self._shade_count} shade")

        def record_shade(self) -> None:
            self._shade_count += 1

    def __init__(self, name: str, height: float, age_days: int,
                 daily_growth: float, trunk_diameter: float) -> None:
        super().__init__(name, height, age_days, daily_growth)
        self._stats: Tree.Stats = Tree.Stats()
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height}cm long and {self._trunk_diameter}cm wide.")
        self._stats.record_shade()


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

    def age(self, days: int = 1) -> None:
        super().age(days)
        self._nutritional_value += days

    def grow(self, light_level: int) -> None:
        super().grow(light_level)
        self._nutritional_value += 1


class Seed(Flower):
    def __init__(self, name: str, height: float, age_days: int,
                 daily_growth: float, color: str) -> None:
        super().__init__(name, height, age_days, daily_growth, color)
        self._seeds = 0

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42


def show_stats(plant: Plant) -> None:
    plant.get_stats().display()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, 8, "red")
    rose.show()
    print("[statistics for Rose]")
    show_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(42)
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    show_stats(rose)
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 0.8, 5.0)
    oak.show()
    print("[statistics for Oak]")
    show_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    show_stats(oak)
    print()
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, 30.0, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(42)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    show_stats(sunflower)
    print()
    print("=== Anonymous")
    anon = Plant.anonymous()
    anon.show()
    print("[statistics for Unknown plant]")
    show_stats(anon)


if __name__ == "__main__":
    main()
