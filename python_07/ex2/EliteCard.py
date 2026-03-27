from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class ElitCard(Card, Combatable, Magical):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            damage: int,
            defense: int,
            combat_type: str,
            hp: int,
            mana: int,
            total_mana: int):
        super().__init__(name, cost, rarity)
        self.damage = damage
        self.defense = defense
        self.combat_type = combat_type
        self.hp = hp
        self.still_alive = True
        self.mana = mana
        self.total_mana = total_mana

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": self.mana
        }

    def channel_mana(self, amount: int) -> dict:
        self.total_mana += amount
        return {
            "channeled": amount,
            "total_mana": self.total_mana
        }

    def get_magic_stats(self) -> dict:
        return {
            "mana": self.mana,
            "total_mana": self.total_mana
        }

    def get_combat_stats(self) -> dict:
        return {
            "hp": self.hp,
            "defense": self.defense,
            "damage": self.damage,
            "combat_type": self.combat_type,
        }

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.damage,
            "combat_type": self.combat_type
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = max(0, incoming_damage - self.defense)
        self.hp = self.hp - damage_taken
        self.still_alive = self.hp > 0
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": self.defense,
            "still_alive": self.still_alive
        }

    def play(self, game_state: dict) -> dict:
        pass
