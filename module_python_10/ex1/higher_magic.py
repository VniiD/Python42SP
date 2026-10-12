from collections.abc import Callable


def spell_combiner(
    spell1: Callable, spell2: Callable
) -> Callable:
    """Combine two spells into a single invocation."""
    def combined_spell(
        target: str, power: int
    ) -> tuple[str, str]:
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return (res1, res2)
    return combined_spell


def power_amplifier(
    base_spell: Callable, multiplier: int
) -> Callable:
    """Return a new spell with multiplied power."""
    def amplified_spell(
        target: str, power: int
    ) -> str:
        new_power = power * multiplier
        return base_spell(target, new_power)
    return amplified_spell


def conditional_caster(
    condition: Callable, spell: Callable
) -> Callable:
    """Cast spell conditionally or return 'Spell fizzled'."""
    def conditional_spell(
        target: str, power: int
    ) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional_spell


def spell_sequence(
    spells: list[Callable]
) -> Callable:
    """Return a function that casts all spells in order."""
    def sequential_spell(
        target: str, power: int
    ) -> list[str]:
        results = []
        for s in spells:
            results.append(s(target, power))
        return results
    return sequential_spell


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} with {power}"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power}"

    def true_cond(target: str, power: int) -> bool:
        return power > 10

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(combined("Dragon", 50))

    print("Testing power amplifier...")
    mega_fb = power_amplifier(fireball, 3)
    print(f"Amplified: {mega_fb('Dragon', 10)}")

    print("Testing conditional caster...")
    guarded = conditional_caster(true_cond, fireball)
    print(guarded("Goblin", 5))
    print(guarded("Goblin", 15))

    print("Testing spell sequence...")
    sequence = spell_sequence([fireball, heal])
    print(sequence("Knight", 25))
