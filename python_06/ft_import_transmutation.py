import alchemy
from alchemy import create_water
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_fire, create_water

print("=== Import Transmutation Mastery ===\n")
print("Method 1 - Full module import:")

fire = create_fire()
print(f"alchemy.elements.create_fire(): {fire}")

print("\nMethod 2 - Specific function import:")
water = create_water()
print(f"create_water(): {water}")

print("\nMethod 3 - Aliased import:")
healing = heal()
print(f"heal(): {healing}")

print("\nMethod 4 - Multiple imports:")
earth = alchemy.elements.create_earth()
fire = alchemy.elements.create_fire()
strength = alchemy.potions.strenght_potion()

print(f"create_earth(): {earth}")
print(f"create_fire(): {fire}")
print(f"strength_potion(): {strength}")

print("\nAll import transmutation methods mastered!")
