from collections.abc import Callable


def spell(target: str, power: int) -> str:
    return f"You hit {target} with {power} power force"


def dammage_spell(target: str, spell: str) -> str:
    return f"{spell} hit {target}"


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


if __name__ == "__main__":

    combined = spell_combiner(dammage_spell, healing_spell)
    print(combined('dragon', 10))
    print()
    power = power_amplifier(dammage_spell, 2)
    print(power('dargon', 2))
