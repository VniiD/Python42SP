from elements import create_water


def main() -> None:
    print("=== Alembic 1 ===")
    print("Using 'from ... import ...' structure to access elements.py")
    result: str = create_water()
    print(f"Testing create_water: {result}")


if __name__ == "__main__":
    main()
