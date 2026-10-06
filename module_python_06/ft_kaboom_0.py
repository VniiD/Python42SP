from alchemy.grimoire import light_spell_record


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    res: str = light_spell_record("Fantasy", "Earth, wind and fire")
    print(f"Testing record light spell: {res}")


if __name__ == "__main__":
    main()
