from ex0.creature import Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def test_healing_factory() -> None:
    print("Testing Creature with healing capability")
    factory = HealingCreatureFactory()

    print("base:")
    base: Creature = factory.create_base()
    print(base.describe())
    print(base.attack())
    if isinstance(base, HealCapability):
        print(base.heal())

    print("evolved:")
    evolved: Creature = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, HealCapability):
        print(evolved.heal())


def test_transform_factory() -> None:
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()

    print("base:")
    base: Creature = factory.create_base()
    print(base.describe())
    print(base.attack())
    if isinstance(base, TransformCapability):
        print(base.transform())
        print(base.attack())
        print(base.revert())

    print("evolved:")
    evolved: Creature = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, TransformCapability):
        print(evolved.transform())
        print(evolved.attack())
        print(evolved.revert())


def main() -> None:
    test_healing_factory()
    test_transform_factory()


if __name__ == "__main__":
    main()
