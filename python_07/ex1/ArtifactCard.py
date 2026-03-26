from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            durability: int,
            effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        if self.durability > 0:
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect
            }
        else:
            return {"durability": "Card perimed"}

    def activate_ability(self) -> dict:
        if self.durability > 0:
            self.durability -= 1
            return {"card_played": self.name,
                    "mana_used": self.cost,
                    "effect": self.effect}
        else:
            return {"durability": "burned"}

    def get_card_info(self) -> dict[str, str | int]:
        return {"name": self.name,
                "cost": self.cost,
                "rarity": self.rarity,
                "type": "Artifact",
                }
