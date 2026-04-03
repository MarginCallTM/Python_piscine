from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def test_healing_factory(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    base = factory.create_base()
    assert isinstance(base, HealCapability)
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())
    evolved = factory.create_evolved()
    print(" evolved:")
    assert isinstance(evolved, HealCapability)
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transform_factory(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    base = factory.create_base()
    assert isinstance(base, TransformCapability)
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print(" evolved:")
    evolved = factory.create_evolved()
    assert isinstance(evolved, TransformCapability)
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    sproutling = HealingCreatureFactory()
    shiftling = TransformCreatureFactory()

    test_healing_factory(sproutling)
    print()
    test_transform_factory(shiftling)
