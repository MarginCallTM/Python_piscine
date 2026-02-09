class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self.initial_height = height

    def grow(self):
        self.height += 1

    def age_plant(self):
        self.age += 1

    def display_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main():
    plant = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    plant.display_info()

    for day in range(6):
        plant.grow()
        plant.age_plant()

    print("=== Day 7 ===")
    plant.display_info()

    growth = plant.height - plant.initial_height
    print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    main()
