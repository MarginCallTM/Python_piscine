from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck

if __name__ == "__main__":
    print("=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    game_state = {"mana": 6, "battlefield": []}
    deck = Deck()
    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    lightning_bolt = SpellCard(
        "Lightning Bolt",
        3,
        "Common",
        "Deal 3 damage to target")
    mana_crystal = ArtifactCard(
        "Mana Crystal",
        2,
        "common",
        2,
        "Permanent: +1 mana per turn")

    deck.add_card(lightning_bolt)
    deck.add_card(mana_crystal)
    deck.add_card(fire_dragon)

    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:\n")
    while deck.cards:
        card = deck.draw_card()
        info = card.get_card_info()
        print(f"Drew: {info['name']} ({info['type']})")
        print(f"Play result: {card.play(game_state)}\n")

    print("\nPolymorphism in action: Same"
          " interface, different card behaviors!")
