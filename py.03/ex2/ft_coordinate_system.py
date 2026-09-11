import math


PROMPT = "Enter new coordinates as floats in format 'x,y,z': "
ORIGIN = (0.0, 0.0, 0.0)


def get_distance(a: tuple[float, float, float],
                 b: tuple[float, float, float]) -> float:
    x1, y1, z1 = a
    x2, y2, z2 = b
    result = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return result


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            user_input = input(PROMPT)
            values = user_input.split(",")
            _, _, _ = values
        except ValueError:
            print("Invalid syntax")
            continue
        try:
            coords = []
            for value in values:
                coords.append(float(value))
            x, y, z = coords
            return (x, y, z)
        except ValueError as e:
            print(f"Error on parameter '{value}': {e}")


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first_set = get_player_pos()
    print(f"Got a first tuple: {first_set}")
    x, y, z = first_set
    print(f"It includes: X={x}, Y={y}, Z={z}")
    distance = round(get_distance(first_set, ORIGIN), 4)
    print(f"Distance to center: {distance}")
    print("\nGet a second set of coordinates")
    second_set = get_player_pos()
    distance = round(get_distance(first_set, second_set), 4)
    print(f"Distance between the 2 sets of coordinates: {distance}")


if __name__ == "__main__":
    main()
