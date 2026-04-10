def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    result = sorted(artifacts, key=lambda x: x['power'], reverse=True)
    return result


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    result = list(filter(lambda mage: mage['power'] >= min_power, mages))
    return result


def spell_transformer(spells: list[str]) -> list[str]:
    result = list(map(lambda x: f"* {x} *", spells))
    return result


def mage_stats(mages: list[dict]) -> dict:
    result = {
        'max_power': max(mages, key=lambda x: x['power'])['power'],
        'min_power': min(mages, key=lambda x: x['power'])['power'],
        'avg_power': round(
            sum(map(lambda x: x['power'], mages)) / len(mages), 2)
    }
    return result


if __name__ == "__main__":
    artifact = [
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'},
        {'name': 'Shadow Blade', 'power': 78, 'type': 'weapon'}
    ]

    mages = [
        {'name': 'Lancelot', 'power': 4, 'element': 'Fire'},
        {'name': 'Merlin', 'power': 3, 'element': 'mana'},
        {'name': 'Calipso', 'power': 1, 'element': 'necro'}
    ]

    spells = ['Adoken', 'Abra', 'cadabra', 'test']

    wizard = [
        {'name': 'Lancelot', 'power': 4, 'element': 'Fire'},
        {'name': 'Merlin', 'power': 3, 'element': 'mana'},
        {'name': 'Calipso', 'power': 1, 'element': 'necro'}
    ]

    print(f"{artifact_sorter(artifact)}\n")
    print(f"{power_filter(mages, 2)}\n")
    print(f"{spell_transformer(spells)}\n")
    print(f"{mage_stats(wizard)}\n")

    print("Testing artifact sorter...")
    name1, pow1 = artifact[0]['name'], artifact[0]['power']
    name2, pow2 = artifact[1]['name'], artifact[1]['power']
    print(f"{name1} ({pow1} power) comes before {name2} ({pow2} power)")
    print("\nTesting spell transformer...")
    print(f"{' '.join(spell_transformer(spells))}")
