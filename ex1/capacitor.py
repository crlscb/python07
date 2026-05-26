from abc import ABC, abstractmethod
from ex0.battle import Creature, CreatureFactory

class HealCapability(ABC):

    @abstractmethod
    def heal(self):
        pass

class TransformCapability(ABC):
    
    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass

class Sproutling(Creature, HealCapability):

    def __init__(self):
        super().__init__("Sproutling", "Grass")
    
    def attack(self) -> str:
        return f"{self._name} uses Vine Whip!"
    
    def heal(self) -> str:
        return f"{self._name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):

    def __init__(self):
        super().__init__("Bloomelle", "Grass/Fairy")
    
    def attack(self) -> str:
        return f"{self._name} uses Petal Dance!"
    
    def heal(self) -> str:
        return f"{self._name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Shiftling", "Normal")
        self._transformed = False
    
    def attack(self) -> str:
        if self._transformed:
            return f"{self._name} performs a boosted strike!"
        
        return f"{self._name} attacks normally."
    
    def transform(self) -> str:
        self._transformed = True
        return f"{self._name} shifts into a sharper form!"
    
    def revert(self) -> str:
        self._transformed = False
        return f"{self._name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Morphagon", "Normal/Dragon")
        self._transformed = False
    
    def attack(self) -> str:
        if self._transformed:
            return f"{self._name} unleashes a devastating morph strike!"
        
        return f"{self._name} attacks normally."
    
    def transform(self) -> str:
        self._transformed = True
        return f"{self._name} morphs into a dragonic battle form!"
    
    def revert(self) -> str:
        self._transformed = False
        return f"{self._name} stabilizes its form."

class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Sproutling()
    
    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Shiftling()
    
    def create_evolved(self) -> Creature:
        return Morphagon()

if __name__ == "__main__":
    print("Testing Creature with healing capability")
    print("base:")

    healing_factory = HealingCreatureFactory()
    base = healing_factory.create_base()
    evolved = healing_factory.create_evolved()
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
