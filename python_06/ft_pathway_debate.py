import alchemy.transmutation
from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life

print("=== Pathway Debate Mastery ===\n")
print("Testing Absolute Imports (from basic.py):")
gold = lead_to_gold()
gem = stone_to_gem()

print(f"lead_to_gold(): {gold}")
print(f"stone_to_gem(): {gem}")

print("\nTesting Relative Imports (from advanced.py)")
philosopher = philosophers_stone()
life_elixir = elixir_of_life()

print(f"philosophers_stone(): {philosopher}")
print(f"elixir_of_life(): {life_elixir}")

print("\nTesting Package Access: ")
lead = alchemy.transmutation.lead_to_gold()
stone = alchemy.transmutation.philosophers_stone()
print(f"alchemy.transmutation.lead_to_gold(): {lead}")
print(f"alchemy.transmutation.philosophers_stone(): {stone}\n")
print("Both pathways work! Absolute: clear, Relative: concise")
