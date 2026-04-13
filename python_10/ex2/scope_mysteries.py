from collections.abc import Callable


def mage_counter() -> Callable:
    n = 0

    def count() -> int:
        nonlocal n
        n += 1
        return n
    return count


def spell_accumulator(initial_power: int) -> Callable:

    def count(add: int) -> int:
        nonlocal initial_power
        initial_power += add
        return initial_power
    return count


def enchantment_factory(enchantment_type: str) -> Callable:

    def factory(item: str) -> str:
        return f"{enchantment_type} {item}"
    return factory


def memory_vault() -> dict[str, Callable]:
    storage = {}

    def store(key: str, value) -> None:
        storage[key] = value

    def recall(key: str) -> str:
        return storage.get(key, "Memory not found")
    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("------ Mage counter ------")
    test_a = mage_counter()
    print(f"test_a call 1: {test_a()}")
    print(f"test_a call 2: {test_a()}")
    print(f"test_a call 3: {test_a()}\n")

    test_b = mage_counter()
    print(f"test_b call 1: {test_b()}")
    print(f"test_b call 2: {test_b()}")
    print(f"test_b call 3: {test_b()}\n")

    print(f"test_a call 4: {test_a()}")

    print("\n------ Spell_Accumulator ------")
    spell_a = spell_accumulator(100)
    print(f"spell_a call 1: {spell_a(20)}")
    print(f"spell_a call 2: {spell_a(20)}\n")

    spell_b = spell_accumulator(100)
    print(f"spell_b call 1: {spell_b(10)}")
    print(f"spell_b call 2: {spell_b(10)}\n")

    print("------ Testing enchantment factory ------")
    enchantment = enchantment_factory("Frozen")
    print(f"{enchantment('Shield')}")
    print(f"{enchantment('Magic stick')}\n")

    enchantment = enchantment_factory("Fire")
    print(f"{enchantment('sword')}")
    print(f"{enchantment('helmet')}\n")

    print("Testing memory vault...")
    vault = memory_vault()
    vault["store"]("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")

