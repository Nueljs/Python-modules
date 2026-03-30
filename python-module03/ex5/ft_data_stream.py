import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    names: list = ["alice", "bob", "dylan", "charlie"]
    actions: list = [
        "run", "eat", "sleep", "grab", "move", "climb", "swim"
        ]
    while True:
        event: tuple = (random.choice(names), random.choice(actions))
        yield (event)


def consume_event(events: list) -> typing.Generator[tuple[str, str],
                                                    None, None]:
    while len(events) > 0:
        i: int = random.randrange(len(events))
        event = events[i]
        events[:] = events[:i] + events[i + 1:]
        yield event


def ft_data_stream() -> None:
    my_generator: typing.Generator[tuple[str, str], None, None] = gen_event()
    for i in range(1000):
        event: tuple[str, str] = next(my_generator)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    ten_events: list[tuple[str, str]] = [next(my_generator) for _ in range(10)]
    print(f"Built list of 10 events: {ten_events}")
    extract_event: typing.Generator[
        tuple[str, str], None, None] = consume_event(ten_events)
    for event in extract_event:
        print(f"Got event from list: {event}")
        print(f"Remain in list: {ten_events}")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    ft_data_stream()
