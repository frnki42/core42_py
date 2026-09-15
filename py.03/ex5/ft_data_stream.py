import typing               # next(), range(), len(), print(), typing.Generator
import random               # random.*


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
        "run",
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

    a = gen_event()
    name, action = next(a)
    print(name)
    print(action)

if __name__ == "__main__":
    main()
