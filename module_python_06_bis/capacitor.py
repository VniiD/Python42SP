from ex3 import TransformCreatureFactory
from ex3.creatures import Creature


def test_transform(entity: Creature) -> None:
    print(entity.describe())
    print(entity.attack())
    if hasattr(entity, "transform") and hasattr(
        entity, "revert"
    ):
        print(entity.transform())  # type: ignore
        print(entity.attack())
        print(entity.revert())  # type: ignore


if __name__ == "__main__":
    print(
        "Testing Creature with transform capability"
    )
    factory = TransformCreatureFactory()
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("base:")
    test_transform(base)

    print("evolved:")
    test_transform(evolved)
