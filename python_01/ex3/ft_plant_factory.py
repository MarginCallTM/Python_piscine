class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def display_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def main():
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 364),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]

    print("=== Plant Factory Output ===")

    for plant in plants:
        plant.display_info()

    print(f"\nTotal plants created: {len(plants)}")


if __name__ == "__main__":
    main()
