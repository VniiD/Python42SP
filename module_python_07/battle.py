from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    """Testa a criação, descrição e ataque das criaturas de uma fábrica."""
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    """Simula um confronto entre duas criaturas base de fábricas distintas."""
    print("Testing battle")
    c1 = factory1.create_base()
    c2 = factory2.create_base()

    print(c1.describe())
    print("VS.")
    print(c2.describe())
    print("fight!")
    print(c1.attack())
    print(c2.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    test_factory(flame_factory)
    test_factory(aqua_factory)
    test_battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
