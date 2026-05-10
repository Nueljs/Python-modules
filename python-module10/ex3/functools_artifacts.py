from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    operations: dict = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda a, b: max(a, b),
        "min": lambda a, b: min(a, b)
    }

    if not spells:
        return 0
    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")
    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, power=50, element="fire"),
        "ice": partial(base_enchantment, power=50, element="ice"),
        "lightning": partial(base_enchantment, power=50, element="lightning")
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return (memoized_fibonacci(n-1) + memoized_fibonacci(n-2))


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def spell(value) -> str:
        return "Unknown spell type"

    @spell.register(int)
    def _(value: int) -> str:
        return f"Damage spell: {value} damage"

    @spell.register(str)
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    @spell.register(list)
    def _(value: list) -> str:
        return f"Multi-cast: {len(value)} spells"
    return spell


if __name__ == "__main__":
    spell_powers: list[int] = [10, 20, 30, 40]
    operations: list[str] = ['add', 'multiply', 'max', 'min']
    fibonacci_tests: list[int] = [14, 12, 10]
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spell_powers, operations[0])}")
    print(f"Product: {spell_reducer(spell_powers, operations[1])}")
    print(f"Max: {spell_reducer(spell_powers, operations[2])}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    spell: Callable = spell_dispatcher()
    print(spell(42))
    print(spell("fireball"))
    print(spell(["ice", "fire", "lightning"]))
    print(spell(("42", 42)))
