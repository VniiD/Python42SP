import alchemy


def main() -> None:
    print("=== Distillation 1 ===")
    print("Using 'import alchemy' structure to access potions")
    str_potion: str = (
        alchemy.potions.strength_potion()  # type: ignore[attr-defined]
    )
    print(f"Testing strength_potion: {str_potion}")
    heal_potion: str = alchemy.heal()  # type: ignore[attr-defined]
    print(f"Testing heal alias: {heal_potion}")


if __name__ == "__main__":
    main()
