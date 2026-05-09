from typing import Callable


def mage_counter() -> Callable:
    counter: int = 0

    def count() -> int:
        nonlocal counter
        counter += 1
        return counter
    return count


def spell_accumulator(initial_power: int) -> Callable:
    power: int = initial_power

    def accumulator(ammount: int) -> int:
        nonlocal power
        power += ammount
        return power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str) -> str:
        return enchantment_type + " " + item_name
    return enchant


def memory_vault() -> dict[str, Callable]:
    memory: dict = {}

    def store(key: int, value: str) -> None:
        memory[key] = value

    def recall(key: int) -> str:
        if key in memory:
            return memory[key]
        return "Memory not found"
    return {'store': store, 'recall': recall}


if __name__ == "__main__":
    counter_a: Callable = mage_counter()
    counter_b: Callable = mage_counter()
    print("Testing mage counter...")
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    acc: Callable = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    print(f"Base 100, add 30: {acc(30)}")

    print("\nTesting enchantment factory...")
    flaming: Callable = enchantment_factory("Flaming")
    frozen: Callable = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault: dict[str, Callable] = memory_vault()
    vault['store']('secret', 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
