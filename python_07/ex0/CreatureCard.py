from ex0.Card import Card
from typing import Dict, List, Any, Optional, Union


class CreatureCard(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            attack: int,
            health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        if attack <= 0 or health <= 0:
            raise ValueError("negatif int triggered")

    def play(self, game_state: dict):
        pass

    def attack_target(self, target):
        pass

    def get_card_info(self) -> dict[str, str | int]:
        return {"name": self.name,
                "cost": self.cost,
                "rarity": self.rarity,
                "attack": self.attack,
                "health": self.health}


if __name__ == "__main__":
    try:
        creature = CreatureCard("titi", 10, "goat", 5, 10)
        creature.get_card_info()
    except ValueError as e:
        print(e)
