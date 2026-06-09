from ex1.factories import (
    HealingCreatureFactory,
    TransformCreatureFactory
)

from ex1.capabilities import (
    HealCapability,
    TransformCapability
)


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    print("base:")

    healing_factory = HealingCreatureFactory()
    base = healing_factory.create_base()
    evolved = healing_factory.create_evolved()

    assert isinstance(base, HealCapability)
    assert isinstance(evolved, HealCapability)

    print(base.describe())
    print(base.attack())
    print(base.heal())

    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())
    print()

    print("Testing Creature with transform capability")
    print("base:")

    transform_factory = TransformCreatureFactory()
    base = transform_factory.create_base()
    evolved = transform_factory.create_evolved()

    assert isinstance(base, TransformCapability)
    assert isinstance(evolved, TransformCapability)

    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())
