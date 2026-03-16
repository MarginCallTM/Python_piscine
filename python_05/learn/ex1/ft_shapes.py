from abc import ABC, abstractmethod


class shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def describe(self) -> None:
        pass


class circle(shape):
    def __init__(self, rayon: int) -> None:
        self.rayon = rayon

    def area(self) -> float:
        result = 3.14159 * self.rayon ** 2
        return result

    def describe(self):
        result = self.area()
        print(f"Circle with radius {self.rayon}, area = {result:.2f}")


class rectangle(shape):
    def __init__(self, widht: int, height: int) -> None:
        self.widht = widht
        self.height = height

    def area(self) -> float:
        result = self.widht * self.height
        return result

    def describe(self):
        result = self.area()
        print(f"Rectangle = {self.widht} x {self.height} = {result}")


if __name__ == "__main__":

    my_circle = circle(15)
    my_rectangle = rectangle(15, 20)

    my_circle.area()
    my_circle.describe()

    my_rectangle.area()
    my_rectangle.describe()
