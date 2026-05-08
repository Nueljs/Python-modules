from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        result1: str = spell1(target, power)
        result2: str = spell2(target, power)
        return (result1, result2)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        result: list = []
        for spell in spells:
            result.append(spell(target, power))
        return result
    return sequence


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    test_values = [5, 7, 7]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    print("Testing spell combiner...")
    combined: Callable = spell_combiner(fireball, heal)
    result = combined(test_targets[0], test_values[0])
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("Testing power amplifier...")
    original_power: int = 10
    amplified: Callable = power_amplifier(fireball, 3)
    result = amplified(test_targets[0], original_power)
    print(f"Original: {original_power}, Amplified: {original_power * 3}")

    print("Testing conditional caster...")
    is_powerfull: Callable = lambda target, power: power > 50
    safe_fireball = conditional_caster(is_powerfull, fireball)
    result1: str = safe_fireball(test_targets[0], 30)
    result2: str = safe_fireball(test_targets[0], 80)
    print(result1)
    print(result2)

    print("Testing spell sequence...")
    spells: list[Callable] = [
        fireball,
        heal
    ]
    sequence = spell_sequence(spells)
    results = sequence(test_targets[1], test_values[2])
    for result in results:
        print(result)