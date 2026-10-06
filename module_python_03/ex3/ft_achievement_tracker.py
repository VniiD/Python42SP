import random

ACHIEVEMENTS: list[str] = [
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Unstoppable",
    "Speed Runner",
    "Survivor",
    "Treasure Hunter",
    "First Steps",
    "Sharp Mind",
    "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    count: int = random.randint(5, 9)
    return set(random.sample(ACHIEVEMENTS, count))


def main() -> None:
    print("=== Achievement Tracker System ===")

    players: dict[str, set[str]] = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    for name, achs in players.items():
        print(f"Player {name}: {achs}")

    all_distinct: set[str] = set().union(*players.values())
    print(f"All distinct achievements: {all_distinct}")

    common_achs: set[str] = set(ACHIEVEMENTS).intersection(*players.values())
    print(f"Common achievements: {common_achs}")

    for name, achs in players.items():
        others: set[str] = set().union(
            *[p_achs for p_name, p_achs in players.items() if p_name != name]
        )
        only_player: set[str] = achs.difference(others)
        print(f"Only {name} has: {only_player}")

    for name, achs in players.items():
        missing: set[str] = all_distinct.difference(achs)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
