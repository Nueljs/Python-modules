def artifact_sorter(artifact: list[dict]) -> list[dict]:
    artifact_order: list[dict] = sorted(
        artifact, key=lambda artifact: artifact['power'], reverse=True)
    return artifact_order


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    mages_order: list[dict] = list(filter(
        lambda mage: mage["power"] >= min_power, mages
    ))
    return mages_order


def spell_transformer(spells: list[str]) -> list[str]:
    transformed_spells: list[str] = list(map(
        lambda spell: "* " + spell + " *", spells
    ))
    return transformed_spells


def mage_stats(mages: list[dict]) -> dict:
    max_power: int = max(
        mages, key=lambda mage: mage["power"]
    )['power']
    min_power: int = min(
        mages, key=lambda mage: mage["power"]
    )['power']
    avg_power: float = round(sum(list(map(
        lambda mage: mage["power"], mages
    ))) / len(mages), 2)
    stats: dict = {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }
    return stats


if __name__ == "__main__":
    artifacts: list[dict] = [
        {'name': 'Lightning Rod', 'power': 83, 'type': 'relic'},
        {'name': 'Ice Wand', 'power': 67, 'type': 'focus'},
        {'name': 'Crystal Orb', 'power': 116, 'type': 'accessory'},
        {'name': 'Water Chalice', 'power': 67, 'type': 'weapon'}
        ]

    mages: list[dict] = [
        {'name': 'Sage', 'power': 57, 'element': 'fire'},
        {'name': 'Morgan', 'power': 98, 'element': 'shadow'},
        {'name': 'Riley', 'power': 73, 'element': 'wind'},
        {'name': 'Storm', 'power': 78, 'element': 'earth'},
        {'name': 'Zara', 'power': 90, 'element': 'lightning'}
        ]

    spells: list[str] = ['shield', 'lightning', 'tsunami', 'fireball']

    print()
    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']}"
          f" power) comes before {sorted_artifacts[1]['name']}"
          f" ({sorted_artifacts[1]['power']} power)")

    print("\nTesting power filter...")
    filtered_mages = power_filter(mages, 75)
    print("Mages with power >= 75:", [mage['name'] for mage in filtered_mages])

    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    print(" ".join(transformed))

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Max power: {stats['max_power']}")
    print(f"Min power: {stats['min_power']}")
    print(f"Avg power: {stats['avg_power']}")