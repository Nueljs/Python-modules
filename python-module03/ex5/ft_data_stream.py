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


def ft_data_stream() -> None:
    my_generator: typing.Generator[tuple[str, str], None, None] = gen_event()
    event: tuple[str, str] = next(my_generator)
