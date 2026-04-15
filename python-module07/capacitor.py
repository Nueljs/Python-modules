from ex1 import Creature, HealingCreatureFactory, TransformCreatureFactory


def ft_capacitor() -> None:
    healing_base: Creature = HealingCreatureFactory().create_base()
    healing_evo: Creature = HealingCreatureFactory().create_evolved()
    transform_base: Creature = TransformCreatureFactory().create_base()
    transform_evo: Creature = TransformCreatureFactory().create_evolved()
    print("Testing Creature with healing capability")
    print(" base:")
    print(healing_base.describe_creature())
    print(healing_base.attack())
    print(healing_base)
    print(" evolved:")
    print(healing_evo.describe_creature())
    print(healing_evo.attack())


if __name__ == "__main__":
    ft_capacitor()