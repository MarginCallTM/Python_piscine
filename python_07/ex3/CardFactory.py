from abc import ABC, abstractmethod
from ex0.Card import Card
from ex1.Deck import Deck
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class CardFactory(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def create_creature(self, name_or_power: str | int |
                        None = None) -> Card:
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> Deck:
        pass

    @abstractmethod
    def get_supported_types(self):
        pass
