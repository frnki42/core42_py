import random
import typing


PLAYER_NAMES = [
        "bob",
        "alice",
        "dylan",
        "charlie",
        ]
ACTION_NAMES = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release",
        ]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(PLAYER_NAMES)
        action = random.choice(ACTION_NAMES)
        yield (name, action)


def main() -> None:
    print("=== Game Data Stream Processor ===")
    events = gen_event()
    for i in range(1000):
        name, action = next(events)
        print(f"Event {i}: Player {name} did action {action}")


if __name__ == "__main__":
    main()
