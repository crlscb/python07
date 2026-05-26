from abc import ABC, abstractmethod

class Creature(ABC):
    def __init__(self, name: str, type_creature: str) -> None:
        self._name = name
        self._type_creature = type_creature
    
    @abstractmethod
    def attack(self) -> str:
        pass
    
    def describe(self) -> str:
        return f"{self._name} is a {self._type_creature} type Creature"

class Flameling(Creature):
    def __init__(self):
        super().__init__("Flameling", "Fire")
    
    def attack(self) -> str:
        return f"{self._name} uses Ember!"

class Pyrodon(Creature):
    def __init__(self):
        super().__init__("Pyrodon", "Fire/Flying")
    
    def attack(self) -> str:
        return f"{self._name} uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self):
        super().__init__("Aquabub", "Water")
    
    def attack(self) -> str:
        return f"{self._name} uses Water Gun!"

class Torragon(Creature):
    def __init__(self):
        super().__init__("Torragon", "Water")
    
    def attack(self) -> str:
        return f"{self._name} uses Hydro Pump!"


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass

class FlameFactory(CreatureFactory):
    
    def create_base(self) -> Creature:
        return Flameling()
    
    def create_evolved(self) -> Creature:
        return Pyrodon()

class AquaFactory(CreatureFactory):
    
    def create_base(self) -> Creature:
        return Aquabub()
    
    def create_evolved(self) -> Creature:
        return Torragon()

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

