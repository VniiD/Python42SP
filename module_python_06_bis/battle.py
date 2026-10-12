from ex3 import (
    CreatureFactory,
    FlameFactory,
    TransformCreatureFactory,
)


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(
    f1: CreatureFactory, f2: CreatureFactory
) -> None:
    c1 = f1.create_base()
    c2 = f2.create_base()
    print(c1.describe())
    print("VS.")
    print(c2.describe())
    print("fight!")
    print(c1.attack())
    print(c2.attack())


if __name__ == "__main__":
    print("Testing factory")
    flame_factory = FlameFactory()
    test_factory(flame_factory)

    print("Testing factory")
    trans_factory = TransformCreatureFactory()
    test_factory(trans_factory)

    print("Testing battle")
    test_battle(flame_factory, trans_factory)
