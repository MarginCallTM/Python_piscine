from collections.abc import Callable


def dammage_spell(target: str, power: int) -> str:
    return f"{power} hit {target}"


def healing_spell(target: str, power: int) -> str:
    return f"Heal spell restore {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def mult_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return mult_spell


def mana_condition(target: str, power: int) -> bool:
    if power >= 3:
        return True
    else:
        return False


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def new_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return new_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        result = list(map(lambda spell: spell(target, power), spells))
        return result
    return sequence


if __name__ == "__main__":

    print("Testing spell combiner...")
    combined = spell_combiner(dammage_spell, healing_spell)
    print(f"Combined spell result: {combined('dragon', 10)}")
    print()
    print("Testing power amplifier...")
    power = power_amplifier(dammage_spell, 3)
    mega = power_amplifier(dammage_spell, 10)

    print(
        f"Original: {dammage_spell('dragon', 3)},"
        f" Amplified: {power('dragon', 2)}\n")

    print(f"Mega Amplified: {mega('dragon', 10)}\n")

    guarded = conditional_caster(mana_condition, healing_spell)
    print(guarded("Dragon", 5))
    print(guarded("Dragon", 1))
    print()

    spells = [
        dammage_spell,
        healing_spell,
    ]
    print("Testing spell_sequence:")
    sequence = spell_sequence(spells)
    print(f"{sequence('Dragon', 10)}\n")
