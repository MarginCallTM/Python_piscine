from abc import ABC, abstractmethod
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        pass

    def get_strategy_name(self) -> str:
        return f"{self.name}"

    def prioritize_targets(self, available_targets) -> list:
        pass
