from alchemy.potions import healing_potion, strength_potion


def main() -> None:
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    str_potion: str = strength_potion()
    print(f"Testing strength_potion: {str_potion}")
    heal_potion: str = healing_potion()
    print(f"Testing healing_potion: {heal_potion}")


if __name__ == "__main__":
    main()
