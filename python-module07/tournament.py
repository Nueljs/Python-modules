from ex0 import FlameFactory, AquaFactory, Creature, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (NormalStrategy, AggressiveStrategy,
                 DefensiveStrategy, BattleStrategy)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1: CreatureFactory
            factory2: CreatureFactory
            strategy1: BattleStrategy
            strategy2: BattleStrategy
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            creature1: Creature = factory1.create_base()
            creature2: Creature = factory2.create_base()

            print("* Battle *")
            print(creature1.describe_creature())
            print("vs.")
            print(creature2.describe_creature())
            print(" now fight!")

            try:
                strategy1.act(creature1)
            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
                print()
                return

            try:
                strategy2.act(creature2)
            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
                print()
                return

            print()


def tournament() -> None:
    flame: FlameFactory = FlameFactory()
    aqua: AquaFactory = AquaFactory()
    heal: HealingCreatureFactory = HealingCreatureFactory()
    transform: TransformCreatureFactory = TransformCreatureFactory()
    normal: NormalStrategy = NormalStrategy()
    aggressive: AggressiveStrategy = AggressiveStrategy()
    defensive: DefensiveStrategy = DefensiveStrategy()

    print("Tournament 0 (basic)")
    opponents0: list[tuple[CreatureFactory, BattleStrategy]] = [
        (flame, normal),
        (heal, defensive)
    ]
    print("[ " + ", ".join(
        (
            name := factory.__class__.__name__
                     .replace("CreatureFactory", "")
                     .replace("Factory", ""),
            f"({name}+{strategy.__class__.__name__.replace('Strategy', '')})"
        )[1]
        for factory, strategy in opponents0
    ) + " ]")
    battle(opponents0)

    print("Tournament 1 (error)")
    opponents1: list[tuple[CreatureFactory, BattleStrategy]] = [
        (flame, aggressive),
        (heal, defensive)
    ]
    print("[ " + ", ".join(
        (
            name := factory.__class__.__name__
                     .replace("CreatureFactory", "")
                     .replace("Factory", ""),
            f"({name}+{strategy.__class__.__name__.replace('Strategy', '')})"
        )[1]
        for factory, strategy in opponents1
    ) + " ]")
    battle(opponents1)

    print("Tournament 2 (multiple)")
    opponents2: list[tuple[CreatureFactory, BattleStrategy]] = [
        (aqua, normal),
        (heal, defensive),
        (transform, aggressive)
    ]
    print("[ " + ", ".join(
        (
            name := factory.__class__.__name__
                     .replace("CreatureFactory", "")
                     .replace("Factory", ""),
            f"({name}+{strategy.__class__.__name__.replace('Strategy', '')})"
        )[1]
        for factory, strategy in opponents2
    ) + " ]")
    battle(opponents2)


if __name__ == "__main__":
    tournament()
