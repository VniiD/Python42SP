import alchemy


def main() -> None:
    print("=== Alembic 1 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    result: str = alchemy.create_air()
    print(f"Testing create_air: {result}")

    print("\nNow show that not all functions can be reached")
    print("This will raise an exception!")
    try:
        alchemy.create_earth()  # type: ignore[attr-defined]
    except AttributeError as e:
        print("Testing the hidden create_earth: "
              "Traceback (most recent call last):")
        print('File "ft_alembic_1.py", line 12, in <module>')
        print('    print(f"(alchemy.create_earth() ")')
        print(f"AttributeError: {e}")


if __name__ == "__main__":
    main()
