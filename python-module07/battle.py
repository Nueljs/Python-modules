from ex0 import FlameFactory, AquaFactory, Creature, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    base: Creature = factory.create_base()
    evolved: Creature = factory.create_evolved()

    print("Testing factory")
    print(base.describe_creature())
    print(base.attack())
    print(evolved.describe_creature())
    print(evolved.attack())


def battle(flame_factory: CreatureFactory,
           aqua_factory: CreatureFactory) -> None:
    flame: Creature = flame_factory.create_base()
    aqua: Creature = aqua_factory.create_base()

    print("Testing battle")
    print(flame.describe_creature())
    print(" vs.")
    print(aqua.describe_creature())
    print(" fight!")
    print(flame.attack())
    print(aqua.attack())


if __name__ == "__main__":
    fire_factory: FlameFactory = FlameFactory()
    aqua_factory: AquaFactory = AquaFactory()
    test_factory(fire_factory)
    print("")
    test_factory(aqua_factory)
    print("")
    battle(fire_factory, aqua_factory)
