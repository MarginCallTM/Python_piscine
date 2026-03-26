from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
import random


class Deck():
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card | str:
        if not self.cards:
            return "Empty Deck"
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        return {
            "total_cards": len(self.cards),
            "creatures": sum(
                1 for card in self.cards if isinstance(card, CreatureCard)
            ),
            "spells": sum(
                1 for card in self.cards if isinstance(card, SpellCard)
            ),
            "artifacts": sum(
                1 for card in self.cards if isinstance(card, ArtifactCard)
            ),
            "avg_cost": round(
                sum(card.cost for card in self.cards) / len(self.cards)
                if self.cards else 0, 2
            )
        }
