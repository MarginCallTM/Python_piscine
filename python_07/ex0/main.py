from ex0.CreatureCard import CreatureCard

if __name__ == "__main__":
    print("=== DataDeck Card Foundation ===\n")
    game_state = {"mana": 6, "battlefield": []}

    print("Testing Abstract Base Class Design:\n")

    print("CreatureCard Info:")
    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    goblin_warrior = CreatureCard("Goblin Warrior", 5, "Common", 2, 8)
    print(fire_dragon.get_card_info())
    print(f"\nPlaying Fire Dragon with {game_state['mana']} mana available:")
    print(f"Playable: {fire_dragon.is_playable(6)}")
    print(f"Play result: {fire_dragon.play(game_state)}")

    print(f"\n{fire_dragon.name} attack {goblin_warrior.name}:")
    print(f"Attack result: {fire_dragon.attack_target(goblin_warrior)}")

    print(f"\nTesting insufficient mana ({game_state['mana']} available):")
    print(f"Playable: {fire_dragon.is_playable(game_state['mana'])}")

    print("Abstract pattern successfully demonstrated!")
