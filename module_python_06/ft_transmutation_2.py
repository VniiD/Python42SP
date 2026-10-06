import alchemy.transmutation.recipes as recipes


def main() -> None:
    print("=== Transmutation 2 ===")
    print("Import alchemy module only")
    result: str = recipes.lead_to_gold()
    print(f"Testing lead to gold: {result}")


if __name__ == "__main__":
    main()
