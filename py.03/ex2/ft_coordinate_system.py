import math


def get_player_pos() -> tuple[float, float, float]:
    try:
        pos = input(
                "Enter new coordinates as floats in format 'x,y,z': "
                ).split(",")
    except ValueError as e:
        print(f"Error on pa{e}")
    return (float(pos[0]), float(pos[1]), float(pos[2]))


def main() -> None:
        pos = get_player_pos()


if __name__ == "__main__":
    main()
