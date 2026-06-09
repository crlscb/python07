from ex1.factories import (
    HealingCreatureFactory,
    TransformCreatureFactory
)

from .strategies import (
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    ABattleStrategy
)

from ex0.battle import (
    FlameFactory,
    AquaFactory,
    CreatureFactory
)


def battle(opponents: list[tuple[CreatureFactory, ABattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")

    # selecciono dos oponentes de mi lista
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            creature1 = factory1.create_base()
            creature2 = factory2.create_base()

            print("* Battle *")
            print(
                f"{creature1.describe()} \n"
                f" vs. \n"
                f"{creature2.describe()} \n"
                f" now fight!"
            )

            try:
                strategy1.act(creature1)
                strategy2.act(creature2)

            except Exception as error:
                print(
                    f"Battle error, aborting tournament: {error}"
                )
                return


if __name__ == "__main__":
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")

    opponents1 = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    battle(opponents1)
    print()

    print("Torunament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")

    opponents2 = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    battle(opponents2)
    print()

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")

    opponents3 = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ]
    battle(opponents3)
