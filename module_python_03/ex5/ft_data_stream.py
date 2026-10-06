import random
from typing import Generator

PLAYERS: list[str] = [
                        "alice",
                        "bob",
                        "charlie",
                        "dylan"
                    ]
ACTIONS: list[str] = [
                        "run",
                        "eat",
                        "sleep",
                        "grab",
                        "move",
                        "climb",
                        "swim",
                        "use",
                        "release"
                    ]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        player: str = random.choice(PLAYERS)
        action: str = random.choice(ACTIONS)
        yield (player, action)


def consume_event(
    events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while events:
        index: int = random.randrange(len(events))
        event: tuple[str, str] = events.pop(index)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    stream: Generator[tuple[str, str], None, None] = gen_event()

    for i in range(1000):
        event: tuple[str, str] = next(stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    event_list: list[tuple[str, str]] = [next(stream) for _ in range(10)]
    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
