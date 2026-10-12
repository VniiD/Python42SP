def main() -> None:
    print("Kaboom 1")
    print(
        "Access to alchemy/grimoire/dark_spellbook.py "
        "directly"
    )
    print("Test import now THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    try:
        from alchemy.grimoire.dark_spellbook import (  # noqa: F401
            dark_spell_record,
        )
    except ImportError as e:
        print(f"ImportError: {e}")


if __name__ == "__main__":
    main()
