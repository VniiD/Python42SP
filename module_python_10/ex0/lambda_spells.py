def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort magic artifacts by power in descending order using lambda."""
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Filter mages by minimum power level using filter and lambda."""
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Transform spell names by add prefix and suffix using map and lambda."""
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Calculate maximum, minimum, and average power levels using lambdas."""
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    max_p = max(mages, key=lambda m: m['power'])['power']
    min_p = min(mages, key=lambda m: m['power'])['power']
    avg_p = round(sum(map(lambda m: m['power'], mages)) / len(mages), 2)

    return {
        'max_power': max_p,
        'min_power': min_p,
        'avg_power': avg_p
    }


if __name__ == "__main__":
    # Test cases to verify the implementation
    artifacts_test = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'relic'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Shadow Wand', 'power': 78, 'type': 'weapon'}
    ]

    mages_test = [
        {'name': 'Alex', 'power': 95, 'element': 'fire'},
        {'name': 'Jordan', 'power': 80, 'element': 'water'},
        {'name': 'Taylor', 'power': 60, 'element': 'earth'}
    ]

    spells_test = ['fireball', 'heal', 'shield']

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts_test)
    art0 = sorted_artifacts[0]
    art1 = sorted_artifacts[1]
    print(
        f"{art0['name']} ({art0['power']} power) "
        f"comes before {art1['name']} ({art1['power']} power)"
    )

    print("Testing spell transformer...")
    transformed_spells = spell_transformer(spells_test)
    for s in transformed_spells:
        print(s)

    print("Testing mage stats...")
    print(mage_stats(mages_test))
