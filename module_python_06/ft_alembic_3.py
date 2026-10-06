from alchemy.elements import create_air


def main() -> None:
    print("=== Alembic 3 ===")
    print("Access alchemy/elements.py using 'from ... import ...' structure")
    result: str = create_air()
    print(f"Testing create_air: {result}")


if __name__ == "__main__":
    main()
