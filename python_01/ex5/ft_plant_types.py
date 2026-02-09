class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def display_info(self):
        return (f"{self.name}: {self.height} cm, {self.age} days")


class Flower(Plant):

    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def display_info(self):
        return f"{self.name}(Flower):{self.height}cm\
,{self.age}days,{self.color} color"

    def bloom(self):
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def display_info(self):
        return f"{self.name}(Tree) {self.height}cm,\
{self.age}days, {self.trunk_diameter}cm diameter"

    def produce_shade(self):
        shade_area = (self.trunk_diameter * self.height) // 100
        print(f"{self.name} provides {shade_area} squares meters of shade\n")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def display_info(self):
        return f"{self.name}(Vegetable): {self.height}cm,\
{self.age} days,{self.harvest_season} harvest"

    def show_nutrition(self):
        print(f"{self.name} is rich in {self.nutritional_value}")


def main():
    print("=== Garden Plant Types ===\n")

    # Flower
    rose = Flower("Rose", 25, 30, "red")
    #tulip = Flower("Tulip", 35, 28, "yellow")

    # Tree
    oak = Tree("Oak", 500, 1825, 50)
    #pine = Tree("Pin", 800, 3650, 60)

    # Vegetables
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    #carrot = Vegetable("Carrot", 15, 120, "fall", "vitamin A")

    print(rose.display_info())
    rose.bloom()

    print(oak.display_info())
    oak.produce_shade()

    print(tomato.display_info())
    tomato.show_nutrition()


if __name__ == "__main__":
    main()
