from ex0.CreatureCard import CreatureCard

if __name__ == "__main__":
    print("=== DataDeck Card Foundation ===\n")
    game_state = {"mana": 6, "battlefield": []}

    print("Testing Abstract Base Class Design:\n")

    print("CreatureCard Info:")
    fireDragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    goblinWarrior = CreatureCard("Goblin Warrior", 5, "Common", 2, 8)
    print(f"{fireDragon.get_card_info()}")
    print(f"\nPlaying Fire Dragon with {game_state['mana']} mana available:")
    print(f"Playable: {fireDragon.is_playable(6)}")
    print(f"Play result: {fireDragon.play(game_state)}")

    print(f"\n{fireDragon.name} attack {goblinWarrior.name}:")
    print(f"Attack result: {fireDragon.attack_target(goblinWarrior)}")

    print(f"\nTesting insufficient mana ({game_state['mana']} available):")
    print(f"Playable: {fireDragon.is_playable(game_state['mana'])}")

    print("Abstract pattern successfully demonstrated!")
