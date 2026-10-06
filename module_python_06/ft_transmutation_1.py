from alchemy import transmutation


def main() -> None:
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    result: str = transmutation.lead_to_gold()  # type: ignore[attr-defined]
    print(f"Testing lead to gold: {result}")


if __name__ == "__main__":
    main()
