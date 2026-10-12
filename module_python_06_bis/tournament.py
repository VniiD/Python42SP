from ex3 import (
    CreatureFactory,
    FlameFactory,
    TransformCreatureFactory,
)
from ex4 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    InvalidEntityStrategyError,
)


def run_tournament(
    opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print("* Battle *")

    created_pairs = []
    for factory, strategy in opponents:
        creature = factory.create_base()
        created_pairs.append((creature, strategy))

    c1, s1 = created_pairs[0]
    c2, s2 = created_pairs[1]

    print(c1.describe())
    print("VS.")
    print(c2.describe())
    print("now fight!")

    try:
        actions_1 = s1.act(c1)
        for act in actions_1:
            print(act)

        actions_2 = s2.act(c2)
        for act in actions_2:
            print(act)

    except InvalidEntityStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


if __name__ == "__main__":
    flame_f = FlameFactory()
    trans_f = TransformCreatureFactory()
    normal_strat = NormalStrategy()
    agg_strat = AggressiveStrategy()

    print("Tournament 0 (basic)")
    print("[(Flameling+Normal), (Shiftling+Aggressive)]")
    run_tournament([(flame_f, normal_strat), (trans_f, agg_strat)])

    print("\nTournament 1 (error)")
    print("[(Shiftling+Aggressive), (Flameling+Aggressive)]")
    run_tournament([(trans_f, agg_strat), (flame_f, agg_strat)])
