from ex1 import (HealingCreatureFactory, TransformCreatureFactory,
                 HealCapability, TransformCapability)
from ex0 import Creature
from typing import cast


def ft_capacitor() -> None:
    healing_base: Creature = HealingCreatureFactory().create_base()
    healing_base2: HealCapability = cast(HealCapability, healing_base)
    healing_evo: Creature = HealingCreatureFactory().create_evolved()
    healing_evo2: HealCapability = cast(HealCapability, healing_evo)
    transform_base: Creature = TransformCreatureFactory().create_base()
    transform_base2: TransformCapability = cast(TransformCapability,
                                                transform_base)
    transform_evo: Creature = TransformCreatureFactory().create_evolved()
    transform_evo2: TransformCapability = cast(TransformCapability,
                                               transform_evo)
    print("Testing Creature with healing capability")
    print(" base:")
    print(healing_base.describe_creature())
    print(healing_base.attack())
    print(healing_base2.heal())
    print(" evolved:")
    print(healing_evo.describe_creature())
    print(healing_evo.attack())
    print(healing_evo2.heal())

    print("")
    print("Testing Creature with transform capability")
    print(" base:")
    print(transform_base.describe_creature())
    print(transform_base.attack())
    print(transform_base2.transform())
    print(transform_base.attack())
    print(transform_base2.revert())
    print(" evolved:")
    print(transform_evo.describe_creature())
    print(transform_evo.attack())
    print(transform_evo2.transform())
    print(transform_evo.attack())
    print(transform_evo2.revert())


if __name__ == "__main__":
    ft_capacitor()
