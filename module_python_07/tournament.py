from typing import List, Tuple
from ex0.factory import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    DefensiveStrategy,
    AggressiveStrategy,
    InvalidStrategyError,
)


Opponent = Tuple[CreatureFactory, BattleStrategy]


def run_tournament(title: str, opponents: List[Opponent]) -> None:
    """Run a single tournament match between multiple opponents."""
    print(title)
    formatted_opponents = [
        f"({f.__class__.__name__}+{s.__class__.__name__})"
        for f, s in opponents
    ]
    print(f"[{', '.join(formatted_opponents)}]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    # Match each opponent against every other opponent once (round-robin style)
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            f1, s1 = opponents[i]
            f2, s2 = opponents[j]

            c1 = f1.create_base()
            c2 = f2.create_base()

            # Check validity of both strategies before starting battle
            if not s1.is_valid(c1):
                print(
                    f"* Battle\n"
                    f"{c1.describe()}\n"
                    f"VS.\n"
                    f"{c2.describe()}\n"
                    f"now fight!"
                    )
                print(
                    f"Battle error, aborting tournament: Invalid Creature "
                    f"'{c1.name}' for this aggressive strategy"
                )
                return

            if not s2.is_valid(c2):
                print(
                    f"* Battle\n"
                    f"{c1.describe()}"
                    f"\nVS.\n"
                    f"{c2.describe()}"
                    f"\nnow fight!"
                    )
                print(
                    f"Battle error, aborting tournament: Invalid Creature "
                    f"'{c2.name}' for this aggressive strategy"
                )
                return

            print("* Battle *")
            print(c1.describe())
            print("VS.")
            print(c2.describe())
            print("now fight!")

            try:
                s1.act(c1)
                s2.act(c2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal_strat = NormalStrategy()
    defensive_strat = DefensiveStrategy()
    aggressive_strat = AggressiveStrategy()

    # Scenario 1: Basic valid tournament
    run_tournament(
        "Tournament (basic)",
        [(flame_factory, normal_strat), (healing_factory, defensive_strat)],
    )

    print()

    # Scenario 2: Tournament with error (invalid strategy for creature)
    run_tournament(
        "Tournament 1 (error)",
        [
            (flame_factory, aggressive_strat),
            (healing_factory, defensive_strat)
        ],
    )

    print()

    # Scenario 3: Multiple opponents tournament
    run_tournament(
        "Tournament 2 (multiple)",
        [
            (aqua_factory, normal_strat),
            (healing_factory, defensive_strat),
            (transform_factory, aggressive_strat),
        ],
    )


if __name__ == "__main__":
    main()
