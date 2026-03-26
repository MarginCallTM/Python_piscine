from ex0.Card import Card


class CreatureCard(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            attack: int,
            health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        if attack <= 0 or health <= 0:
            raise ValueError("negatif int triggered")

    def play(self, game_state: dict) -> dict:
        game_state['mana'] -= self.cost
        return {"card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
                }

    def attack_target(self, target: "CreatureCard") -> dict[str, str | int]:
        target.health -= self.attack
        return {"attacker": self.name,
                "target": target.name,
                "damage_dealt": self.attack,
                "combat_resolved": True
                }

    def get_card_info(self) -> dict[str, str | int]:
        return {"name": self.name,
                "cost": self.cost,
                "rarity": self.rarity,
                "type": "Creature",
                "attack": self.attack,
                "health": self.health}


if __name__ == "__main__":
    try:
        creature = CreatureCard("titi", 10, "goat", 5, 10)
        creature.get_card_info()
    except ValueError as e:
        print(e)
