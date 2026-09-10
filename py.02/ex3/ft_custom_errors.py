MIN_WATER_LEVEL = 66


class GardenError(Exception):
    default_message = "Unknown garden error"

    def __init__(self, message: str | None = None) -> None:
        if message is None:
            message = self.default_message
        super().__init__(message)


class PlantError(GardenError):
    default_message = "Unknown plant error"


class WaterError(GardenError):
    default_message = "Unknown water error"


def check_plant(plant_name: str, wilting: bool) -> None:
    if wilting:
        raise PlantError(f"The {plant_name} plant is wilting!")


def check_water(water_level: int) -> None:
    if water_level < MIN_WATER_LEVEL:
        raise WaterError("Not enough water in the tank!")


def test_plant_error() -> None:
    try:
        check_plant("tomato", True)
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")


def test_water_error() -> None:
    try:
        check_water(42)
    except WaterError as e:
        print(f"Caught {e.__class__.__name__}: {e}")


def test_garden_errors() -> None:
    try:
        check_plant("tomato", True)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water(42)
    except GardenError as e:
        print(f"Caught GardenError: {e}")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    test_plant_error()
    print("\nTesting WaterError...")
    test_water_error()
    print("\nTesting catching all garden errors...")
    test_garden_errors()
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
