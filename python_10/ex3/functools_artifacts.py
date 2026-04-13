from functools import reduce, partial, lru_cache, singledispatch
from collections.abc import Callable
from typing import Any
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if operation not in operations:
        raise ValueError(f"Unknow operation: {operation}")

    return reduce(operations[operation], spells)


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"Basic enchantment power: {power}, element: {element} on {target}"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    new_function_fire = partial(base_enchantment, power=50, element="Fire")
    new_function_water = partial(base_enchantment, power=50, element="Water")
    new_function_air = partial(base_enchantment, power=50, element="Air")
    return {
        "Fire": new_function_fire,
        "Water": new_function_water,
        "Air": new_function_air}


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def cast_spell(spell):
        return "Unknown spell type"

    @cast_spell.register(int)
    def _(spell):
        return f"Damage spell: {spell} damage"

    @cast_spell.register(str)
    def _(spell):
        return f"Enchantment: {spell}"

    @cast_spell.register(list)
    def _(spell):
        return f"Multi-cast: {len(spell)} spells"
    return cast_spell


if __name__ == "__main__":
    try:
        print("------ Testing spell reducer... ------")
        print(f"Add: {spell_reducer([10, 20, 30], 'add')}")
        print(f"Multiply: {spell_reducer([10, 20, 30], 'multiply')}")
        print(f"Max: {spell_reducer([10, 20, 30], 'max')}")
        print(f"Min: {spell_reducer([10, 20, 30], 'min')}")
        print(f"Test: {spell_reducer([10, 20, 30], 'test')}\n")
    except Exception as e:
        print(e)
    try:
        print("------ Testing Partial_enchanter ------\n")
        base = base_enchantment(10, "Fire", "Mouton")
        print(base)
        enchanter = partial_enchanter(base_enchantment)
        print(enchanter["Water"](target="Dragon"))
    except Exception as e:
        print(e)
    try:
        print("\n------ Testing memoized fibonacci.. ------")
        fibo = memoized_fibonacci(0)
        print(f"fib(0): {fibo}")
        print(memoized_fibonacci.cache_info())
        fibo = memoized_fibonacci(1)
        print(f"\nfib(1): {fibo}")
        print(memoized_fibonacci.cache_info())
        fibo = memoized_fibonacci(10)
        print(f"\nfib(10): {fibo}")
        print(memoized_fibonacci.cache_info())
        fibo = memoized_fibonacci(15)
        print(f"\nfib(15): {fibo}")
        print(memoized_fibonacci.cache_info())
    except Exception as e:
        print(e)
    try:
        print("\n------ Testing spell dispatcher.. ------")
        dispatcher = spell_dispatcher()
        print(dispatcher(42))
        print(dispatcher("Fireball"))
        print(dispatcher(["fireball", 42, "lightning"]))
        print(dispatcher(3.14))
    except Exception as e:
        print(e)