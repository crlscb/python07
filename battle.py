from ex0.factories import (
    CreatureFactory,
    FlameFactory,
    AquaFactory,
)


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()

    print(
        f"{creature1.describe()} \n"
        f" vs. \n"
        f"{creature2.describe()} \n"
        f" fight!"
    )

    print(creature1.attack())
    print(creature2.attack())


if __name__ == "__main__":

    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    print("Testing factory")
    test_factory(flame_factory)
    print()

    print("Testing factory")
    test_factory(aqua_factory)
    print()

    print("Testing battle")
    battle(flame_factory, aqua_factory)
