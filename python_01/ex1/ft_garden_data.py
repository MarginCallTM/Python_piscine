class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def display_info(self):
        print(f"{self.name}: {self.height}cm {self.age} days old")


def main():
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflowe", 80, 45)
    plant3 = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")

    plant1.display_info()
    plant2.display_info()
    plant3.display_info()

if   __name__ == "__main__":
    main()