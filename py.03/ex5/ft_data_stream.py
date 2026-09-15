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


def consume_event(events: list[tuple[str, str]]
                  ) -> typing.Generator[tuple[str, str], None, None]:
    while events:
        index = random.randrange(len(events))
        yield events.pop(index)


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(PLAYER_NAMES)
        action = random.choice(ACTION_NAMES)
        yield (name, action)


def main() -> None:
    print("=== Game Data Stream Processor ===")
    event_generator = gen_event()
    for i in range(1000):
        name, action = next(event_generator)
        print(f"Event {i}: Player {name} did action {action}")
    events = []
    for _ in range(10):
        events.append(next(event_generator))
    print(f"Built list of 10 events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
