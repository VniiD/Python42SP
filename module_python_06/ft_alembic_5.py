from alchemy import create_air


def main() -> None:
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import ...'")
    result: str = create_air()
    print(f"Testing create_air: {result}")


if __name__ == "__main__":
    main()
