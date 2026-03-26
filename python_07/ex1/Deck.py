from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
import random


class Deck():
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card):
        self.cards.append(card)

    def remove_card(self, card_name: str):
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if not self.cards:
            return "Empty Deck"
        return self.cards.pop(0)

    def get_deck_stats(self):
        return {
            "total_cards": len(self.cards),
            "creature": sum(
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
