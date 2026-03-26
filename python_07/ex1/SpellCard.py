from ex0.Card import Card


class SpellCard(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.used = False

    def play(self, game_state: dict) -> dict:
        if not self.used:
            self.used = True
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect_type
            }
        else:
            return {"Card burned": True}

    def resolve_effect(self, targets: list) -> dict:
        return {"caster": self.name,
                "target": [target.name for target in targets],
                "effect_applied": self.effect_type
                }

    def get_card_info(self) -> dict[str, str | int]:
        return {"name": self.name,
                "cost": self.cost,
                "rarity": self.rarity,
                "type": "Spell"
                }
