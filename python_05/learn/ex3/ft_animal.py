from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def speak(self) -> str:
        pass

    @abstractmethod
    def move(self) -> str:
        pass

    def describe(self) -> None:
        print(f"{self.name} do {self.move()} and {self.speak()}")


class dog(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def speak(self) -> str:
        return "Woof"

    def move(self) -> str:
        return "Run"


class bird(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def speak(self) -> str:
        return "Tweet!"

    def move(self) -> str:
        return "Fly"


class fish(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def speak(self) -> str:
        return "BlopBlop"

    def move(self) -> str:
        return "Swim"


class broker_dog(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)


if __name__ == "__main__":
    animals = [dog("levrier"), bird("Woodie"), fish("Golden fish")]
    for animal in animals:
        animal.describe()

    b = broker_dog("Rex")

    b.describe()
