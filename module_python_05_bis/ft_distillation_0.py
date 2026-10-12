from alchemy.potions import (
    healing_potion,
    strength_potion,
)


def main() -> None:
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    strength_res: str = strength_potion()
    print(
        "Testing strength_potion: "
        f"{strength_res}"
    )
    healing_res: str = healing_potion()
    print(
        "Testing healing_potion: "
        f"{healing_res}"
    )


if __name__ == "__main__":
    main()
