from alchemy.grimoire.spellbook import record_spell
from alchemy.grimoire.validator import validate_ingredients

try:
    print("=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    ingredient_name0 = "fire air"
    ingredient_name1 = "dragon scale"
    ingredient_0 = validate_ingredients(ingredient_name0)
    ingredient_1 = validate_ingredients(ingredient_name1)

    print(f"validate_ingredients({ingredient_name0}): {ingredient_0}")
    print(f"validate_ingredients({ingredient_name1}): {ingredient_1}")

    print("\nTesting spell recording with validation:")
    record_name0 = "Fireball"
    record_0 = record_spell(record_name0, "fire air")
    record_name1 = "Dark Magic"
    record_1 = record_spell(record_name1, "shadow")

    print(f"record_spell({record_name0}, fire air):{record_0}")
    print(f"record_spell({record_name1}, shadow): {record_1}")

    print("\nTesting late import technique:")
    record_name3 = "Lightning"
    record_2 = record_spell(record_name3, "air")
    print(f"record_spell({record_name3}, lightning): {record_2}")
except Exception:
    print("Circular error detected")
print("\nCircular dependency curse avoided using late imports!")
print("All spells processed safely!")
