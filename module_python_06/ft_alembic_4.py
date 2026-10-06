import alchemy


def main() -> None:
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    result: str = alchemy.create_air()  # type: ignore[attr-defined]
    print(f"Testing create_air: {result}")
    print("\nNow show that not all functions can be reached")
    print("This will raise an exception!")
    print("Testing the hidden create_earth: ")
    print(alchemy.create_earth())  # type: ignore[attr-defined]


if __name__ == "__main__":
    main()
