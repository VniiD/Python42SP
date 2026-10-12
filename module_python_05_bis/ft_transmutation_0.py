from alchemy.transmutation.recipes import (
    lead_to_gold,
)


def main() -> None:
    print("Transmutation 0")
    print(
        "Using file "
        "alchemy/transmutation/recipes.py directly"
    )
    transmutation_res: str = lead_to_gold()
    print(f"Testing lead to gold: {transmutation_res}")


if __name__ == "__main__":
    main()
