from ex0.CreatureCard import CreatureCard

if __name__ == "__main__":
    player1 = CreatureCard("Pikachu", 5, "Common", 2, 8)
    player2 = CreatureCard("Tortank", 5, "rare", 4, 8)

    print(f"{player1.get_card_info()}")
    print(f"{player2.get_card_info()}")

    print(f"{player1.attack_target(player2)}")
    print(f"{player2.get_card_info()}")
