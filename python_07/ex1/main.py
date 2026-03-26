from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck

if __name__ == "__main__":
    print("=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    game_state = {"mana": 6, "battlefield": []}
    deck = Deck()
    fireDragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    Lightning_bolt = SpellCard(
        "Lightning Bolt",
        3,
        "Common",
        "Deal 3 damage to target")
    mana_crystal = ArtifactCard("Mana Crystal", 2, "common", 2, "buff")

    deck.add_card(Lightning_bolt)
    deck.add_card(mana_crystal)
    deck.add_card(fireDragon)

    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:\n")
    for card in deck.cards:
        print(f"Draw: {card.get_card_info()}")
        print(card.play(game_state))
